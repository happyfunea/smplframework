#!/usr/bin/python
#-*-ckding:utf-8-*-
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
try:
	from requests import get,post
	from time import sleep as turu
	from sys import exit
except Exception as a:
	print (a);exit()
#TCP Port Scan

class bangsad():
	def __init__(self):
		print '\tCoded By : Github.com/happyfunea\n\tTCP Port Scan'
		self.host = raw_input('Enter Ip Address : '+G)
		print R+'[!] Waiting..';turu(1)
		self.url = get('https://api.hackertarget.com/nmap/?q='+self.host)
		print C+"---------------------Result----------------------"+W
		print self.url.text