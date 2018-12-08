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
#R3v3rs3-Ip-LookUp
class lokup():
	def __init__(self):
		try:
			print '\tCoded By : github.com/happyfunea\n\tReverse-Ip-LookUp'
			self.host = raw_input(N+'Enter Ip Address : '+G)
			print R+'[!] Waiting..';turu(1)
			self.file = open('Hasil.txt', 'w')
			self.url = get('https://api.hackertarget.com/reverseiplookup/?q='+self.host).text
			print C+"-----------Result------------"+W
			self.file.write(self.url)
			print self.url
			self.file.close()
		except Exception as wibu:
			print '''=========-3r00r-=========
{}
=========-------========='''.format(wibu);exit()