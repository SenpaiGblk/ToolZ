#!/usr/bin/env python2

#...................#

import os
import sys
import time
import threading
from getpass import getpass
import git
from time import sleep

#...................#

toolzlogo = '\33[91m' + '''

    _______             __ _______
   |       .-----.-----|  |   _   |
   |.|   | |  _  |  _  |  |___|   |
   `-|.  |-|_____|_____|__|/  ___/
     |:  |  \33[97m\33[41mTermux Toolz\33[0m\33[92m\33[91m  |:  1___
\33[97m     |::.|                |::.. . |
     `---'                `-------'
''' '\33[0m'

toolslogo = '\33[91m' + '''

    _______             __ _______
   |       .-----.-----|  |   _   |
   |.|   | |  _  |  _  |  |   1___|
   `-|.  |-|_____|_____|__|____   |
     |:  |                |:  1   |
\33[97m     |::.|                |::.. . |
     `---'                `-------'
''' '\33[0m'

zshlogo = '\33[91m' + '''

    _______ _______ ___ ___
   |   _   |   _   |   Y   |
   |___|   |   1___|.  1   |
    /  ___/|____   |.  _   |
   |:  1  \|:  1   |:  |   |
\33[97m   |::.. . |::.. . |::.|:. |
   `-------`-------`--- ---'
''' '\33[0m'

promptlogo = '\33[91m' + '''

    _______                           __
   |   _   .----.-----.--------.-----|  |_
   |.  1   |   _|  _  |        |  _  |   _|
   |.  ____|__| |_____|__|__|__|   __|____|
   |:  |                       |__|
\33[97m   |::.|
   `---'
''' '\33[0m'

applogo = '\33[91m' + '''

    _______             __ __            __   __
   |   _   .-----.-----|  |__.----.---.-|  |_|__.-----.-----.
   |.  1   |  _  |  _  |  |  |  __|  _  |   _|  |  _  |     |
   |.  _   |   __|   __|__|__|____|___._|____|__|_____|__|__|
   |:  |   |__|  |__|
\33[97m   |::.|:. |
   `--- ---'
''' '\33[0m'

installlogo = '\33[91m' + '''


    ___             __         __ __                 __
   |   .-----.-----|  |_.---.-|  |  |   .-----.-----|  |--.
   |.  |     |__ --|   _|  _  |  |  |   |-- __|__ --|     |
   |.  |__|__|_____|____|___._|__|__|   |_____|_____|__|__|
   |:  |
\33[97m   |::.|
   `---'
''' '\33[0m'

keyshortcutlogo = '\33[91m' + '''

    ___ ___                       __               __              __
   |   Y   .-----.--.--.   .-----|  |--.-----.----|  |_.----.--.--|  |_
   |.  1  /|  -__|  |  |   |__ --|     |  _  |   _|   _|  __|  |  |   _|
   |.  _  \|_____|___  |   |_____|__|__|_____|__| |____|____|_____|____|
   |:  |   \     |_____|
\33[97m   |::.| .  )
   `--- ---'
''' '\33[0m'

backtomenulogo = '\33[1m' +  '''

   \33[91m(\33[97mB\33[91m)\33[97m Back to menu
   \33[91m(\33[97mE\33[91m)\33[97m for \33[41mexit\33[0m

'''

bbacktomenulogo = '\33[1m' +  '''

   \33[91m(\33[97mZ\33[91m)\33[97m Edit zsh
   \33[91m(\33[97mB\33[91m)\33[97m Back to menu
   \33[91m(\33[97m0\33[91m)\33[97m for \33[41mexit\33[0m

'''

#...................#

prompt = '\33[1m' + 'TZ'  '\33[93m' + '> '  '\33[0m'

done = '\x1b[3;37;4m' + 'The installation is complete...' + '\033[0m'

wronginput = '\n\007\033[01;31mSorry \033[01;37m: \033[01;37mInvalid input !!\033[00m'

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

#...................#

class backto3:
    def __init__(self):
        print(bbacktomenulogo)
        bck3 = raw_input(prompt)
	if bck3 == "Z":
		os.system('nano /data/data/com.termux/files/home/.zshrc')
        elif bck3 == "B":
                tools()
        elif bck3 == "E":
                os.system('clear')
                sys.exit()
        else:
            print(wronginput)
            sleep(1)
            backto()

class backto:
    def __init__(self):
	os.system('clear')
	print(done)
	print(backtomenulogo)
	bck = raw_input(prompt)
	if bck == "B":
		tools()
	elif bck == "E":
		os.system('clear')
		sys.exit()
	else:
	    print(wronginput)
	    sleep(1)
	    backto()

