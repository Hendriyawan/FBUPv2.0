#! /usr/bin/python
# 06.08.2017 (c) by hendriyawan (mr_silent)
# under license by hendriyawan
# This program free software software, you can redistribute it and/or modify with give some credits
# slow_print( imam basyari )
import os
import sys
import time

""" colors """
R = '\x1b[1;31m'
G = '\x1b[1;32m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
HB = '\x1b[1;38;5;32m'
D = '\x1b[0m'

def set_windowTitle(title):
	setTitle = "echo -ne '\e]0;%s\007'" %str(title)
	os.system('clear')
	os.system(setTitle)
	
def slow_print(char):
	for c in char + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1.0/95)

def Banner():
	slow_print(HB+"      ,,,____   __")
	slow_print(HB+"     /"+W+"8888**"+HB+"/  /$$\x5c  "+Y+"  FACEBOOK UP "+C+"v2.0")
	slow_print(HB+"  __/"+W+"888"+HB+"/__   /$$$$\x5c "+W+"  (c) GDEV 2017")
	slow_print(HB+" /"+W+"8888888*"+HB+"/  /$$$$$$\x5c"+W+"  script for update status")
	slow_print(HB+"   /"+W+"888"+HB+"/       |$$|")
	slow_print(HB+"  /"+W+"888"+HB+"/        |$$|"+D)
	print""
	
class pyConsole:
	
	
	R = '\x1b[1;31m'
	G = '\x1b[1;32m'
	B = '\x1b[1;34m'
	Y = '\x1b[1;33m'
	C = '\x1b[1;36m'
	HB = '\x1b[1;38;5;32m'
	D = '\x1b[0m'
	
	def Proc(self, mesg):
		return(self.B+'[*] '+self.D+mesg)
	def Err(self, mesg):
		return(self.R+'[-] '+self.D+mesg)
	def Warn(self, mesg):
		return(self.Y+'[!] '+self.D+mesg)
	def Succ(self, mesg):
		return(self.G+'[+] '+self.D+mesg)
	def Num(self,num, mesg):
		return(self.Y+'['+self.D+num+self.Y+'] '+self.D+mesg)
		
		