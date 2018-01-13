##################
# Created by Ben #
##################
# The idea of this script is to create a psuedo human mouse.
# This script will use random numbers and math to create a seemingly
# human mouse movement using pyautogui library

import pyautogui
import math
import random

import logging

logging.basicConfig(format='%(levelname)s:%(message)s', filename="dump.txt", level=logging.DEBUG)

def init():
    pyautogui.PAUSE=1 #set 1 second pause after each call.
    size = pyautogui.size()
    pyautogui.FAILSAFE = True
    print("monitor size: " + str(size))

def getPosition():
    pos = pyautogui.position()
    log(pos)
    return pos
    
def gotoMiddle():
    width, height = pyautogui.size()
    centerX = width/2
    centerY = height/2
    pyautogui.moveTo(centerX,centerY,3)
    
def moveToPoint(method=0):
    log("func: moveToPoint()")
    startx, starty = pyautogui.position()
    #find x2 and y2 - using center for now
    width, height = pyautogui.size()
    endx = width/2
    endy = height/2
    log("end point: (%s, %s)" %(endx, endy))
    if method == 0:
        #go straight to position
        #distance formula to get distance from cursor position
        total_dist = distFormula(startx, starty, endx, endy)
        log("distance: %s" % total_dist)
        
        #randomize time divider for varying movements.
        t_divider = timeDiv()
        
        total_time = total_dist / t_divider
        log("calculated time: %s seconds" %total_time)
        
        pyautogui.moveTo(endx,endy,total_time, pyautogui.easeOutQuad)
    elif method == 1:
        #use random datapoints between (startx, starty) to (endx, endy)
        curx = startx
        cury = starty 
        tarx = endx
        tary = endy
        while curx != endx or cury != endy: #while not at destination
            tarx = pickRandPositive(curx, endx) #pick random x in between
            tary = pickRandPositive(cury, endy) #pick random y in between
            log("rand point: (%s, %s)" %(tarx, tary))
            
            dist = distFormula(curx, cury, tarx, tary)            
            t_divider = timeDiv()
        
            time = dist / t_divider
            log("calculated time: %s seconds" %time)
            
            # case so it never takes a long time (adds rounding of 2.5%)
            if startx <= endx and abs(tarx) >= abs(endx) * 0.975: tarx = endx
            if starty <= endy and abs(tary) >= abs(endy) * 0.975: tary = endy
            if startx >= endx and abs(tarx) <= abs(endx) * 1.025: tarx = endx
            if starty >= endy and abs(tary) <= abs(endy) * 1.025: tary = endy
            
            log("moving to: (%s,%s)"% (tarx, tary))
            pyautogui.moveTo(tarx, tary, time)
            #update current position
            curx = tarx
            cury = tary
    elif method == 2:
        #use threshold and choose points along slope with error = threshold
        threshold = 10 #random within 10 pixels of direct slope
        curx = startx
        cury = starty 
        tarx = endx
        tary = endy        
        num_pts = pickRandPositive(3,12) #pick random number of pts
        print ("num_pts: %s" % num_pts)
        x_incr = (endx - startx) / num_pts #calculate increment value
        y_incr = (endy - starty) / num_pts
        counter = 0
        while counter < num_pts:
            tarx = curx + x_incr           
            tary = cury + y_incr
            log("current point: (%s, %s)" % (curx, cury))
            
            if counter + 1 is not num_pts: 
                # if not last iteration, find a target pt randomly
                log("target point: (%s, %s)" % (tarx, tary))
                randx = random.randrange(-threshold,threshold)
                randy = random.randrange(-threshold,threshold)
                                
                log("randx: %s" % randx)
                log("randy: %s" % randy)
                
                tarx = tarx + randx
                tary = tary + randy
            else:
                # last iteration, move to end pt
                tarx = endx
                tary = endy
                
            dist = distFormula(curx, cury, tarx, tary)
            t_divider = timeDiv()
        
            time = dist / t_divider
            log("calculated time: %s seconds" %time)
            pyautogui.moveTo(tarx, tary, time)
            
            #finished moving
            curx = tarx
            cury = tary
            counter += 1
        log("final pt: (%s, %s)" % (curx, cury))
        

def pickRandPositive(val1, val2):
    val1 = abs(val1)
    val2 = abs(val2)
    if val1 == val2:
        return val2
    elif(val1 < val2):
        return random.randrange(val1, val2)
    elif(val1 > val2):
        return random.randrange(val2, val1)

def distFormula(x1, y1, x2, y2):
    val = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return val

def timeDiv():
    val = random.randrange(800, 1500) #change this for different rand times
    #print("random time divider: %s" %val)
    return  val

def log(msg="default message",console=1,file=1):
    if console == 1: print(msg)
    if file == 1: logging.debug(msg)