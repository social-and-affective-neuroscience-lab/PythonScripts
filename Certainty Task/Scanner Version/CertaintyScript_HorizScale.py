#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys
import random
import csv
import pandas as pd
from numpy.random import choice
from psychopy.hardware import keyboard
from psychopy.hardware import joystick
from pyglet.window import key
keyState=key.KeyStateHandler()
prefs.general['audioLib']=['pyo']
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '2021.1.2'
expName = 'Certainty Task-JoyScanner'
expInfo = {'Participant*': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant*'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Certainty Study\\Certainty Task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001
#joystick.backend='pyglet'
win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
win.winHandle.push_handlers(keyState)
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0
nJoys = joystick.getNumJoysticks()
print("nJOys = ", nJoys)
id = 0
joy = joystick.Joystick(id)
nAxes = joy.getNumAxes()

defaultKeyboard = keyboard.Keyboard()

# Initialize variables
Instructions1Clock = core.Clock()
ITIClock = core.Clock()
BackgroundInfoClock = core.Clock()
ISIClock = core.Clock()
RoleCueClock = core.Clock()
VideoClock = core.Clock()
Q1Clock = core.Clock()
EndScreenClock = core.Clock()
routineTimerList = []
routineTimerListRed = []
routineTimerListGreen = []

Intro = visual.TextStim(win=win, text='', pos=[0,0], height=0.055, wrapWidth=1.55,color='white');
ITI_sign = visual.TextStim(win=win, text='+',pos=(0, 0), height=0.15, color='white');
ISI_sign = visual.TextStim(win=win, text='+', pos=(0, 0), height=0.1, color='white');
RoleText = visual.TextStim(win=win, text='',pos=(0, 0), height=0.1, wrapWidth=1.5, color='white');
BackgroundText = visual.TextStim(win=win, text='', pos=(0, -0.31), height=0.05, wrapWidth=1.6, color='white');
BackgroundSpace = visual.TextStim(win=win, text="When you're ready to move on, press SPACE.", pos=(0, -0.455), height=0.03, wrapWidth=1.6, color='white');
Inn_Anchor = visual.TextStim(win=win, text='Innocent', pos=(0.615, -0.39),height=0.045,color='white');
Guilty_Anchor = visual.TextStim(win=win,text='Guilty',pos=(-0.6, -0.39), height=0.045, color='white');
RoleVidText = visual.TextStim(win=win, text='', pos=(0, 0.43), height=0.058, wrapWidth=1.6, color='white');
AccusedNm = visual.TextStim(win=win, text='',pos=(0.05, -0.05), height=0.05, color='white');
VictimNm = visual.TextStim(win=win, text='',pos=(0.05, 0.29), height=0.05, color='white');
certaintyCountText = visual.TextStim(win=win, text='', pos=[0,-0.462], height=0.038, wrapWidth=1.55,color='white');
innHundred = visual.TextStim(win=win, text='', pos=(-0.483, -0.31), height=0.031, color='white');
guiltyHundred = visual.TextStim(win=win, text='100%', pos=(0.497, -0.31), height=0.031, color='white');
innFifty = visual.TextStim(win=win, text='50%', pos=(-0.242, -0.31), height=0.031, color='white');
zero=visual.TextStim(win=win, text="0%", pos=(0,-0.31), height=0.031, color="white");
guiltyFifty = visual.TextStim(win=win, text='50%', pos=(0.261, -0.31), height=0.031, color='white');
LeftAnchor = visual.TextStim(win=win, text='',pos=(-0.52, -0.35), height=0.045, wrapWidth=0.3, color='white');
RightAnchor = visual.TextStim(win=win, text='',pos=(0.535, -0.35), height=0.045, wrapWidth=0.3, color='white');
RoleQ = visual.TextStim(win=win, text='What was your role during the previous video?',pos=(0, 0.15), height=0.055, wrapWidth=1.4, color='white');
friendAcc = visual.TextStim(win=win, text='Friend of the accused',pos=(0.62, -0.246), height=0.05, wrapWidth=0.4, color='white');
friendVic = visual.TextStim(win=win, text='Friend of the victim',pos=(-0.62, -0.246), height=0.05, wrapWidth=0.4, color='white');
Det = visual.TextStim(win=win, text='Detective',pos=(0, -0.246), height=0.05, wrapWidth=0.4, color='white');
qText = visual.TextStim(win=win, text='',pos=(0, 0.07), height=0.06, wrapWidth=1.5, color='white');
qInst = visual.TextStim(win=win, text="Please use either the mouse or the number keys (1-7) to respond, then press ENTER to continue.", pos=(0,0.39), height=0.037, wrapWidth=1.5, color="white");
endText = visual.TextStim(win=win,
    text='Thank you for your participation in this study!\n\nTo submit your work and continue to the next part of the study, please press ENTER!',
    pos=(0, 0), height=0.06, wrapWidth=1.6, color='white');

yCoord = visual.TextStim(win=win, text="", height=0.08, color="white")
xArray = []
yArray = []

AccusedImage = visual.ImageStim(win=win, image='sin', mask=None, ori=0.0, pos=(-0.55, -0.05), size=(0.37, 0.27),
    color=[1,1,1], colorSpace='rgb', texRes=128.0, interpolate=True, depth=-3.0)
VictimImage = visual.ImageStim(win=win,image='sin', mask=None, ori=0.0, pos=(-0.55, 0.29), size=(0.37, 0.28),
    color=[1,1,1], colorSpace='rgb', texRes=128.0, interpolate=True, depth=-4.0)
CertaintyRatings = visual.Slider(win=win, size=(0.995, 0.11), pos=(0,  -0.39), units=None,
    labels=None, ticks=[1,2, 3, 4, 5], granularity=0.0,
    style='slider', styleTweaks=(), opacity=1.0,
    color='black', fillColor='darkblue', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-3, readOnly=False)
y1=0
innScale = visual.Rect(win=win, width=(y1, 0.11)[0], height=(y1, 0.18)[1],
    ori=0.0, pos=(0.6, 0),lineWidth=1.0,  colorSpace='rgb',  lineColor='darkGrey', fillColor='green',
    opacity=0.5, depth=-6.0, interpolate=True)
QuestionScale = visual.RatingScale(win=win, scale=None, showValue=False, showAccept=False, textColor="darkGrey", skipKeys=None, stretch=2.0, tickHeight=-1.0)

Space2 = keyboard.Keyboard()
Space1 = keyboard.Keyboard()
innKeys = keyboard.Keyboard()
guiltyKeys = keyboard.Keyboard()
endEnter = keyboard.Keyboard()
EnterEnd = keyboard.Keyboard()
enter=keyboard.Keyboard()
globalClock = core.Clock()
routineTimer = core.CountdownTimer()
cueList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#myCount = 0
increment = [0, 0]
certaintyRatingsArray = []
#showListNames = ['Broadchurch', 'Fargo', 'The Outsider', 'The Night Of','The Undoing', 'Mindhunter']
statusArray = []
#create ISI func 
def ISI_function(time):
    continueRoutine = True
    routineTimer.add(time)
    ITIComponents = [ITI_sign]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine and routineTimer.getTime() > 0:
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if ITI_sign.status == NOT_STARTED:
            ITI_sign.tStart = t
            ITI_sign.setAutoDraw(True)
        if ITI_sign.status == STARTED:
            if t>time-frameTolerance:
                ITI_sign.tStop = t
                ITI_sign.setAutoDraw(False)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)




