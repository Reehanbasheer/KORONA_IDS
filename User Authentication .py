from passlib.hash import pbkdf2_sha256
import subprocess
import mysql.connector
import re
import uuid 
import geocoder
import requests
import smtplib
	from email.MIMEMultipart import MIMEMultipart
	from email.MIMEBase import MIMEBase
	from email.MIMEText import MIMEText
	from email.Utils import COMMASPACE, formatdate
	from email import Encoders
import os

def sub_pro:
	user= 'sudo ssh %s@%s';
	pwd= encoding()
	process=subprocess.Popen([user,pwd,mac_add_for],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stderr=process.communicate()

def database_connection(pwd):
	username=input("username");
	con=mysql.connector.connect(host="localhost", user="root",password="liza12345",database="authentication")
	cursor=con.cursor()
	
	sql=("select mac_add from user where usrname='%s' and pwd='%s'")
	cursor.execute(sql)
	
	else if user!=username and pwd==password and mac_add_for==mac;
		print "Error in connecting...Invalid details!"
		sendmail();
	else if user==username and pwd!=password and mac_add_for==mac;
		print "Error in connecting...Invalid details!"
		sendmail();
	else if user!=username and pwd!=password and mac_add_for==mac;
		print "Error in connecting...Invalid details!"
	else if user==username and pwd==password and mac_add_for!=mac;
		freegeoip = "https://freegeoip.app/json/"
		geo_r = requests.get(freegeoip)
		geo_json = geo_r.json()
		address=input('enter an address: ')
		g= geocoder.google(address)
		latitude_address=g.latlng[0]
		longitude_address=g.latlng[1]
		user_postition = [geo_json["latitude"], geo_json["longitude"]]
		latitude_ip=user_postition[0]
		longitude_ip=user_postition[1]
		#Calculate the great circle distance between two points on the earth (specified in decimal degrees)
		from math import radians, cos, sin, asin, sqrt
		# convert decimal degrees to radians 
		longitude_address, latitude_address, longitude_ip, latitude_ip = map(radians, [longitude_address, latitude_address, longitude_ip, latitude_ip])
		# haversine formula 
		dlon = longitude_ip - longitude_address 
		dlat = latitude_ip - latitude_address 
		a = sin(dlat/2)**2 + cos(latitude_address) * cos(latitude_ip) * sin(dlon/2)**2
		c = 2 * asin(sqrt(a)) 
		km = 6367 * c
		#end of calculation
		#limit decimals
		km = ('%.0f'%km)
		print(address+' is about '+str(km)+' km away from you trying to access your system')
		
	else:
		
		cmd = 'ssh'user '@' % ip -y
		p   = Popen(cmd, shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
		res = p.stdout.read()
	con.commit()

#def check():
	#if 
		#write the code to store mac us arp
		cmd = 'arp -a %s' % ip
		p   = Popen(cmd, shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
		res = p.stdout.read()
		mac1 = hstring.split(':')[0]
		mac2  = int(startipadd.split(':')[-1])
		mac3 = int(startipadd.split(':')[0]) 
		mac4    = hstring.split(':')[1]
		mac=mac1+mac2+mac3+mac4
def mac_add_format():
	#print("MAC address in easy format: ",end="")
	mac_add_for= ':',join(re.finall('..','%012x; %uuid.getnode()))
	

def encoding(pwd):
	hash=pbkdf2_sha256.encrypt(pwd,rounds=200,salt_size=16)
	return hash
if __name__="__main__":
	database_connection(encoding(get_data()))
def sendMail(to, fro, subject, text, files=[],server="localhost"):
	    assert type(to)==list
	    assert type(files)==list
	
	
	    msg = MIMEMultipart()
	    msg['From'] = admin@yourdomainrocks.com
	    msg['To'] = database_connection(sql1)
	    msg['Date'] = formatdate(localtime=True)
	    msg['Subject'] = Your account has been trying to work.
	
	    msg.attach( MIMEText(This is to inform you that your account has been tried to access from <km> km away from the longitude <lon> and latitude <lati>. please do contact your system admin for further details as soon as possible if you want to add the following mac address : <mac>) )

	    smtp = smtplib.SMTP(server)
	    smtp.sendmail(fro, to, msg.as_string() )
	    smtp.close()





