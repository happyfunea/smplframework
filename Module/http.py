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
try:
	from requests import get,post
	from time import sleep as turu
	from sys import exit
except:
	print 'Module Ada Yg Kurang'
	exit()

class httphead():
	def __init__(self):
		print '\tCoded by : github.com/happyfunea\n\tExample : site.com'
		self.dom = raw_input(N+'Host : '+G)
		self.url = get('https://api.hackertarget.com/httpheaders/?q=http://'+self.dom).text
		print C+"-----------Result------------"+W
		print self.url
