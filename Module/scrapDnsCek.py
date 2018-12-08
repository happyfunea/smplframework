#!/usr/bin/python
#-*-coding:utf-8-*-
''''SARAN MENGGUNAKAN VPN'''
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
banner = G+'''\t ------------\033[34m[\033[0m====\033[34m]\033[1;32m------------
\t  Title Program : Reverse Dns
\t Coded By : github.com/happyfunea
\t ------------\033[34m[\033[0m====\033[34m]\033[1;32m------------
'''
#Checking Import
try:
	from random import random
	import sys
	from Queue import Queue
	from threading import Thread
	from mechanize import Browser
	from requests import get,post
	from time import sleep as turu
	from bs4 import BeautifulSoup as bs
except Exception as c:
	print '''========×××========
{}
========×××========'''.format(c)
#classed tools
def writing(O):
	for x in O:
		sys.stdout.write(x)
		sys.stdout.flush()
		turu(random() * 0.11)

class Dcek():
	def __init__(self):
			self.inp = raw_input('[?] Dns : '+B)
			self.br = Browser()
			self.br.set_handle_robots(False)
			self.br.set_handle_referer(True)
			self.br.addheaders=[('User-agent', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36')]
			self.br._factory.is_html = True
			self.br.open('https://dnschecker.org/reverse-dns.php')
			writing(W+'[*]'+B+' Connecting..\n')
			turu(1)
			self.br.select_form(nr=0)
			self.br.form['ip'] = self.inp
			self.br.submit()
			self.geting = self.br.geturl()
			self.url = post(self.geting, data = {'ip':self.inp}).text
			self.soup = bs(self.url, 'html.parser')
			self.tag = self.soup.find_all('p', class_='lead')
			for self.c in self.tag:
				try:
					print G+'________________________________'
					print W+'[=]'+R, self.c.text
					print G+'________________________________'
				except Exception as c:
					print (c)
				
threader = []
for lol in threader:
	t = Thread(target=Dcek, args = (self))
	t.daemon = True
	threader.append(t)
	t.start()
