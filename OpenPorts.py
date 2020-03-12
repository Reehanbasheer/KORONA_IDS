#!/usr/bin/env python3
import socket
import argparse
import sys
import logging

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import ICMP, IP, conf, sr


# turn off verbosity
conf.verb = 0


def alive(ip):
	""" Before scanning, Check if the host is online
	"""

	# pinging ip
	responses, unanswered = sr(IP(dst=ip)/ICMP(), timeout=0.2, retry=3)

	for s,r in responses:
		return (r[ICMP].type == 0)

	return False


def openport(ip, ports):

	isopen = False
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)
	try:
		sock.connect((ip, ports))
		isopen = True
	except socket.error:
		pass
	finally:
		sock.close()

	return isopen


def scaphost(ip, ports):
	""" Hit and run method to connect to each port
	"""

	scannedport = []

	for p in ports:

		if openport(ip, p):
			scannedport.append(p)

	return scannedport


def getports(pstring):
	""" extracting the ports from the cmd line args
	"""

	ports = []

	for token in pstring.split(','):

		if '-' in token:
			# a range of ports
			start, end = [ int(i) for i in token.split('-') ]
			[ ports.append(int(p)) for p in range(start, end + 1) ]
		else:
			ports.append(int(token))

	ports.sort()
	return ports


def gethosts(hstring):
	""" retireve the hosts and scan, by the usage of provided netmasks
	"""

	if not '/' in hstring:
		return [ hstring ]


	startipadd  = hstring.split('/')[0]
	lastoctade  = int(startipadd.split('.')[-1])
	firstoctade = int(startipadd.split('.')[0]) 
	netmask    = hstring.split('/')[1]

#------------- Feature being use for Class C IP's-------------------------------------------------------------------------------------------------------------------------
	if netmask == '24' and firstoctade >= 192:
		hosts  = []
		net    = startipadd[:startipadd.rfind('.')] + '.'
		for i in range(lastoctade, 2**8 - 1):
			hosts.append(net + str(i))

		return hosts
	return [ startipadd ]



if __name__ == "__main__":

#-------------- parsing the CLI arguments--------------------------------------------------------------------------------------------------------------------------------
	print('Starting ...', end='')
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', action="store", dest="ports", required=True, type=str, help="Specify the Ports that has to be Scanned, e.g.,\
		 -p 10, -p 70-140, -p 96,98-169")
	parser.add_argument('-i', action="store", dest="hosts", required=True, type=str, help="Specify the hosts/IPs that has to be Scanned, e.g.,\
		 -i 10.10.21.6, -i 10.10.22.2/32")

	# parse cmd line args
	parse_res = parser.parse_args(sys.argv[1:])

	ports   = getports(parse_res.ports)
	hosts   = gethosts(parse_res.hosts)
	print('\r' + ' '*30 + '\rStarting.\nScanning.\n')


	for index, host in enumerate(hosts):
		print('Scanned %d/%d' % (index + 1, len(hosts)), end='\r')
		if alive(host):
			openports = scaphost(host, ports)
			print(' ' * 30 + '\r-- %s --' % host)

			if len(ports) == 1:
				print('   %d/tcp' % ports[0], '-- %s' % ('Open Port' if(len(openports)) else 'Closed Port'))

			else:
				for p in openports:
					print('   %d/tcp -- %10s' % (p, 'Open Port'))

	print(' ' * 50 + '\r\nScanning Done')

