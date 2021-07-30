#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Joanne Stasiak
# N-Back Task adapted from Barch et al: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4011498/#R40

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys
from psychopy.hardware import keyboard
import numpy
from numpy import random
from psychopy.hardware import joystick
#from psychopy.hardware import joyButtons
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

expName = 'N-Back Localizer'
expInfo = {'Participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',extraInfo=expInfo,originPath='C:\\Users\\joann\\Downloads\\Self-Regulation-Psychopy-Files-master\\Self-Regulation-Psychopy-Files-master\\Slot MachineTask\\SlotMachTest.py',
    savePickle=True, saveWideText=True, dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
frameTolerance = 0.001

win = visual.Window( size=(1024, 768), fullscr=True, screen=0, winType='pyglet',monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

#Define variables
defaultKeyboard = keyboard.Keyboard()
globalClock = core.Clock()
routineTimer = core.CountdownTimer()
InstrClock = core.Clock()
instText = visual.TextStim(win=win, text='', height=0.06, pos=(0,0), font='Arial', wrapWidth=1.45, color='white')
space = keyboard.Keyboard()
picStim = visual.ImageStim(win=win, image=None, pos=(0,0), size=(0.6,0.6))
choiceKeys = keyboard.Keyboard()
choiceClock = core.Clock()
targetClock = core.Clock()
isi = visual.TextStim(win=win, text='+', height=0.13, pos=(0,0), color='white')
cue = visual.TextStim(win=win, text='+', height=0.19, pos=(0,0), color='white')
targetText=visual.TextStim(win=win, text='Your target image is:', height=0.085, pos=(0, 0.4), color='white')
interRun=visual.TextStim(win=win, text='The run will begin momentarily...', height=0.08, pos=(0, 0), color='white')
# DEfine functions

def instFunc(textArg):
    continueRoutine = True
    instructionComponents= [instText, space] 
    for i in instructionComponents: 
        i.status = STARTED  
    while continueRoutine:
        instText.setText(textArg)
        instText.setAutoDraw(True)
        win.flip()
        if space.status == STARTED:
            theseKeys = space.getKeys(keyList=['1']) 
            if len(theseKeys):
                continueRoutine = False 
                instText.setAutoDraw(False)
                space.rt = theseKeys[-1].rt 
        if defaultKeyboard.getKeys(keyList=["escape"]): 
            core.quit()
    thisExp.addData("Instructions Text", instText.text) 
    thisExp.nextEntry() 

instTextArray = ['In this task, you will be seeing a series of pictures and making key responses. \n\nPress 1 to continue', 'Specifically, you will be making responses to indicate if a picture shown on screen is the same, or different, than a picture that was previously shown \n\nPress 1 to continue.',\
"In some blocks, your goal will be to identify if an image shown on screen is the same as a target image. In these blocks, you will be shown a target image and will be instructed to indicate if an image shown on screen is the SAME or DIFFERENT to the target image. \nTo indicate that the image is the same, \
press 1. To indicate that the image shown on screen is different, press 2. \n\nPress 1 to continue.", "In other blocks, your goal will be to identify if an image shown on screen is the same as the image that was presented 2 slides prior. \nTo indicate that the image is the same, as the one you saw 2 slides back, \
press 1. To indicate that the image shown on screen is different, press 2. \n\nPress 1 to continue.", "You will know which type of blocks you are working on based on a cue shown on screen. When you see the cue 'TARGET' you will be identifying if the image shown on screen is the same or different than a target \
image. When you see the cue '2-Back' you will be making responses to indicate if an image shown on screen is the same as the image that was presented 2 slides prior. \nPress 1 to continue." , "Again, for both of these blocks, you can press 1 if you think the image is the same, or 2 if you think the image is different. \
You will only have two seconds to respond once the image appears on screen. \n\n You will first be playing some practice rounds. To begin the practice, press 1!"]

def isiFunc(time): 
    continueRoutine = True
    isi.status = STARTED 
    isi.setAutoDraw(True)
    win.flip()
    core.wait(time)
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    isi.setAutoDraw(False)
    isi.status = FINISHED 
    thisExp.addData("ISI Time", time) 
    thisExp.nextEntry()

def choiceFunc(imageArray):
    for a in imageArray:
        continueRoutine = True
        choiceFuncComponents= [picStim, choiceKeys, choiceClock]
        choiceKeys.keys=[] 
        choiceKeyPress=[]
        choiceKeys.rt=[] 
        choiceClock.reset() 
        for i in choiceFuncComponents: 
            i.status = STARTED
        while choiceClock.getTime() < 2.0000: 
            picStim.setImage(a)
            picStim.setAutoDraw(True)
            theseKeys = choiceKeys.getKeys(keyList=['1', '2']) 
            choiceKeyPress.extend(theseKeys)
            if len(choiceKeyPress):
                choiceKeys.keys = choiceKeyPress[-1].name 
                choiceKeys.rt = choiceKeyPress[-1].rt 
            if continueRoutine: 
                win.flip()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        picStim.setAutoDraw(False)
        continueRoutine = False 
        thisExp.addData("Image Presented", a)
        if choiceKeys.keys == '1':
            thisExp.addData("Image Response", 'Same')
        if choiceKeys.keys == '2':
            thisExp.addData("Image Response", 'Different')
        thisExp.addData("Response RT", choiceKeys.rt) 
        thisExp.addData("Response Made", choiceKeys.keys) 
        isiFunc(0.500)
        thisExp.nextEntry()

def cueFunc(cueText):
    continueRoutine = True 
    cue.status = STARTED 
    cue.setText(cueText)
    cue.setAutoDraw(True) 
    win.flip()
    core.wait(2.5000)
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    cue.setAutoDraw(False)
    thisExp.addData("Cue Presented", cueText) 
    thisExp.nextEntry() 

def targetPres(targetStim):
    continueRoutine = True
    targetFuncComponents= [picStim, targetText]
    targetClock.reset() 
    for i in targetFuncComponents: 
        i.status = STARTED
        i.setAutoDraw(True)
    while targetClock.getTime() < 2.000: 
        picStim.setImage(targetStim)
        if continueRoutine: 
            win.flip()
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    picStim.setAutoDraw(False)
    targetText.setAutoDraw(False)
    continueRoutine = False 
    thisExp.addData("Target Image", targetStim)
    isiFunc(0.500)
    thisExp.nextEntry()
  
triggerKey = keyboard.Keyboard()
def interRunFunc():
    continueRoutine = True
    triggerKey.keys = []
    triggerKey.rt = []
    _triggerKey_allKeys = []
    interRunComponents = [interRun, triggerKey]
    for thisComponent in interRunComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    triggerClock = core.Clock()
    triggerClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine:
        t = triggerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=triggerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if interRun.status == NOT_STARTED:
            interRun.status == STARTED
            interRun.frameNStart = frameN
            interRun.tStart = t
            interRun.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(interRun, 'tStartRefresh')
            interRun.setAutoDraw(True)
        waitOnFlip = False
        if triggerKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            triggerKey.frameNStart = frameN
            triggerKey.tStart = t
            triggerKey.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(triggerKey, 'tStartRefresh')
            triggerKey.status = STARTED
            waitOnFlip = True
            win.callOnFlip(triggerKey.clock.reset)
            win.callOnFlip(triggerKey.clearEvents, eventType='keyboard')
        if triggerKey.status == STARTED and not waitOnFlip:
            theseKeys = triggerKey.getKeys(keyList=['equal'], waitRelease=False)
            _triggerKey_allKeys.extend(theseKeys)
            if len(_triggerKey_allKeys):
                triggerKey.keys = _triggerKey_allKeys[-1].name
                triggerKey.rt = _triggerKey_allKeys[-1].rt
                continueRoutine = False
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in interRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()
    # end inst routine
    for thisComponent in interRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if triggerKey.keys in ['', [], None]:
        triggerKey.keys = None
    thisExp.addData('Scanner Trigger Key',triggerKey.keys)
    thisExp.addData('Pre-Run Text', interRun.text)
    thisExp.addData('Scanner Trigger Time',triggerKey.rt)
    thisExp.nextEntry()
    routineTimer.reset()

#Run the task
blocks=[1,2]
Run=[1,2]
miniBlocks=[1,2, 3, 4]
practiceTargetArray=['Tool05.jpg', 'Tool06.jpg', 'Tool20.jpg', 'Tool08.jpg', 'Tool20.jpg']
practiceNbackArray=['Ind1.jpg', 'Ind2.jpg', 'Ind1.jpg', 'Ind2.jpg', 'Ind3.jpg']
cueList=["TARGET", "2-BACK"]
bodyList = ['Tool01.jpg', 'Tool02.jpg', 'Tool03.jpg', 'Tool04.jpg', 'Tool05.jpg','Tool06.jpg', 'Tool07.jpg', 'Tool09.jpg', 'Tool08.jpg', 'Tool10.jpg'\
'Tool11.jpg', 'Tool12.jpg', 'Tool13.jpg', 'Tool14.jpg', 'Tool15.jpg','Tool16.jpg', 'Tool17.jpg', 'Tool18.jpg', 'Tool19.jpg', 'Tool20.jpg']
toolList = ['Tool01.jpg', 'Tool02.jpg', 'Tool03.jpg', 'Tool04.jpg', 'Tool05.jpg','Tool06.jpg', 'Tool07.jpg', 'Tool09.jpg', 'Tool08.jpg', 'Tool10.jpg'\
'Tool11.jpg', 'Tool12.jpg', 'Tool13.jpg', 'Tool14.jpg', 'Tool15.jpg','Tool16.jpg', 'Tool17.jpg', 'Tool18.jpg', 'Tool19.jpg', 'Tool20.jpg']
placeList = ['Ind1.jpg', 'Ind2.jpg', 'Ind3.jpg', 'Ind4.jpg', 'Ind5.jpg', 'Ind6.jpg', 'Ind7.jpg', 'Ind8.jpg', 'Ind9.jpg', 'Ind10.jpg', \
'Ind11.jpg', 'Ind12.jpg', 'Ind13.jpg', 'Ind14.jpg', 'Ind15.jpg', 'Ind16.jpg', 'Ind17.jpg', 'Ind18.jpg', 'Ind19.jpg', 'Ind20.jpg']
faceList = ['Ind1.jpg', 'Ind2.jpg', 'Ind3.jpg', 'Ind4.jpg', 'Ind5.jpg', 'Ind6.jpg', 'Ind7.jpg', 'Ind8.jpg', 'Ind9.jpg', 'Ind10.jpg', \
'Ind11.jpg', 'Ind12.jpg', 'Ind13.jpg', 'Ind14.jpg', 'Ind15.jpg', 'Ind16.jpg', 'Ind17.jpg', 'Ind18.jpg', 'Ind19.jpg', 'Ind20.jpg']

rows = [(0,5), (5,10), (10,15), (15,20)]


#show the instructions
for i in instTextArray:
    instFunc(i)
#first do practice trials
isiFunc(3.000)
cueFunc("TARGET")
targetPres('Tool20.jpg')
choiceFunc(practiceTargetArray)
isiFunc(2.000)
cueFunc("2-BACK")
choiceFunc(practiceNbackArray)
instFunc("Great job! You will now be completing the full task.\n\nPress 1 to begin!")

lists = [bodyList, faceList, placeList, toolList, cueList]
for i in lists:
    random.shuffle(i)
    
for i in Run:#2 runs
    interRunFunc()
    isiFunc(15.000)
    for i in miniBlocks: #once every 2 blocks do a 15s isi, for 4x a run
        imgStimuli = ["face", "tool", "place", "body", "face", "tool", "place", "body"]
        for a, b in zip(blocks, cueList): # 2 blocks
            result = random.choice(imgStimuli)
            cueFunc(b) # one cue preceeds 10 trials 
            z=np.random.choice(len(rows))
            y=[]
            print("z=", z)
            print("Random Img Stim Type:", result)
            print("Cue:", b)
            if b == '2-BACK':
                if result == 'face':
                    y = faceList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("2back cue and face stim list:",b)
                    choiceFunc(b) # 10 trials
                if result == 'tool':
                    y = toolList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("2back cue and tool stim list:",b)
                    choiceFunc(b)
                if result == 'place':
                    y = placeList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("2back cue and place stim list:",b)
                    choiceFunc(b)
                if result == 'body':
                    y = bodyList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("2back cue and body stim list:", b)
                    choiceFunc(b)
            if b == 'TARGET':
                if result == 'face':
                    targetFace = random.choice(faceList[slice(*z)])
                    targetPres(targetFace)
                    y = faceList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("Target cue and face stim list :", b)
                    choiceFunc(b)
                if result == 'tool':
                    targetTool = random.choice(toolList[slice(*z)])
                    targetPres(targetTool)
                    y = toolList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("Target cue and tool stim list : ", b)
                    choiceFunc(b)
                if result == 'place':
                    targetPlace = np.random.choice(placeList[slice(*z)])
                    targetPres(targetPlace)
                    y = placeList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("Target cue and place stim list:", b)
                    choiceFunc(b)
                if result == 'body':
                    targetBody= random.choice(bodyList[slice(*z)])
                    targetPres(targetBody)
                    y = bodyList[slice(*z)]
                    b = []
                    for i in y:
                        b.extend([i, i])
                    random.shuffle(b)
                    print("Target cue and body stim list:", b)
                    choiceFunc(b)
            imgStimuli.remove(result)
        isiFunc(15.000)
#isiFunc(15.000)
instFunc("Thank you! You have completed this part of the study. \n\nPlease press 1.")