class backto2:
    def __init__(self):
        os.system('clear')
        print(done)
        print(backtomenulogo)
        bck1 = raw_input(prompt)
        if bck1 == "B":
                toolz()
        elif bck1 == "0":
		os.system('clear')
                sys.exit()
        else:
            print(wronginput)
            sleep(1)
            backto()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(9.0 / 100)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.99 / 100)

#...................#

class toolz:
    def __init__(self):
	os.system('clear')
	print(toolzlogo)
	print('\33[1m' + '''   \33[91m[ \33[97m1 \33[91m]\33[97m Show tools
   \33[91m[ \33[97m2 \33[91m]\33[97m Show zsh
   \33[91m[ \33[97m3 \33[91m]\33[97m Show app
   \33[91m[ \33[97m4 \33[91m]\33[97m Termux keys shortcut
   
    \33[91m(\33[97mE\33[91m)\33[97m for \33[41mexit\33[0m
	''')
	choice1 = raw_input(prompt)

	if choice1 == "1":
		tools()
	elif choice1 == "2":
		zsh()
	elif choice1 == "3":
		app()
	elif choice1 == "4":
		keyshortcut()
	elif choice1 == "E":
		sys.exit()
        else:
            print(wronginput)
	    sleep(1)
	    toolz()

class tools:
    def __init__(self):
	os.system('clear')
	print(toolslogo)
	print('\33[1m' + '''   \33[91m[ \33[97m1 \33[91m]\33[93m Install>\33[97m sqlmap
   \33[91m[ \33[97m2 \33[91m]\33[93m Install>\33[97m hiddeneye
   \33[91m[ \33[97m3 \33[91m]\33[93m Install>\33[97m hammer
   \33[91m[ \33[97m4 \33[91m]\33[93m Install>\33[97m webdav

    \33[91m(\33[97m0\33[91m)\33[97m Back to menu
	''')
	choice2 = raw_input(prompt)

	if choice2 == "1":
		sqlmap()
	elif choice2 == "2":
		hiddeneye()
	elif choice2 == "3":
		hammer()
	elif choice2 == "4":
		webdav()
	elif choice2 == "0":
		toolz()
	else:
            print(wronginput)
	    sleep(1)
	    tools()

class zsh:
    def __init__(self):
	os.system('clear')
	print(zshlogo)
	print('\33[1m' + '''   \33[91m[ \33[97m1 \33[91m]\33[97m\33[97m Install zsh prompt
   \33[91m[ \33[97m2 \33[91m]\33[97m\33[97m Install zsh

    \33[91m(\33[97m0\33[91m)\33[97m Back to menu
	''')
	choice3 = raw_input(prompt)

	if choice3 == "1":
		zshprompt()
	elif choice3 == "2":
		installzsh()
	elif choice3 == "0":
		toolz()
	else:
	    print(wronginput)
	    sleep(1)
	    zsh()

class zshprompt:
    def __init__(self):
	os.system('clear')
	print(promptlogo)
	print('\33[1m' + '''   \33[91m[ \33[97m1 \33[91m]\33[93m Install>\33[97m Powerlevel10k

   \33[91m(\33[97m0\33[91m)\33[97m Back to main menu
   \33[91m(\33[97m00\33[91m)\33[97m Back to menu zsh
	''')
	choice4 = raw_input(prompt)

	if choice4 == "1":
		powerlevel10k()
	elif choice4 == "0":
                toolz()
	elif choice4 == "00":
                zsh()
	else:
            print(wronginput)
	    sleep(1)
	    zshprompt()

class installzsh:
    def __init__(self):
	os.system('clear')
	print(installlogo)
	print('Y: continue install zsh B: back to zsh menu')
	yn = raw_input('Do you want to continue install zsh? [Y/b]: ')

	if yn == 'y' or yn == 'Y':
		os.system('pkg update && pkg upgrade -y')
	        os.system('pkg install nano -y')
	        os.system('pkg install curl -y')
		os.system('')
	        os.system('sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"')
		os.system('clear')
		os.system('rm -rf /data/data/com.termux/files/home/termux-ohmyzsh')
		slowprint('Trying to exit')
		sleep(4)
		os.system('killall -9 com.termux')
	elif yn == 'b' or yn == 'B':
	        zsh()
	else:
	    print(wronginput)
	    sleep(1)
	    installzsh()

class app:
    def __init__(self):
	os.system('clear')
	print(applogo)
	print('\33[1m' + '''   \33[91m(\33[97m1\33[91m)\33[97m Screen Recorder
   \33[91m(\33[97m2\33[91m)\33[97m Minecraft PE
   \33[91m(\33[97m0\33[91m)\33[97m Soon

    \33[91m(\33[97m0\33[91m)\33[97m Back to menu
	''')
	choice5 = raw_input(prompt)

	if choice5 == "1":
		screenrecorder()
	elif choice5 == "2":
		minecraftpe()
	elif choice5 == "0":
		toolz()
	else:
            print(wronginput)
	    sleep(1)
	    app()