# Intro Loop conditions
Instructions = data.TrialHandler(nReps=1.0, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('InstructionsText_Horizontal.csv'),
    seed=None, name='Instructions')
thisExp.addLoop(Instructions)
thisInstruction = Instructions.trialList[0]
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in Instructions:
    currentLoop = Instructions
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))

    #begin routine Instructions1
    continueRoutine = True
    Intro.setText(InstText)
    Intro.setFlip('None')
    Space1.keys = []
    Space1.rt = []
    _Space1_allKeys = []
    Instructions1Components = [Intro, Space1]
    for thisComponent in Instructions1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instructions1Clock.reset(-_timeToFirstFrame)
    frameN = -1

    #every frame Instructions1
    while continueRoutine:
        t = Instructions1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instructions1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if Intro.status == NOT_STARTED:
            Intro.frameNStart = frameN
            Intro.tStart = t
            Intro.setAutoDraw(True)

        waitOnFlip = False
        if Space1.status == NOT_STARTED:
            Space1.tStart = t
            Space1.status = STARTED
            waitOnFlip = True
            win.callOnFlip(Space1.clock.reset)
            win.callOnFlip(Space1.clearEvents, eventType='keyboard')
        if Space1.status == STARTED:
            theseKeys = Space1.getKeys(keyList=['space'], waitRelease=False)
            _Space1_allKeys.extend(theseKeys)
            if len(_Space1_allKeys):
                Space1.keys = _Space1_allKeys[-1].name
                Space1.rt = _Space1_allKeys[-1].rt
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in Instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    #end routine Instructions1
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if Space1.keys != None:
        Instructions.addData('Space1.rt', Space1.rt)
    routineTimer.reset()
    thisExp.nextEntry()

