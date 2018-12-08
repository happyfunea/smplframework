#!/usr/bin/python
#-*-coding:utf-8-*-
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
from requests import get
from json import loads as ngelod
from time import sleep as bobo
class proxy():
	def __init__(self):
		print '\tCoded By : github.com/happyfunea'
		print G+'-----------------------'
		print N+'|[*] Checking Proxy...|'
		print G+'-----------------------'
		self.knt = raw_input(R+' [=] Press Enter untuk Melanjutkan...')
		print N+' [*]'+G+' Tunggu..'
		bobo(2)
		self.url = get('https://api.getproxylist.com/proxy').text
		self.js = ngelod(self.url)
		print N+' [*]'+G+' Checking...'
		bobo(3)
		print N+'[=]'+G+' Result >>> '
		print G+'---------------------------------------------'
		print N+'[*]'+G+' IP : '+R, self.js['ip']
		print N+'[*]'+G+' proxy : '+R, self.js['port']
		print N+'[*]'+G+' protocol : '+R, self.js['protocol']
		print N+'[*]'+G+' anonymity : '+R, self.js['anonymity']
		print N+'[*]'+G+' download speed : '+R, self.js['downloadSpeed']
		print N+'[*]'+G+' second to first byte : '+R, self.js['secondsToFirstByte']
		print G+'---------------------------------------------'
