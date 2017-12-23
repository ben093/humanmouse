##################
# Created by Ben #
##################
# The idea of this script is to create a psuedo human mouse.
# This script will use random numbers and math to create a seemingly
# human mouse movement using pyautogui library

import pyautogui
import math

def init():
	pyautogui.PAUSE=1 #set 2.5 second pause after each call.
	size = pyautogui.size()
	pyautogui.FAILSAFE = True
	print("test")


def getPosition():
	pos = pyautogui.position()
	print(pos)
	return pos
	
def gotoMiddle():
	width, height = pyautogui.size()
	centerX = width/2
	centerY = height/2
	pyautogui.moveTo(centerX,centerY,3)
	
def moveToPoint():
	x1, y1 = pyautogui.position()
	#find x2 and y2 - using center for now
	width, height = pyautogui.size()
	x2 = width/2
	y2 = height/2
	
	dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	
	
	
def openCalculator():
	pyautogui.press('win')
	pyautogui.typewrite('calculator')
	pyautogui.press('enter')