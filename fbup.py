#! /usr/bin/python
#! /system/bin/python
# -*- coding : utf-8 -*-
# 06.08.2017 (c) gdev by hendriyawan(mr_silent)
# under license by Hendriyawan
# slow_print ( imam basyari )
# This program free software software, you can redistribute it and/or modify with give credits
#------------------------------------------------
# FBUP v2.0
# what new feature in v2.0 ?
# - easy to use
# USAGE : python fbup.py <options>
# list of options
# --pto : post status text only
# --pnc : post photo to wall without caption
# --pwc : post photo to wall with caption

# contact me :
# facebook : www.facebook.com/hendri.glanex
# email : hendrijs44@gmail.com
# github : https://github.com/mrSilent0598

# you can give me donation for support me :
# phone : +6289512786416

from core import updater
from core import console
from core import token
import sys
con = console.pyConsole()
fbup = updater.FacebookUP('FBUP v2.0')
token = token.Token()

#helps
def helps():
	print('\n\t|+|====== '+con.Y+'FACEBOOK BUP'+con.D+con.C+' v2.0'+con.D+' =====|+|\n')
	print('Before use this tool, please follow the explaination in bellow !')
	print con.Num(str(1), 'you must have access token for use it, you can visit')
	print('    link bellow to create access token\n')
	print('    *) https://developers.facebook.com/tools/explorer')
	print('    *) http://gdevnet.blogspot.co.id/2017/07/cara-mendapatkan-akses-token-facebook.html?m=1\n')
	print con.Num(str(2), 'and then copy & put your access token with filename.txt')
	print('    and save it in token directory')
	print con.Num(str(3), 'usage : python fbup.py <options>')
	print con.Num(str(4), 'list of options :\n')
	print('    --pto :  update status only text message')
	print('    --pnc : upload photo without caption')
	print('    --pwc : upload photo with caption')
	print('    --help : for helps\n')
	print con.Num(str(5), 'contact me :\n')
	print('    email    : hendrijs44@gmail.com')
	print('    facebook : www.fb.com/hendri.glanex')
	print('    blog     : https://gdevnet.blogspot.com')
	print('    github   : https://github.com/mrSilent0598\n')

#post to wall text only
def post_textOnly():
	console.set_windowTitle('FBUP v2.0/STATUS')
	console.Banner()
	token.find_token('token/')
	
	token_selected = raw_input(con.Proc('select your token : '))
	message = raw_input(con.Proc('enter message : '))
	fbup.post_toWall(message, token.get_token(token_selected))
	
#post photo to wall without caption
def post_photoOnly():
	console.set_windowTitle('FBUP v2.0/UPLOAD PHOTO')
	console.Banner()
	token.find_token('token/')
	token_selected = raw_input(con.Proc('select your token : '))
	image = raw_input(con.Proc('enter image file : '))
	fbup.post_photoNoCaption(image, token.get_token(token_selected))
	
#post photo to wall with caption
def post_photoWithCaption():
	console.set_windowTitle('FBUP v2.0/UPLOAD PHOTO WITH CAPTION')
	console.Banner()
	token.find_token('token/')
	token_selected = raw_input(con.Proc('select your token : '))
	image = raw_input(con.Proc('enter image file : '))
	caption = raw_input(con.Proc('enter caption : '))
	fbup.post_photoWithCaption(image, caption, token.get_token(token_selected))
	
# menu mode
def menu_mode():
	console.set_windowTitle('FBUP v2.0')
	print '\n\t'+con.Num(str(1), 'post status text only')
	print '\t'+con.Num(str(2), 'post photo without caption')
	print '\t'+con.Num(str(3), 'post photo with caption\n')
	select_menu = raw_input(con.Proc('select menu : '))
	if not select_menu:
		print con.Err('no menu selected !\n')
		sys.exit(1)
	else:
		try:
			if int(select_menu) == 1:
				post_textOnly()
			elif int(select_menu) == 2:
				post_photoOnly()
			elif int(select_menu) == 3:
				post_photoWithCaption()
			else:
				print con.Err('you must select 1-3 !\n')
				sys.exit(1)
		except Exception, e:
			print con.Err(str(e))
			print con.Err('failed !\n')
			sys.exit(1)

#main
def main(argv):
	if (len(sys.argv) != 2):
		helps()
		sys.exit(1)
	
	options = str(sys.argv[1])
	if options == '-pto' or options == '--pto':
		post_textOnly()
	if options == '-pnc' or options == '--pnc':
		post_photoOnly()
	if options == '-pwc' or options == '--pwc':
		post_photoWithCaption()
	if options == '-menu' or options == '--menu':
		menu_mode()
	if options == '-help' or options == '--help':
		helps()
		
	if not options in ['-pto', '--pto', '-pnc', '--pnc', '-pwc', '--pwc','-menu', '--menu','-help', '--help']:
		helps()
		sys.exit(1)
		
if __name__ == '__main__':
	main(sys.argv[1:])
	