##################
# Created by Ben #
##################
# The idea of this script is to create a psuedo human mouse.
# This script will use random numbers and math to create a seemingly
# human mouse movement using pyautogui library

import pyautogui
import math
import random

def init():
    pyautogui.PAUSE=1 #set 1 second pause after each call.
    size = pyautogui.size()
    pyautogui.FAILSAFE = True
    print("monitor size: " + str(size))


def getPosition():
    pos = pyautogui.position()
    print(pos)
    return pos
    
def gotoMiddle():
    width, height = pyautogui.size()
    centerX = width/2
    centerY = height/2
    pyautogui.moveTo(centerX,centerY,3)
    
def moveToPoint(paranoid=0):
    startx, starty = pyautogui.position()
    #find x2 and y2 - using center for now
    width, height = pyautogui.size()
    endx = width/2
    endy = height/2
    print("end point: (%s, %s)" %(endx, endy))
    if paranoid == 0:
        #distance formula to get distance from cursor position
        #total_dist = math.sqrt((endx-startx)**2 + (endy-starty)**2)
        total_dist = distFormula(startx, starty, endx, endy)
        print("distance: %s" % total_dist)
        
        #randomize time divider for varying movements.
        t_divider = timeDiv()
        
        total_time = total_dist / t_divider
        print("calculated time: %s seconds" %total_time)
        
        pyautogui.moveTo(endx,endy,total_time, pyautogui.easeOutQuad)
    elif paranoid == 1:
        #use different datapoints along/near the path to (endx, endy)
        curx = startx
        cury = starty 
        tarx = endx
        tary = endy
        while curx != endx or cury != endy: #while not at destination
            tarx = pickRand(curx, endx) #pick random x in between
            tary = pickRand(cury, endy) #pick random y in between
            #dist = math.sqrt((tarx-curx)**2 + (tary-cury)**2)
            dist = distFormula(curx, cury, tarx, tary)
            print("rand point: (%s, %s)" %(tarx, tary))
            t_divider = timeDiv()
        
            time = dist / t_divider
            #print("calculated time: %s seconds" %time)
            
            # case so it never takes a long time (adds rounding)
            if startx <= endx and abs(tarx) >= abs(endx) * 0.975: tarx = endx
            if starty <= endy and abs(tary) >= abs(endy) * 0.975: tary = endy
            if startx >= endx and abs(tarx) <= abs(endx) * 1.025: tarx = endx
            if starty >= endy and abs(tary) <= abs(endy) * 1.025: tary = endy
            
            print("moving to: (%s,%s)"% (tarx, tary))
            pyautogui.moveTo(tarx, tary, time)
            #update current position
            curx = tarx
            cury = tary

def pickRand(val1, val2):
    val1 = abs(val1)
    val2 = abs(val2)
    if val1 == val2:
        return val2
    elif(val1 < val2):
        return random.randrange(val1,val2)
    elif(val1 > val2):
        return random.randrange(val2, val1)

def distFormula(x1, y1, x2, y2):
    val = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return val

def timeDiv():
    val = random.randrange(800,1500) #change this for different rand times
    #print("random time divider: %s" %val)
    return  val
    
def openCalculator():
    pyautogui.press('win')
    pyautogui.typewrite('calculator')
    pyautogui.press('enter')