ISI_function(5.00)

# Create Loop for background info + role + video + questions
VidTrials = data.TrialHandler(nReps=1.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli1.xlsx'),
    seed=None, name='VidTrials')
thisExp.addLoop(VidTrials)
thisVidTrial = VidTrials.trialList[0]
if thisVidTrial != None:
    for paramName in thisVidTrial:
        exec('{} = thisVidTrial[paramName]'.format(paramName))

for thisVidTrial in VidTrials:
    currentLoop = VidTrials
    if thisVidTrial != None:
        for paramName in thisVidTrial:
            exec('{} = thisVidTrial[paramName]'.format(paramName))

    # begin routine BackgroundInfo
    continueRoutine = True
    showVar = Show
#    print("show var  = ", showVar)
#    if Show not in showListNames:
#        stimuli.__next__()
#        continue
#    showVar = Show
    print("show var  = ", showVar)
#    showListNames.remove(showVar)

    Space2.keys = []
    Space2.rt = []
    _Space2_allKeys = []
    AccusedImage.setImage(AccusedImg)
    VictimImage.setImage(VictimImg)
    AccusedNm.setText('The accused: ' + str(AccusedName))
    VictimNm.setText('The victim: ' + str(VictimName))
    BackgroundInfoComponents = [BackgroundText, BackgroundSpace, Space2, AccusedImage, VictimImage, AccusedNm, VictimNm]
    for thisComponent in BackgroundInfoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BackgroundInfoClock.reset(-_timeToFirstFrame)
    frameN = -1

    # every frame of BackgroundInfo
    while continueRoutine:
        t = BackgroundInfoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BackgroundInfoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if BackgroundText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            BackgroundText.frameNStart = frameN
            BackgroundText.tStart = t
            BackgroundText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(BackgroundText, 'tStartRefresh')
            BackgroundText.setAutoDraw(True)
        if BackgroundText.status == STARTED:
            BackgroundText.setText(Background)

        if BackgroundSpace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            BackgroundSpace.frameNStart = frameN
            BackgroundSpace.tStart = t
            BackgroundSpace.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(BackgroundSpace, 'tStartRefresh')
            BackgroundSpace.setAutoDraw(True)

        waitOnFlip = False
        if Space2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            Space2.frameNStart = frameN
            Space2.tStart = t
            Space2.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(Space2, 'tStartRefresh')
            Space2.status = STARTED
            waitOnFlip = True
            win.callOnFlip(Space2.clock.reset)
            win.callOnFlip(Space2.clearEvents, eventType='keyboard')
        if Space2.status == STARTED and not waitOnFlip:
            theseKeys = Space2.getKeys(keyList=['space'], waitRelease=False)
            _Space2_allKeys.extend(theseKeys)
            if len(_Space2_allKeys):
                Space2.keys = _Space2_allKeys[-1].name
                Space2.rt = _Space2_allKeys[-1].rt
                continueRoutine = False
        if AccusedImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            AccusedImage.frameNStart = frameN
            AccusedImage.tStart = t
            AccusedImage.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(AccusedImage, 'tStartRefresh')
            AccusedImage.setAutoDraw(True)
        if VictimImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            VictimImage.frameNStart = frameN
            VictimImage.tStart = t
            VictimImage.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(VictimImage, 'tStartRefresh')
            VictimImage.setAutoDraw(True)
        if AccusedNm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            AccusedNm.frameNStart = frameN
            AccusedNm.tStart = t
            AccusedNm.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(AccusedNm, 'tStartRefresh')
            AccusedNm.setAutoDraw(True)
        if VictimNm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            VictimNm.frameNStart = frameN
            VictimNm.tStart = t
            VictimNm.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(VictimNm, 'tStartRefresh')
            VictimNm.setAutoDraw(True)

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in BackgroundInfoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    # end routine BackgroundInfo
    for thisComponent in BackgroundInfoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if Space2.keys != None:
        VidTrials.addData('Space2.rt', Space2.rt)
