#! /usr/bin/python
# 06.08.2017 (c) by hendriyawan (mr_silent)
# under license by hendriyawan
# This program free software software, you can redistribute it and/or modify with give some credits
from core import console
import os, sys
con = console.pyConsole()

class Token:
	def __init__(self):
		self.tokens = []
		
	#find token files
	def find_token(self, path):
		self.path = path
		for token in os.listdir(self.path):
			if token.endswith('.txt'):
				self.tokens.append(os.path.join(token))
				
		total = len(self.tokens)
		if total > 0:
			print con.Succ('token available : '+str(total)+'\n')
			x = 0
			while x < total:
				for index in self.tokens:
					x = x+1
					print '    '+con.Num(str(x), index)
			print ""
		else:
			print con.Err('token not available in '+self.path+' directory !')
			print con.Err('usage : python fbup.py --help\n')
			sys.exit(1)
			
	#get tokens
	def get_token(self, index):
		self.token = ""
		self.path = 'token/'
		if not index:
			print con.Err('no token selected !\n')
			sys.exit(1)
		else:
			self.index = int(index) -1
			
		try:
			f = open(self.path+self.tokens[self.index], 'r')
			for value in f.readlines():
				self.token += value
			f.seek(0)
			char = f.read(1)
			if not char:
				print con.Err('token is empty in '+self.path+self.tokens[self.index]+' file !\n')
				sys.exit(1)
			else:
				return self.token
			f.close()
			
		except Exception, e:
			print con.Err(e.message+' !\n')
			sys.exit(1)
		