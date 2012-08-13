########################
# -*- coding: utf-8 -*	 #
# Gone 2012              #
# Submitted for the PLLG #
########################

# imports #
import time
import sys
import os
import socket

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
        mpbattle()
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

def promptLoadGame():
    cc1=input('').lower()
    if cc1=='q':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    elif cc1=='start':
        os.system('cls' if os.name=='nt' else 'clear')
        cutscene1()
        promptLoadGame()

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
    print(' --------------------------  ')
    print('l Type \'Start\' to Start! l ')
    print(' --------------------------  ')
    print(' ---------------------------------- ')
    print('l Type \'MP\' to start Multiplayer l ')
    print(' ----------------------------------')
    print(' ---------------------------------  ')
    print('l Type \'Help\' for Some Commands l ')
    print(' --------------------------------- ')
    print(' ---------------------------------------  ')
    print('l Type \'Credits\' to See Who Made This l ')
    print(' --------------------------------------- ')
    print(' -----------------------  ')
    print('l Type \'Quit\' to Exit l ')
    print(' ----------------------- ')
    print('')
    promptLoad()

def mpbattle():
    player1='Gold'
    player1 = str(player1)
    player2='Swum'
    player2 = str(player2)
    health='95'
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
    print('     ( )                           ( )           ')
    print('    --|--                         --|--          ') 
    print('     / \                           / \           ')
    print(' ----------------------------------------------- ')
    print('        Punch with P Kick with K Stab with S     ')
    print('       Once you have hit 3 times, you can use    ')
    print('                 a melee attack once             ')
    print(' ----------------------------------------------- ')
    print('                    HP:'+health+'                ')
    print(' ----------------------------------------------- ')
    print('  Player 1 name: '+player1+' Player 2 name: '+player2+'  ')
    print(' ----------------------------------------------- ')
    print('          Press Q to quit the Game               ')
    print(' ----------------------------------------------- ')
    pc1 = input('').lower()
    if pc1=='q':
       os.system('cls' if os.name=='nt' else 'clear')
       start()
    elif pc1=='p':
       os.system('cls' if os.name=='nt' else 'clear')
       start()
    elif pc1=='p':
       os.system('cls' if os.name=='nt' else 'clear')
       start()
               
def game():
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
    print('l Type Start to begin your adventure!   l ')
    print(' ---------------------------------------  ')
    print(' --------------------------  ')
    print('l Type \'Q\' to go back    l  ')
    print(' -------------------------- ')
    print('')
    promptLoadGame()


def cutscene1():
    print(' -----------------------------------------------')
    print('       ()___                                    ')
    print('      ()//__/)_________________()               ')
    print('      |(___)//#/_/#/_/#/_/#()/||                ')
    print('      ||----|#| |#|_|#|_|#|_|| ||               ')
    print('      ||____|_|#|_|#|_|#|_|#||/||               ')
    print('      ||    |#|_|#|_|#|_|#|_||                  ')
    print('					                               ')
    print(' -----------------------------------------------')	
    print(' ---------------------------------------  ')
    print(' "What Happened? I dont remember! Oh well, lets ')
    print(' "    go and see what is happening outside"     ')
    print(' ---------------------------------------  ')
    print('')
    time.sleep(1)

def scene1():
    cc1=input('').lower()
    print(' -----------------------------------------------')
    print('       ()___                                    ')
    print('      ()//__/)_________________()               ')
    print('      |(___)//#/_/#/_/#/_/#()/||                ')
    print('      ||----|#| |#|_|#|_|#|_|| ||               ')
    print('      ||____|_|#|_|#|_|#|_|#||/||               ')
    print('      ||    |#|_|#|_|#|_|#|_||                  ')
    print('					                               ')
    print(' -----------------------------------------------')	
    print(' ---------------------------------------  ')
    print(' You are in a room, there are 2 doors, a locked ')
    print(' one, and an open one, there is some food and a ')
    print('              knife to attack with              ')
    print('            Type B to pick up the knife         ')
    print(' ---------------------------------------  ')
    print('')
    if cc1=='b':
        os.system('cls' if os.name=='nt' else 'clear')
    print(' -----------------------------------------------')
    print('       ()___                                    ')
    print('      ()//__/)_________________()               ')
    print('      |(___)//#/_/#/_/#/_/#()/||                ')
    print('      ||----|#| |#|_|#|_|#|_|| ||               ')
    print('      ||____|_|#|_|#|_|#|_|#||/||               ')
    print('      ||    |#|_|#|_|#|_|#|_||                  ')
    print('					                               ')
    print(' -----------------------------------------------')	
    print(' ---------------------------------------  ')
    print(' You are in a room, there are 2 doors, a locked ')
    print('              one, and an open one              ')
    print('              Type A to open the door')
    print(' ---------------------------------------        ')
    print('')
     elif cc1=='a':
     os.system('cls' if os.name=='nt' else 'clear')
     cutscene2()
    

def multiplayer():
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
    print('l Welcome to the lobby, plz type in  l ')
    print('l your servers ip address to battle  l ')
    print(' ---------------------------------------  ')
    print('')
    mpip = input('').lower()
    if mpip=='q':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    else:
        os.system('cls' if os.name=='nt' else 'clear')
    clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsock.connect((mpip,20000))
    clientsock.recv([1024])
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
    print('     ---------------------------------------  ')
    print('l                   Connecting...      ')
    print('     ---------------------------------------  ')
    print('')

atty = sys.stdout.isatty()

if atty == False:
    print('This program must be run in cmd (Windows) or Terminal (Mac/Linux)!')
    time.sleep(1.5)
    sys.exit()    
else:
    start()