#        VidTrials.addData('Show', Show)
        VidTrials.addData('Victim Name', VictimName)
        VidTrials.addData('Accused Name', AccusedName)
        VidTrials.addData('Video Clip', VideoClip)
    routineTimer.reset()

    ISI_function(2.000)
    # begin routine RoleCue
    continueRoutine = True
    routineTimer.add(4.000000)
    randCue = random.choice(cueList)
    print("randCue = ", randCue)
    if randCue == 1 or randCue == 4 or randCue == 7 or randCue == 10:
        roleCueText = "detective"
        print("roleCue = ", roleCueText)
    if randCue == 2 or randCue == 5 or randCue ==8 or randCue ==11:
        roleCueText = "friend of the accused"
        print("roleCue = ", roleCueText)
    if randCue == 3 or randCue == 6 or randCue == 9 or randCue == 12:
        roleCueText = "friend of the victim"
        print("roleCue = ", roleCueText)

    roleCueText=str(roleCueText)
    print("roleCueText = ", roleCueText)
    cueList.remove(randCue)
    RoleText.setText('Imagine that you are a \n' + str(roleCueText))
    RoleCueComponents = [RoleText]
    for thisComponent in RoleCueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RoleCueClock.reset(-_timeToFirstFrame)
    frameN = -1

    #every frame of RoleCue
    while continueRoutine and routineTimer.getTime() > 0:
        t = RoleCueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RoleCueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        if RoleText.status == NOT_STARTED:
            RoleText.tStart = t
            RoleText.setAutoDraw(True)
        if RoleText.status == STARTED:
            if t> 4.0:
                RoleText.tStop = t
                RoleText.setAutoDraw(False)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in RoleCueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    # end routine RoleCue
    for thisComponent in RoleCueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VidTrials.addData('RoleText', RoleText.text)

    ISI_function(2.00)
    
    #begin routine Video
    continueRoutine = True
    VidClip = visual.MovieStim3(
        win=win, name='VidClip',units='height', noAudio = False,filename=VideoClip,
        ori=0.0, pos=(0, 0.035), opacity=1.0,loop=False,size=[1.2, .65])
    RoleVidText.setText('Imagine that you are a ' + str(roleCueText))
    CertaintyRatings.reset()
    innHundred.setText('100%')
    innKeysCount = 0
    guiltyKeysCount = 0

    y3=0
    y1=0
    VideoComponents = [VidClip, RoleVidText, yCoord, CertaintyRatings, certaintyCountText, Inn_Anchor, Guilty_Anchor, innScale, innHundred, guiltyHundred, innFifty, zero, guiltyFifty]
    for thisComponent in VideoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VideoClock.reset(-_timeToFirstFrame)
    frameN = -1

    #every frame Video
    while continueRoutine:
        t = VideoClock.getTime()
        routineTimer1 = VideoClock.getTime()
        frameN = frameN + 1
        if innKeys.status == NOT_STARTED:
            innKeys.status = STARTED
        if guiltyKeys.status == NOT_STARTED:
            guiltyKeys.status = STARTED
        if guiltyKeysCount == 0 or y1 == 0:
            certaintyCountText.setText("0" + "% certain")
            certaintyRatingsArray.append("0")
            statusArray.append("0")
            
        if joy.getX() > 0:
            y1 += 0.005
            y3 = ((y1)/2)
            if y1 >0:
                guiltyKeysCount += 1
            if guiltyKeysCount > 100:
                guiltyKeysCount = 100
            if y1 <0:
                guiltyKeysCount -= 1
            if y1 == 0.000:
                guiltyKeysCount = 0
            if y1 >= 0.5:
                y1 = 0.5
                guiltyKeysCount = 100