class screenrecorder:
    def __init__(self):
	os.system('clear')
	print(recorderlogo)

class keyshortcut:
    def __init__(self):
	os.system('clear')
	print(keyshortcutlogo)
	yn2 = raw_input('Do you want to continue install termux key shortcut? [Y/b]: ')
        if yn2 == 'y' or yn2 == 'Y':
		os.system('clear')
		print(a+'\t  Shorcut for help you')
		print(b+'\t Karjok Pangesty')
		print('\t https://t.me/CRABS_ID')
		print(a+'+'*40)
		print('\nProses..')
		sleep(1)
		print(b+'\n[!] making termux properties directory..')
		sleep(1)
		try:
		      os.mkdir('/data/data/com.termux/files/home/.termux')
		except:
		      pass
		print(a+'[!]Success !')
		sleep(1)
		print(b+'\n[!] Making setup file..')
		sleep(1)

		key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
		kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
		kontol.write(key)
		kontol.close()
		sleep(1)
		print(a+'[!] Success !')
		sleep(1)
		print(b+'\n[!] Setting up..')
		sleep(2)
		os.system('termux-reload-settings')
		print(a+'[!] Successfully !! ^^'+c+'\n\nhubungi https://t.me/om_karjok untuk requests\natau pertanyaan, atau hubungi https://t.me/CRABS_ID\nThanks :*\n\n')
		sleep(2)
                backto2()

#...................#

def powerlevel10k():
	os.system('clear')
        slowprint('\33[1m' + '\33[32m' + 'Installing Powerlevel10k...' '\33[0m')
	sleep(2)
	os.system('rm -rf ~/.oh-my-zsh/custom/themes/powerlevel10k')
	os.system('git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k')
        sleep(2)
	os.system('clear')
	print(done)
	print('prompt> ZSH_THEME="powerlevel10k/powerlevel10k"')
	backto3()
class update:
	os.system("git clone --depth=1 https://github.com/SenpaiGblk/ToolZ")

#...................#

def sqlmap():
	os.system('clear')
	slowprint('\33[1m' + '\33[32m' + 'Installing sqlmap...' '\33[0m')
	sleep(2)
	os.system('apt update && apt upgrade')
	print("Cloning into '/data/data/com.termux/files/home/sqlmap'...")
	sleep(1)
	os.system('rm -rf /data/data/com.termux/files/home/sqlmap')
	git.Git("/data/data/com.termux/files/home/").clone("https://github.com/sqlmapproject/sqlmap")
	sleep(2)
	backto()

def hiddeneye():
	os.system('clear')
	slowprint('\33[1m' + '\33[32m' + 'Installing hiddeneye...' + '\33[0m')
	sleep(2)
	os.system('apt update && apt upgrade')
	os.system('pkg install git python php curl openssh grep')
	os.system('rm -rf /data/data/com.termux/files/home/HiddenEye')
	print("Cloning into '/data/data/com.termux/files/home/HiddenEye'...")
	sleep(1)
	os.system('cd /data/data/com.termux/files/home/ && git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git')
	os.system('cd /data/data/com.termux/files/home/HiddenEye pip install -r requirements.txt')
	sleep(2)
	backto()

def hammer():
	os.system('clear')
	slowprint('\33[1m' + '\33[32m' + 'Installing hammer...' + '\33[0m')
	sleep(2)
	os.system('apt update && apt upgrade')
	os.system('rm -rf /data/data/com.termux/files/home/hammer')
        print("Cloning into '/data/data/com.termux/files/home/hammer'...")
        sleep(1)
	git.Git('/data/data/com.termux/files/home/').clone('https://github.com/cyweb/hammer')
	sleep(2)
	backto()

def webdav():
	os.system('clear')
	slowprint('\33[1m' + '\33[32m' + 'Installing webdav...' + '\33[0m')
	sleep(2)
        os.system('apt update && apt upgrade')
        os.system('rm -rf /data/data/com.termux/files/home/webdav')
	print("Cloning into '/data/data/com.termux/files/home/webdav'...")
        sleep(1)
        git.Git('/data/data/com.termux/files/home/').clone('https://github.com/cyweb/hammer')
	sleep(2)
	backto()

#...................#

def durecorder():
	os.system('xdg-open http://www.mediafire.com/file/zb6qf60f2x5j607/Du_recorder_v1.15.1_latest/file')
	app()

#...................#




if __name__ == "__main__":
    try:
        toolz()
    except KeyboardInterrupt:
	os.system('clear')
        sleep(0.25)
