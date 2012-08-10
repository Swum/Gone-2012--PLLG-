########################
# -*- coding: utf-8 -*	 #
# Gone 2012              #
# Submitted for the PLLG #
########################

# imports #
import time
import sys
import os

# cleanup and set size of window
os.system('cls' if os.name=='nt' else 'clear')
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=125))
# key for variables #
#   pc1 : Pre-Choice 1, l:38
#   pc2 : Pre-Choice 2
#   cc1 : Credit Choice 1, l:82
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# functions #
def promptLoad():
    pc1=''
    pc1=input().lower()
    if pc1=='help':
        help(0)
    elif pc1=='start':
        os.system('cls' if os.name=='nt' else 'clear')
        beginning()
    elif pc1=='back':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    elif pc1=='credits' or pc1=='credit':
        os.system('cls' if os.name=='nt' else 'clear')
        credits()
    elif pc1=='quit':
        sys.exit('Thanks for playing!')
    elif pc1=='mp' or pc1=='multiplayer':
        os.system('cls' if os.name=='nt' else 'clear')
        multiplayer()
    else:
        print('')
        print('Command is Invalid')
        time.sleep(0.2)
        promptLoad()
def promptCredits():
    cc1=input('').lower()
    if cc1=='quit':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    else:
        print('')
        print('Command is Invalid')
        time.sleep(0.2)
        promptCredits()

def promptLoadSave():
    cc1=input('').lower()
    if cc1=='q':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    else:
        print('')
        print('Command is Invalid')
        time.sleep(0.2)
        promptLoadSave()

def promptMultiPlayer():
    cc1=input('').lower()
    if cc1=='q':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    elif cc1=='c':
        os.system('cls' if os.name=='nt' else 'clear')
        mpbattle()
        else:
        print('')
        print('Command is Invalid')
        time.sleep(0.2)
        promptLoadSave()


def help(x):
    os.system('cls' if os.name=='nt' else 'clear')
    print(' ------ ')
    print('l Help l')
    print(' ------ ')
    print(' ---------- ')
    print('l Movement l')
    print(' ---------- ')
    print(' N - north, S - south, E - east, W - west')
    print(' Interact <object> - interacts with an object, not all objects can be used.')
    print('') 
    print(' ---------- ')
    print('l Commands l')
    print(' ---------- ')
    print(' Quit - Exits the program.')
    print('### Type Q to Go Back ###')
    helpGoBack=input('').lower()
    if helpGoBack==('q'):
        if x==0:
            os.system('cls' if os.name=='nt' else 'clear')
            start()
        elif x==1:
            print('Aww yeah')


def beginning():
    print('In the beginning, there was life...')
    print('Loading.')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print('In the beginning, there was life...')
    print('Loading..')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print('In the beginning, there was life...')
    print('Loading...')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    game()

def credits():
	print('')
	print(' -----------------------------------------------')
	print('l  .oooooo.                                     l ')
	print('l d8P\'  `Y8b                                    l ')
	print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
	print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
	print('l888     ooooo 888   888  888   888  888ooo888  l ')
	print('l`88.    .88\'  888   888  888   888  888    .o  l ')
	print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
	print('l					        l ')
	print(' ----------------------------------------------- ')
	print(' ----------------------------    ')
	print('l         Credits            l   ')
	print(' ----------------------------    ')
	print(' ------------------------------')
	print('l   Gone 2012                   l ')
	print('l Made by                       l ')
	print('l Sasandy3189 (Designer,Coder)  l ')  
	print('l Swum (Designer.Coder)         l ')
	print('l Deadifyed (StoryWriter)       l ')
	print('l Jonathan  (StoryWriter,Coder) l ')
	print(' ------------------------------  ')
	print(' -------------------  ')
	print('l Type \'Quit\' to go back l ')
	print(' -------------------  ')
	promptCredits()

def start():
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    promptLoad()

def mpbattle():
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('l Pick a slot to save/load by typing 1-3  l ')
    print(' ---------------------------------------  ')
    print(' ------------------------------------------------------------ ')
    print('l Save Slot 1 Empty     l') 
    print(' ------------------------------------------------------------')
    print(' ------------------------------------------------------------ ')
    print('l Save Slot 2 Empty     l') 
    print(' ------------------------------------------------------------')
    print(' ------------------------------------------------------------ ')
    print('l Save Slot 3 Empty     l') 
    print(' ------------------------------------------------------------')
    print(' --------------------------  ')
    print('l Type \'Q\' to go back    l  ')
    print(' -------------------------- ')
    print('')
    promptLoadSave()

def multiplayer():
    players=['player1','player2']
    playernumber=15
    playernumber = str(playernumber)
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('l Welcome to the lobby, Press C to battle  l ')
    print('l a random player on the server, and win!*  l ')
    print('l *possibly                                   ')
    print(' ---------------------------------------  ')
    print(' ---------------------------------------  ')
    print('l Currently '+playernumber+' people are Online l ')
    print(' ---------------------------------------  ')
    print(' --------------------------  ')
    print('l Type \'Q\' to go back    l  ')
    print(' -------------------------- ')
    print('')
    promptMultiPlayer()

atty = sys.stdout.isatty()

if atty == False:
    print('This program must be run in cmd (Windows) or Terminal (Mac/Linux)!')
    time.sleep(1.5)
    sys.exit()    
else:
    start()
    
def boot():
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting.   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print(' 888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting..   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting...   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting.   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting..   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting...   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting.   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting..   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' ---------------------------------------  ')
    print('                 Booting...   ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(0.5)
    os.system('cls' if os.name=='nt' else 'clear')