#        if keyState[key.DOWN] == True:
#            y1 -= 0.005
#            y3 = ((y1)/2)
#            if y1 <0:
#                guiltyKeysCount += 1
#            if guiltyKeysCount > 100:
#                guiltyKeysCount = 100
#            if y1 >0:
#                guiltyKeysCount -= 1
#            if y1 == 0.000:
#                guiltyKeysCount = 0
#            if y1 <= -0.5:
#                y1 = -0.5
#                guiltyKeysCount = 100
#            VidTrials.addData('Down Keys RT', guiltyKeys.rt)
        if joy.getX() < -0.00045:

            y1 -= 0.005
            y3 = ((y1)/2)
            if y1 <0:
                guiltyKeysCount += 1
            if guiltyKeysCount > 100:
                guiltyKeysCount = 100
            if y1 >0:
                guiltyKeysCount -= 1
            if y1 == 0.000:
                guiltyKeysCount = 0
            if y1 <= -0.5:
                y1 = -0.5
                guiltyKeysCount = 100
                
                
        if keyState[key.UP] == False and keyState[key.DOWN] == False:
            y1=y1
#        if keyState[key.UP] == True:
#            y1 += 0.005
#            y3 = ((y1)/2)
#            if y1 >0:
#                guiltyKeysCount += 1
#            if guiltyKeysCount > 100:
#                guiltyKeysCount = 100
#            if y1 <0:
#                guiltyKeysCount -= 1
#            if y1 == 0.000:
#                guiltyKeysCount = 0
#            if y1 >= 0.5:
#                y1 = 0.5
#                guiltyKeysCount = 100
#            VidTrials.addData('Up Keys RT', innKeys.rt)

#        if keyState[key.UP] == False and keyState[key.DOWN] == False:
#            y1=y1

        if y1>0:
#            rightThumbY = joy.getY()
#            yArray.append(rightThumbY)
            innScale.setFillColor("green")
            statusArray.append("Innocent")
            guiltyKeysCount = abs(guiltyKeysCount)
            guiltyKeysCountStr = str(guiltyKeysCount)
            certaintyRatingsArray.append(guiltyKeysCountStr)
            certaintyCountText.setText(guiltyKeysCountStr + "% certain")
#            VidTrials.addData('Total CertaintyRatings', certaintyRatingsArray)
#            VidTrials.addData('Routine Timer Total', routineTimerList)

        if y1<0:
#            rightThumbY = joy.getY()
#            yArray.append(rightThumbY)
            innScale.setFillColor("red")
            statusArray.append("Guilty")
#            guiltyKeysCount = guiltyKeysCount
            guiltyKeysCountStr = str(guiltyKeysCount)
            guiltyKeysCountVal = (guiltyKeysCount* (-1))
            certaintyRatingsArray.append(guiltyKeysCountVal)
#            routineTimerList.append(routineTimer1Str)
            certaintyCountText.setText(guiltyKeysCountStr + "% certain")
#            VidTrials.addData('Total CertaintyRatings', certaintyRatingsArray)
#            VidTrials.addData('Routine Timer Total', routineTimerList)
        continueRoutine = True
