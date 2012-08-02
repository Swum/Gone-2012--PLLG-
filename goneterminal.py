########################
# -*- coding: utf-8 -*	 #
# Gone 2012              #
# Submitted for the PLLG #
########################

# imports #
import time
import sys

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
        help()
    elif pc1=='start':
        beginning()
    elif pc1=='credits' or pc1=='credit':
        credits()
    elif pc1=='quit':
        sys.exit('Thanks for playing!')
    else:
        print('')
        print('Command is Invalid')
        promptLoad()
def promptCredits():
    cc1=input('').lower()
    if cc1=='q':
        start()
    else:
        print('')
        print('Command is Invalid')
        promptCredits()

def help():
    print(' ------ ')
    print('l Help l')
    print(' ------ ')
    print(' ---------- ')
    print('l Movement l')
    print(' ---------- ')
    print(' N - north, S - south, E - east, W - west')
    print(' Interact <object> - interacts with an object, not all objects can be used.')
    print('')

def beginning():
    print('In the beginning, there was life.')

def credits():
	print('')
	print(' -----------------------------------------------')
	print('l  .oooooo.                                     l ')
	print('l d8P\'  `Y8b                                    l ')
	print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
	print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
	print('l888     ooooo 888   888  888   888  888ooo888  l ')
	print('l`88.    .88\'  888   888  888   888  888    .o  l ')
	print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
	print('l					        l ')
	print(' ----------------------------------------------- ')
	print(' ----------------------------    ')
	print('l         Credits            l   ')
	print(' ----------------------------    ')
	print(' ------------------------------')
	print('l   Gone 2012                   l ')
	print('l Made by                       l ')
	print('l Sasandy3189 (Designer)        l ')  
	print('l Swum (Coder)                  l ')
	print('l Deadifyed (StoryWriter)       l ')
	print(' ------------------------------  ')
	print(' -------------------  ')
	print('l Type Q to go back l ')
	print(' -------------------  ')
	promptCredits()
    
def start():
    print(' -----------------------------------------------')
    print('l  .oooooo.                                     l ')
    print('l d8P\'  `Y8b                                    l ')
    print('l888            .ooooo.  ooo. .oo.    .ooooo.   l ')
    print('l888           d88\' `88b `888P\"Y88b  d88\' `88b  l ')
    print('l888     ooooo 888   888  888   888  888ooo888  l ')
    print('l`88.    .88\'  888   888  888   888  888    .o  l ')
    print('l `Y8bood8P\'   `Y8bod8P\' o888o o888o `Y8bod8P\'  l ')
    print('l					        l ')
    print(' ----------------------------------------------- ')	
    print(' --------------------------  ')
    print('l Type \'Start\' to Start! l ')
    print(' --------------------------  ')
    print(' ---------------------------------  ')
    print('l Type \'Help\' for Some Commands l ')
    print(' --------------------------------- ')
    print(' ---------------------------------------  ')
    print('l Type \'Credits\' to See Who Made This l ')
    print(' --------------------------------------- ')
    print(' -----------------------  ')
    print('l Type \'Quit\' to Exit l ')
    print(' ----------------------- ')
    promptLoad()

#OnLoad#
start()

