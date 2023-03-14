import os
import time
from requests import get
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def sendMessage(ipAddress):
    client = Client(os.getenv("SID"), os.getenv("AUTH"))
    
    message = client.messages.create(
    	from_ = os.getenv("TWILIO_NUMBER"),
    	body = '{} is the new External IP'.format(ipAddress),
    	to = os.getenv("PERSONAL_NUMBER")
    )
    
    print(message.sid)

def get_ip():
	ip = get('https://api.ipify.org').content.decode('utf8')
	return '{}'.format(ip)

def main():
	print("check_my_ip.py is running.")
	ip_checker = False

	while ip_checker == False:
		f = open("ip.txt", "r")
		ip = f.readline()
		f.close()

		if str(ip) == str(get_ip()):
			print("Same IP.")
			time.sleep(3600)
		else:
			print("Sending new IP to {}".format(os.getenv("PERSONAL_NUMBER")))
			sendMessage(str(get_ip()))

			f = open("ip.txt", "w")
			f.write(str(get_ip()))
			f.close()
			time.sleep(3600)

main()