#        if y1>0:
#            innScale.setFillColor("green")
#            guiltyKeysCount = abs(guiltyKeysCount)
#            guiltyKeysCountStr = str(guiltyKeysCount)
#            certaintyCountText.setText(guiltyKeysCountStr + "% certain")
#            VidTrials.addData('InnocentCertaintyRatings', guiltyKeysCount)
#
#        if y1<0:
#            innScale.setFillColor("red")
#            guiltyKeysCount = abs(guiltyKeysCount)
#            guiltyKeysCountStr = str(guiltyKeysCount)
#            certaintyCountText.setText(guiltyKeysCountStr + "% certain")
#            VidTrials.addData('GuiltyCertaintyRatings', guiltyKeysCount)

        continueRoutine = True
        if VidClip.status == NOT_STARTED:
            VidClip.setAutoDraw(True)
        if VidClip.status == STARTED:
            rightThumbY = joy.getX()
            yStr = str(rightThumbY)
            yArray.append(yStr)
            routineTimer1Str = str(routineTimer1)
            routineTimerList.append(routineTimer1Str)

            #VidTrials.addData("y coord list", yArray)
            # keep track of start time/frame for later

        if VidClip.status == FINISHED:
            continueRoutine = False

        if RoleVidText.status == NOT_STARTED:
            RoleVidText.tStart = t
            RoleVidText.setAutoDraw(True)

        if CertaintyRatings.status == NOT_STARTED:
            CertaintyRatings.setAutoDraw(True)
        if certaintyCountText.status == NOT_STARTED:
            certaintyCountText.setAutoDraw(True)
        if Inn_Anchor.status == NOT_STARTED:
            Inn_Anchor.tStart = t
            Inn_Anchor.setAutoDraw(True)
        if Guilty_Anchor.status == NOT_STARTED:
            Guilty_Anchor.tStart = t
            Guilty_Anchor.setAutoDraw(True)
        if innScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            innScale.frameNStart = frameN
            innScale.tStart = t
            innScale.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(innScale, 'tStartRefresh')
            innScale.setAutoDraw(True)
        if innScale.status == STARTED:
            innScale.setPos((y3, -0.39))
            innScale.setSize((y1, 0.11))
            innScale.setOpacity(0.5)
        if innHundred.status == NOT_STARTED:
            innHundred.tStart = t
            innHundred.setAutoDraw(True)
        if zero.status == NOT_STARTED:
            zero.tStart = t
            zero.setAutoDraw(True)
        if guiltyHundred.status == NOT_STARTED:
            guiltyHundred.tStart = t
            guiltyHundred.setAutoDraw(True)
        if innFifty.status == NOT_STARTED:
            innFifty.tStart = t
            innFifty.setAutoDraw(True)
        if guiltyFifty.status == NOT_STARTED:
            guiltyFifty.tStart = t
            guiltyFifty.setAutoDraw(True)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in VideoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    #end routine Video
    for thisComponent in VideoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VidClip.stop()
    thisExp.addData("Show", Show)
    thisExp.addData('Total Certainty Ratings', certaintyRatingsArray)
