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
    elif pc1=='credits' or pc1=='credit':
        os.system('cls' if os.name=='nt' else 'clear')
        credits()
    elif pc1=='quit':
        sys.exit('Thanks for playing!')
<<<<<<< HEAD
    elif pc1=='mp' or 'multiplayer':
=======
    elif pc1=='mp' or pc1=='multiplayer':
>>>>>>> Multiplayer menu in.
        os.system('cls' if os.name=='nt' else 'clear')
        multiplayer()
    else:
        print('')
        print('Command is Invalid')
        time.sleep(0.2)
        promptLoad()
def promptCredits():
    cc1=input('').lower()
    if cc1=='q':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    else:
        print('')
        print('Command is Invalid')
        time.sleep(0.2)
        promptCredits()

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
    time.sleep(1)

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
	print('l Type Q to go back l ')
	print(' -------------------  ')
	promptCredits()

def multiplayer():
    players=['player1','player2']
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
    print('         --------------------------  ')
    print('      Type \'PlayMp\' to challenge someone!  ')
    print('         --------------------------  ')
    print('      ---------------------------------- ')
    print('       Currently the players online are:  ')
    print('      ----------------------------------')
    print('      ---------------------------------- ')
    print('       Currently the players online are:  ')
    print(players)
    print('      ----------------------------------')
    print('          -----------------------  ')
    print('          Type \'Back\' to go back  ')
    print('          ----------------------- ')
    print('')
    promptLoad()

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
<<<<<<< HEAD
=======

def multiplayer():
    players=['player1','player2']
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
    print('l Type \'Play\' to challenge someone!   l ')
    print(' ---------------------------------------  ')
    print(' ------------------------------------------------------------ ')
    print('l Currently the players online are: ' + str(players) + '     l') 
    print(' ------------------------------------------------------------')
    print(' --------------------------  ')
    print('l Type \'Q\' to go back    l  ')
    print(' -------------------------- ')
    print('')
    promptMultiplayer()

def promptMultiplayer():
    pc3=input().lower()
    if pc3=='q':
        os.system('cls' if os.name=='nt' else 'clear')
        start()
    if pc3=='play':
        print('Comming soon!')
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        start()

>>>>>>> Multiplayer menu in.
#OnLoad#
print('### WARNING! ###')
print('This program must be run in cmd (Windows) or Terminal (Mac/Linux)!')
print('Are you running in the console? Yes or No')
TomMadeMeDoThis=input().lower()
if TomMadeMeDoThis =='no' or TomMadeMeDoThis=='n':
    print('Try again using the console.')
    sys.exit()
elif TomMadeMeDoThis=='yes' or TomMadeMeDoThis=='y':
    print('Sorry for the inconvenience.')
    os.system('cls' if os.name=='nt' else 'clear')
    start()
elif TomMadeMeDoThis=='sausage' or TomMadeMeDoThis=='Sausage':
    print('Sausage = <3')
    start()
else:
    #Dafuq are you saying?
    print('Please enter Yes or No')

