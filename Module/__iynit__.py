#!/usr/bin/python
#-*-coding:utf-8-*-
from requests import get,post
from time import sleep as turu
import sys
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
class Search():
	def __init__(self):
		print '\tCoded By : Github.com/happyfunea\n\tWhois Lookup'
		self.dom = raw_input('Enter ip or domain : '+G)
		try:
			print R+'[!] Waiting..';turu(1)
			self.fil = open('Whois.txt', 'w')
			self.url = get('https://api.hackertarget.com/whois/?q='+self.dom)
			self.fil.write(self.url.text)
			print C+"-----------Result------------"+W
			print self.url.text
			self.fil.close()
		except Exception as a:
			sys.exit()