#    thisExp.addData('Routine Timer Total', routineTimerList)
#    thisExp.addData("y coord list", yArray)
    thisExp.addData("Certainty Status", statusArray)
    
    
    routineTimer.reset()
    certaintyCountText.setText("")
    guiltyKeysCount = 0
    certaintyRatingsArray = []
    routineTimerList = []
    statusArray=[]
    yArray = []
    ISI_function(2.000)
    
    
        #Ask role question
    continueRoutine = True
    _enter_allKeys = []
    slider.reset()
    trialComponents = [slider, enter, RoleQ, friendAcc, Det, friendVic, qInst]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    frameN = -1

    while continueRoutine:
        t = trialClock.getTime()

        if slider.status == NOT_STARTED:
            slider.tStart = t
            slider.setAutoDraw(True)

        waitOnFlip = False
        if enter.status == NOT_STARTED:
            enter.status = STARTED
            waitOnFlip = True
            win.callOnFlip(enter.clearEvents, eventType='keyboard')
        if enter.status == STARTED and not waitOnFlip:
            theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
            _enter_allKeys.extend(theseKeys)
            if len(theseKeys) and slider.getRating() != None:
                EnterEnd.rt = theseKeys[-1].rt
                continueRoutine = False

        if RoleQ.status == NOT_STARTED:
            RoleQ.setAutoDraw(True)
        if Det.status == NOT_STARTED:
            Det.setAutoDraw(True)
        if friendVic.status == NOT_STARTED:
            friendVic.setAutoDraw(True)
        if friendAcc.status == NOT_STARTED:
            friendAcc.setAutoDraw(True)
        if qInst.status == NOT_STARTED:
            qInst.setAutoDraw(True)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('slider.response', slider.getRating())
    if slider.getRating() == '1' or slider.getRating() == 1:
        thisExp.addData('RoleManip Check Answer','Friend of the victim')
    if slider.getRating() == '2' or slider.getRating() == 2:
        thisExp.addData('RoleManip Check Answer', 'Detective')
    if slider.getRating() == '3' or slider.getRating() == 3:
        thisExp.addData('RoleManip Check Answer', 'Friend of the accused')
    thisExp.addData('slider.rt', slider.getRT())
    if enter.keys != None:
        thisExp.addData('enter.rt', enter.rt)
    thisExp.nextEntry()
    routineTimer.reset()
    
    # Question Loop
    Questions = data.TrialHandler(nReps=1.0, method='sequential',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('QsText.csv'),
        seed=None, name='Questions')
    thisExp.addLoop(Questions)
    thisQuestion = Questions.trialList[0]
    if thisQuestion != None:
        for paramName in thisQuestion:
            exec('{} = thisQuestion[paramName]'.format(paramName))

    for thisQuestion in Questions:
        currentLoop = Questions
        if thisQuestion != None:
            for paramName in thisQuestion:
                exec('{} = thisQuestion[paramName]'.format(paramName))

        #begin routine Q1
        continueRoutine = True
        QuestionScale.reset()
        EnterEnd.keys = []
        EnterEnd.rt = []
        _EnterEnd_allKeys = []
        LeftAnchor.setText(LowAnchor)
        RightAnchor.setText(HighAnchor)
        qText.setText(QuestionText)
        Q1Components = [QuestionScale, EnterEnd, LeftAnchor, RightAnchor, qNums, qText, qInst]
        for thisComponent in Q1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Q1Clock.reset(-_timeToFirstFrame)
        frameN = -1

        #every frame Q1
        while continueRoutine:
            t = Q1Clock.getTime()

            if QuestionScale.status == NOT_STARTED:
                QuestionScale.setAutoDraw(True)
            if qInst.status == NOT_STARTED:
                qInst.setAutoDraw(True)
            if qNums.status == NOT_STARTED:
                qNums.setAutoDraw(True)
            waitOnFlip = False
            if EnterEnd.status == NOT_STARTED:
                EnterEnd.status = STARTED
                waitOnFlip = True
            if EnterEnd.status == STARTED:
                theseKeys = EnterEnd.getKeys(keyList=['return'], waitRelease=False)
                if len(theseKeys) and QuestionScale.getRating() != None:
                    EnterEnd.rt = theseKeys[-1].rt
                    continueRoutine = False
            if LeftAnchor.status == NOT_STARTED:
                LeftAnchor.setAutoDraw(True)

            if RightAnchor.status == NOT_STARTED:
                RightAnchor.setAutoDraw(True)
            if qText.status == NOT_STARTED:
                qText.setAutoDraw(True)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            if continueRoutine:
                win.flip()

        #end routine Q1
        for thisComponent in Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Questions.addData('QuestionScale.response', QuestionScale.getRating())
        Questions.addData('QuestionScale.rt', QuestionScale.getRT())
        if EnterEnd.keys != None:
            Questions.addData('EnterEnd.rt', EnterEnd.rt)
        routineTimer.reset()
        thisExp.nextEntry()

    ISI_function(5.000)
    #myCount += 1
    if not cueList:
        VidTrials.finished = True
    thisExp.nextEntry()

#begin routine EndScreen
continueRoutine = True
endEnter.keys = []
endEnter.rt = []
_endEnter_allKeys = []
EndScreenComponents = [endText, endEnter]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)
frameN = -1

#every frame EndScreen
while continueRoutine:
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if endText.status == NOT_STARTED:
        endText.frameNStart = frameN
        endText.tStart = t
        endText.setAutoDraw(True)
        waitOnFlip = False
    if endEnter.status == NOT_STARTED:
        endEnter.frameNStart = frameN
        endEnter.tStart = t
        endEnter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(endEnter.clock.reset)
        win.callOnFlip(endEnter.clearEvents, eventType='keyboard')
    if endEnter.status == STARTED and not waitOnFlip:
        theseKeys = endEnter.getKeys(keyList=['return'], waitRelease=False)
        _endEnter_allKeys.extend(theseKeys)
        if len(_endEnter_allKeys):
            endEnter.keys = _endEnter_allKeys[-1].name
            endEnter.rt = _endEnter_allKeys[-1].rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()

#end routine EndScreen
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if endEnter.keys != None:
    thisExp.addData('endEnter.rt', endEnter.rt)
thisExp.nextEntry()
routineTimer.reset()
win.flip()
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
