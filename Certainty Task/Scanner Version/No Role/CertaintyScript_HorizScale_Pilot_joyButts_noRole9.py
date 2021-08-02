
#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
showtime

'''
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
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib

from pyglet.window import key
keyState=key.KeyStateHandler()
prefs.general['audioLib']=['pyo']
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '2021.1.2'
expName = 'Certainty Task-Joy Scanner'
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
win = visual.Window(size=(1024, 768), fullscr=False, screen=0, winType='pyglet', allowGUI=True, allowStencil=False,
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

button_resp = type('', (), {})() 
button_resp.device = None
button_resp.device_number = 0
button_resp.device = joystick.Joystick(0)
button_resp.status = None
button_resp.clock = core.Clock()
button_resp.numButtons = button_resp.device.getNumButtons()


defaultKeyboard = keyboard.Keyboard()

# Initialize variables
Instructions1Clock = core.Clock()
isiClock = core.Clock()
BackgroundInfoClock = core.Clock()
ISIClock = core.Clock()
RoleCueClock = core.Clock()
VideoClock = core.Clock()
Q1Clock = core.Clock()
EndScreenClock = core.Clock()
routineTimerList = []
routineTimerListRed = []
routineTimerListGreen = []

introText = visual.TextStim(win=win, text='', pos=[0,0], height=0.05, wrapWidth=1.5,color='white');
text = visual.TextStim(win=win, text='+',pos=(0, 0), height=0.08, color='white');
ISI_sign = visual.TextStim(win=win, text='+', pos=(0, 0), height=0.08, color='white');
RoleText = visual.TextStim(win=win, text='',pos=(0, 0), height=0.07, wrapWidth=1.3, color='white');
BackgroundText = visual.TextStim(win=win, text='', pos=(0, -0.31), height=0.04, wrapWidth=1.44, color='white');
BackgroundSpace = visual.TextStim(win=win, text="When you're ready to move on, press 1.", pos=(0, -0.45), height=0.036, wrapWidth=1.6, color='white');
Inn_Anchor = visual.TextStim(win=win, text='Innocent', pos=(0.615, -0.39),height=0.045,color='white');
Guilty_Anchor = visual.TextStim(win=win,text='Guilty',pos=(-0.6, -0.39), height=0.045, color='white');
RoleVidText = visual.TextStim(win=win, text='', pos=(0, 0.43), height=0.052, wrapWidth=1.2, color='white');
AccusedNm = visual.TextStim(win=win, text='',pos=(0.05, -0.05), height=0.05, color='white');
VictimNm = visual.TextStim(win=win, text='',pos=(0.05, 0.29), height=0.05, color='white');
certaintyCountText = visual.TextStim(win=win, text='', pos=[0,-0.462], height=0.038, wrapWidth=1.55,color='white');
innHundred = visual.TextStim(win=win, text='', pos=(-0.483, -0.31), height=0.031, color='white');
guiltyHundred = visual.TextStim(win=win, text='100%', pos=(0.497, -0.31), height=0.031, color='white');
innFifty = visual.TextStim(win=win, text='50%', pos=(-0.242, -0.31), height=0.031, color='white');
zero=visual.TextStim(win=win, text="0%", pos=(0,-0.31), height=0.031, color="white");
guiltyFifty = visual.TextStim(win=win, text='50%', pos=(0.261, -0.31), height=0.031, color='white');
LeftAnchor = visual.TextStim(win=win, text='',pos=(-0.59, -0.35), height=0.045, wrapWidth=0.3, color='white');
RightAnchor = visual.TextStim(win=win, text='',pos=(0.592, -0.35), height=0.045, wrapWidth=0.3, color='white');
RoleQ = visual.TextStim(win=win, text='What was your role during the previous video?',pos=(0, 0.15), height=0.055, wrapWidth=1.4, color='white');
friendAcc = visual.TextStim(win=win, text='Friend of the accused',pos=(0.62, -0.246), height=0.05, wrapWidth=0.4, color='white');
friendVic = visual.TextStim(win=win, text='Friend of the victim',pos=(-0.62, -0.246), height=0.05, wrapWidth=0.4, color='white');
Det = visual.TextStim(win=win, text='Detective',pos=(0, -0.246), height=0.05, wrapWidth=0.4, color='white');
qText = visual.TextStim(win=win, text='',pos=(0, 0.2), height=0.05, wrapWidth=1.5, color='white');
qInst = visual.TextStim(win=win, text="Please use the joystick to hover over your choice and wait for the screen to move on.", pos=(0,0.39), height=0.037, wrapWidth=1.5, color="white");
interRun=visual.TextStim(win=win, text='', pos=(0,0), height=0.1, font='Arial', wrapWidth=1.35, color='white')

horLine = visual.Line(win=win, start=(-[1.25, 1.25][0]/2.0, 0), end=(+[1.25, 1.25][0]/2.0, 0),
    ori=0, pos=(0, -0.15), lineWidth=9,  colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
tick1 = visual.Line(win=win, start=(-[0.1, 0][0]/2.0, 0), end=(+[0.1, 0][0]/2.0, 0),
    ori=90, pos=(-0.6, -0.15), lineWidth=5,  colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
tick2 = visual.Line(win=win, start=(-[0.1, 0][0]/2.0, 0), end=(+[0.1, 0][0]/2.0, 0),
    ori=90, pos=(-0.3, -0.15), lineWidth=5,  colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
tick3 = visual.Line(win=win, start=(-[0.1, 0][0]/2.0, 0), end=(+[0.1, 0][0]/2.0, 0),
    ori=90, pos=(0, -0.15), lineWidth=5,  colorSpace='rgb',  lineColor='white', opacity=1, depth=0.0, interpolate=True)
tick4 = visual.Line(win=win, start=(-[0.1, 0][0]/2.0, 0), end=(+[0.1, 0][0]/2.0, 0),
    ori=90, pos=(0.3, -0.15), lineWidth=5,  colorSpace='rgb',  lineColor='white', opacity=1, depth=0.0, interpolate=True)
tick5 = visual.Line(win=win, start=(-[0.1, 0][0]/2.0, 0), end=(+[0.1, 0][0]/2.0, 0),
    ori=90, pos=(0.6, -0.15), lineWidth=5.0,  colorSpace='rgb',  lineColor='white', opacity=1, depth=0.0, interpolate=True)
    
endText = visual.TextStim(win=win,
    text='Thank you for your participation in this part of the study!',
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
qNums = visual.TextStim(win=win, text='1               2               3               4               5               6               7',pos=(0, -0.246), height=0.0375, wrapWidth=1.8, color='white');
num1 = visual.TextStim(win=win, text='1',pos=(-0.6, -0.246), height=0.0375, wrapWidth=1.8, color='white');
num2 = visual.TextStim(win=win, text='2',pos=(-0.3, -0.246), height=0.0375, wrapWidth=1.8, color='white');
num3 = visual.TextStim(win=win, text='3',pos=(0, -0.246), height=0.0375, wrapWidth=1.8, color='white');
num4 = visual.TextStim(win=win, text='4',pos=(0.3, -0.246), height=0.0375, wrapWidth=1.8, color='white');
num5 = visual.TextStim(win=win, text='5',pos=(0.6, -0.246), height=0.0375, wrapWidth=1.8, color='white');

trialClock = core.Clock()
slider = visual.Slider(win=win, size=(1.3, 0.1), pos=(0, -0.14), units=None,labels=None, ticks=(1, 2, 3), granularity=1.0,
    style='rating', color='LightGray', fillColor='Red', borderColor='White', labelHeight=0.05,flip=False, depth=0, readOnly=False)


Space2 = keyboard.Keyboard()
Space1 = keyboard.Keyboard()
innKeys = keyboard.Keyboard()
guiltyKeys = keyboard.Keyboard()
endEnter = keyboard.Keyboard()
EnterEnd = keyboard.Keyboard()
enter=keyboard.Keyboard()
globalClock = core.Clock()
routineTimer = core.CountdownTimer()
cueList = [1, 2, 3]
increment = [0, 0]
certaintyRatingsArray = []
statusArray = []
#create ISI func 

def isiFunc(timeVar):
    continueRoutine = True
    routineTimer.add(timeVar)
    isiComponents = [text]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)
    frameN = -1

    # every frame isi
    while continueRoutine and routineTimer.getTime() > 0:
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            text.frameNStart = frameN
            text.tStart = t
            text.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(text, 'tStartRefresh')
            text.setAutoDraw(True)
        if text.status == STARTED:
            if tThisFlipGlobal > text.tStartRefresh + timeVar-frameTolerance:
                text.tStop = t
                text.frameNStop = frameN
                win.timeOnFlip(text, 'tStopRefresh')
                text.setAutoDraw(False)
        isiOffsetTime = text.tStartRefresh + isiClock.getTime()

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    # end isi
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('isi Onset', text.tStartRefresh)
    thisExp.addData('isi Offset', isiOffsetTime)


button_resp.oldButtonState = button_resp.device.getAllButtons()[:]
button_resp.keys = []
button_resp.rt = []

# Intro Loop conditions
textArray = ['In this part of the study, you will be watching clips of television shows and making continous assessments about your thoughts regarding one of the characters.\n\nPress 1 to continue.',\
    'You will first be presented with a little background for the clip - each video you watch will be from a murder mystery show, in which one character has been accused of the crime. \n\nYou will be given information about the accused, the victim, and surrounding context for the video.\n\n\nPress 1 to continue.', \
    "We also ask that while watching the video, you make continuous judgments of your feelings toward the accused. Specifically, we ask you to evaluate how certain you are that the accused is innocent of the crime or guilty of the crime. \n\nThese assessments tend to be flexible, and may shift upon hearing something the character says or seeing something the character does. We ask that you update your assessments at any point where your feelings of certainty of the character's guilt/innocence changes. \n\nPress 1 to continue.", \
    "You can use the left joystick on the controller to indicate how certain you feel in your evaluation. Please push the joystick to the right to indicate feelings that the character is innocent and to the left to indicate feelings that the character is guilty.\n\nPushing the joystick further right or left indicates that you're feeling more certain of a character's innocence or guilt, respectively.\n\nPress 1 to continue.", \
    "The clips you will be watching are sourced from shows that have been streamed or broadcast on television. \nThe clips may contain adult themes and graphic language. While these clips will portray a character accused of a violent crime, as well as verbal descriptions of the crime, the crimes themselves will not be shown, nor will any other graphic visual content. \n\nWhen you are ready to receive the background information for the first clip, press 1."]
space = keyboard.Keyboard()
def introFunc(text):
    continueRoutine = True
    space.keys = []
    space.rt = []
    _space_allKeys = []
    introComponents = [introText, space, button_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock = core.Clock()
    introClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if introText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            introText.setText(text)
            introText.frameNStart = frameN
            introText.tStart = t
            introText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(introText, 'tStartRefresh')
            introText.setAutoDraw(True)
        if button_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            button_resp.frameNStart = frameN 
            button_resp.tStart = t  
            button_resp.tStartRefresh = tThisFlipGlobal 
            win.timeOnFlip(button_resp, 'tStartRefresh')
            button_resp.status = STARTED
            win.callOnFlip(button_resp.clock.reset) 
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [2] if i in button_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(button_resp.device_number,i)) for i in button_resp.pressedButtons]
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0: 
                button_resp.keys = theseKeys[-1] 
                button_resp.rt = button_resp.clock.getTime()
                continueRoutine=False

        waitOnFlip = False
        if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            space.frameNStart = frameN
            space.tStart = t
            space.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(space, 'tStartRefresh')
            space.status = STARTED
            waitOnFlip = True
            win.callOnFlip(space.clock.reset)
            win.callOnFlip(space.clearEvents, eventType='keyboard')
        if space.status == STARTED and not waitOnFlip:
            theseKeys = space.getKeys(keyList=['1'], waitRelease=False)
            _space_allKeys.extend(theseKeys)
            if len(_space_allKeys):
                space.keys = _space_allKeys[-1].name
                space.rt = _space_allKeys[-1].rt
#                continueRoutine = False

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    # end inst routine
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if space.keys in ['', [], None]:
        space.keys = None
    thisExp.nextEntry()
    routineTimer.reset()

for i in textArray:
    introFunc(i)

text1= 'The first video will begin momentarily....'
text2= 'The next video will begin momentarily...'
text3 = 'The next video will begin momentarily...'
text4= 'The next video will begin momentarily....'
text5= 'The next video will begin momentarily...'
text6 = 'The next video will begin momentarily...'
text7= 'The next video will begin momentarily....'
text8= 'The next video will begin momentarily...'
text9 = 'The last video will begin momentarily...'
textArray = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
triggerKey = keyboard.Keyboard()
def trialInstFunc(text):
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
        if interRun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            interRun.setText(text)
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

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in interRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        interRunOffset = interRun.tStartRefresh + triggerClock.getTime()
        if continueRoutine:
            win.flip()

    # end inst routine
    for thisComponent in interRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if triggerKey.keys in ['', [], None]:
        triggerKey.keys = None
    thisExp.addData('Scanner Trigger Key',triggerKey.keys)
    thisExp.addData('Inter-Run Text', interRun.text)
    thisExp.addData('Scanner Trigger Time',triggerKey.rt)
    thisExp.addData('Inter-Run Text Onset', interRun.tStartRefresh)
    thisExp.addData('Inter-Run Text Offset', interRunOffset)
    thisExp.nextEntry()
    routineTimer.reset()

isiFunc(5.00)

# Create Loop for background info + role + video + questions
VidTrials = data.TrialHandler(nReps=1.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli1_Pilot.xlsx'),
    seed=None, name='VidTrials')

thisExp.addLoop(VidTrials)
thisVidTrial = VidTrials.trialList[0]
if thisVidTrial != None:
    for paramName in thisVidTrial:
        exec('{} = thisVidTrial[paramName]'.format(paramName))

for (thisVidTrial, i) in zip(VidTrials, textArray):
    currentLoop = VidTrials
    if thisVidTrial != None:
        for paramName in thisVidTrial:
            exec('{} = thisVidTrial[paramName]'.format(paramName))

    # begin routine BackgroundInfo
    continueRoutine = True
    showVar = Show

    print("show var  = ", showVar)
    Space2.keys = []
    Space2.rt = []
    _Space2_allKeys = []
    AccusedImage.setImage(AccusedImg)
    VictimImage.setImage(VictimImg)
    AccusedNm.setText('The accused: ' + str(AccusedName))
    VictimNm.setText('The victim: ' + str(VictimName))
    if showVar == "Broadchurch":
        print("VIDEO 1 = BROADCHURCH")
    if showVar == "The Undoing":
        print("VIDEO 2 = THE UNDOING")
    if showVar == "Mindhunter":
        print("VIDEO 3 = MINDHUNTER")
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
        if button_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            button_resp.frameNStart = frameN  
            button_resp.tStart = t  
            button_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(button_resp, 'tStartRefresh')
            button_resp.status = STARTED
            win.callOnFlip(button_resp.clock.reset) 
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [2] if i in button_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(button_resp.device_number,i)) for i in button_resp.pressedButtons]
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:  
                button_resp.keys = theseKeys[-1] 
                button_resp.rt = button_resp.clock.getTime()
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        bgInfoOffsetTime = VictimNm.tStartRefresh + BackgroundInfoClock.getTime()
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
        VidTrials.addData('Victim Name', VictimName)
        VidTrials.addData('Accused Name', AccusedName)
        VidTrials.addData('Video Clip', VideoClip)
    if button_resp.keys in ['', [], None]: 
        button_resp.keys=None
    thisExp.addData('button_resp.keys',button_resp.keys)
    thisExp.addData("Background Offset Time", bgInfoOffsetTime)
    if button_resp.keys != None: 
        thisExp.addData('button_resp.rt', button_resp.rt)
    routineTimer.reset()

    isiFunc(3.000)
    # begin routine RoleCue
#    continueRoutine = True
#    routineTimer.add(6.5000000)
#    randCue = random.choice(cueList)
#    print("randCue = ", randCue)
#    if randCue == 1:
#        roleCueText = "detective and will be called to testify"
#        print("roleCue = ", roleCueText)
#    if randCue == 2:
#        roleCueText = "friend of the accused and will be called to testify in support of the accused"
#        print("roleCue = ", roleCueText)
#    if randCue == 3:
#        roleCueText = "friend of the victim and will be called to testify in support of the victim"
#        print("roleCue = ", roleCueText)
#
#    roleCueText=str(roleCueText)
#    print("roleCueText = ", roleCueText)
#    cueList.remove(randCue)
#    RoleText.setText('Imagine that you are a \n' + str(roleCueText))
#    RoleCueComponents = [RoleText]
#    for thisComponent in RoleCueComponents:
#        thisComponent.tStart = None
#        thisComponent.tStop = None
#        if hasattr(thisComponent, 'status'):
#            thisComponent.status = NOT_STARTED
#    t = 0
#    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
#    RoleCueClock.reset(-_timeToFirstFrame)
#    frameN = -1
#
#    #every frame of RoleCue
#    while continueRoutine and routineTimer.getTime() > 0:
#        t = RoleCueClock.getTime()
#        tThisFlip = win.getFutureFlipTime(clock=RoleCueClock)
#        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
#        if RoleText.status == NOT_STARTED:
#            RoleText.tStart = t
#            RoleText.setAutoDraw(True)
#        if RoleText.status == STARTED:
#            if t> 6.50000:
#                RoleText.tStop = t
#                RoleText.setAutoDraw(False)
#        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
#            core.quit()
#        if not continueRoutine:
#            break
#        continueRoutine = False
#        for thisComponent in RoleCueComponents:
#            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                continueRoutine = True
#                break
#        if continueRoutine:
#            win.flip()
#
#    # end routine RoleCue
#    for thisComponent in RoleCueComponents:
#        if hasattr(thisComponent, "setAutoDraw"):
#            thisComponent.setAutoDraw(False)
#    VidTrials.addData('RoleText', RoleText.text)

    isiFunc(3.00)
    trialInstFunc(i)
    isiFunc(15.00)

    #begin routine Video
    continueRoutine = True
    VidClip = visual.MovieStim3(
        win=win, name='VidClip',units='height', noAudio = False,filename=VideoClip,
        ori=0.0, pos=(0, 0.035), opacity=1.0,loop=False,size=[1.2, .65])
#    RoleVidText.setText('Imagine that you are a ' + str(roleCueText))
    CertaintyRatings.reset()
    innHundred.setText('100%')
    innKeysCount = 0
    guiltyKeysCount = 0

    y3=0
    y1=0
    VideoComponents = [VidClip, yCoord, CertaintyRatings, certaintyCountText, Inn_Anchor, Guilty_Anchor, innScale, innHundred, guiltyHundred, innFifty, zero, guiltyFifty]
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
#
#        if RoleVidText.status == NOT_STARTED:
#            RoleVidText.tStart = t
#            RoleVidText.setAutoDraw(True)

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
    isiFunc(15.000)
    introFunc("You will now be answering questions about the previous video. \n\nFor each question, please use the joystick to hover over an answer choice, then wait until the screen moves on. \n\nPlease press 1 to continue.")
    button_resp.clock.reset()
#        #Ask role question
#    continueRoutine = True
#    _enter_allKeys = []
#    trialComponents = [joy, tick1, tick3, tick5, horLine, friendAcc, Det, friendVic, qInst]
#    for thisComponent in trialComponents:
#        thisComponent.tStart = None
#        thisComponent.tStop = None
#        thisComponent.tStartRefresh = None
#        thisComponent.tStopRefresh = None
#        if hasattr(thisComponent, 'status'):
#            thisComponent.status = NOT_STARTED
#    t = 0
#    frameN = -1
#    Det.setColor("white")
#    friendAcc.setColor("white")
#    friendVic.setColor("white")
#    roleSelect=[]
#    routineTimer.add(8.500)
#    while continueRoutine and routineTimer.getTime() > 0:
#        t = trialClock.getTime()
#
#        waitOnFlip = False
#        t = VideoClock.getTime()
#        routineTimer1 = VideoClock.getTime()
#        frameN = frameN + 1
#        if horLine.status == NOT_STARTED:
#            horLine.tStart = t
#            horLine.setAutoDraw(True)
#        if tick1.status == NOT_STARTED:
#            tick1.tStart = t
#            tick1.setAutoDraw(True)
#        if tick3.status == NOT_STARTED:
#            tick3.tStart = t
#            tick3.setAutoDraw(True)
#        if tick5.status == NOT_STARTED:
#            tick5.tStart = t
#            tick5.setAutoDraw(True)
#                
#        if RoleQ.status == NOT_STARTED:
#            RoleQ.setAutoDraw(True)
#        if Det.status == NOT_STARTED:
#            Det.setAutoDraw(True)
#        if friendVic.status == NOT_STARTED:
#            friendVic.setAutoDraw(True)
#        if friendAcc.status == NOT_STARTED:
#            friendAcc.setAutoDraw(True)
#        if qInst.status == NOT_STARTED:
#            qInst.setAutoDraw(True)
#        if keyState[key.UP] == False and keyState[key.DOWN] == False:
#            Det.setColor("white")
#            friendVic.setColor("white")
#            friendAcc.setColor("white")
#        if joy.getX() < 0.69 and joy.getX() > -0.69:
#            Det.setColor("green")
#            friendVic.setColor("white")
#            friendAcc.setColor("white")
#            roleSelect = "Detective"
#
#        if joy.getX() > -2 and joy.getX() < -0.7:
#            friendVic.setColor("green")
#            Det.setColor("white")
#            friendAcc.setColor("white")
#            roleSelect = " Friend of Victim"
#        if joy.getX() > 0.7 and joy.getX() <2:
#            friendAcc.setColor("green")
#            Det.setColor("white")
#            friendVic.setColor("white")
#            roleSelect = "Friend of Accused"
##        if RoleQ.status == STARTED:
##            if RoleQ > RoleQ.tStartRefresh + 8.00-frameTolerance:
##                RoleQ.tStop = t
##                RoleQ.frameNStop = frameN
##                win.timeOnFlip(text, 'tStopRefresh')
##                RoleQ.setAutoDraw(False)
##                continu
##
#
#
#        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
#            core.quit()
#
#        if not continueRoutine:
#            break
#        continueRoutine = False
#        for thisComponent in trialComponents:
#            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                continueRoutine = True
#                break
#
#        if continueRoutine:
#            win.flip()
#
#    for thisComponent in trialComponents:
#        if hasattr(thisComponent, "setAutoDraw"):
#            thisComponent.setAutoDraw(False)
#    thisExp.addData('Role Selected', roleSelect)
##    if enter.keys != None:
##        thisExp.addData('button_resp.rt', button_resp.rt)
#    thisExp.nextEntry()
#    routineTimer.reset()
#    isiFunc(2.00)
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
        ratingSelection = 0
        QuestionScale.reset()
        EnterEnd.keys = []
        EnterEnd.rt = []
        _EnterEnd_allKeys = []
        LeftAnchor.setText(LowAnchor)
        RightAnchor.setText(HighAnchor)
        qText.setText(QuestionText)
        Q1Components = [QuestionScale, tick1, tick2, tick3, tick4, tick5,  horLine, num1, num2, num3, num4, num5, joy, button_resp, LeftAnchor, RightAnchor, qNums, qText, qInst]
        for thisComponent in Q1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Q1Clock.reset(-_timeToFirstFrame)
        frameN = -1
        routineTimer.add(8.00)
        #every frame Q1
        while continueRoutine and routineTimer.getTime() > 0:
            t = Q1Clock.getTime()
            if horLine.status == NOT_STARTED:
                horLine.tStart = t
                horLine.setAutoDraw(True)
            if tick1.status == NOT_STARTED:
                tick1.tStart = t
                tick1.setAutoDraw(True)
            if tick4.status == NOT_STARTED:
                tick4.tStart = t
                tick4.setAutoDraw(True)
            if tick2.status == NOT_STARTED:
                tick2.tStart = t
                tick2.setAutoDraw(True)
            if tick3.status == NOT_STARTED:
                tick3.tStart = t
                tick3.setAutoDraw(True)
            if tick5.status == NOT_STARTED:
                tick5.tStart = t
                tick5.setAutoDraw(True)
            if num1.status == NOT_STARTED:
                num1.setAutoDraw(True)
            if num3.status == NOT_STARTED:
                num3.setAutoDraw(True)
            if num2.status == NOT_STARTED:
                num2.setAutoDraw(True)
            if num4.status == NOT_STARTED:
                num4.setAutoDraw(True)
            if num5.status == NOT_STARTED:
                num5.setAutoDraw(True)

            if keyState[key.UP] == False and keyState[key.DOWN] == False:
                num1.setColor("white")
                num3.setColor("white")
                num2.setColor("white")
                num4.setColor("white")
                num5.setColor("white")

            if joy.getX() < 1.6 and  joy.getX() > 0.98:
                num5.setColor("green")
                num3.setColor("white")
                num2.setColor("white")
                num4.setColor("white")
                num1.setColor("white")
                ratingSelection = 5
            if joy.getX() > -1.6 and joy.getX() < -0.98:
                num1.setColor("green")
                num2.setColor("white")
                num3.setColor("white")
                num4.setColor("white")
                num5.setColor("white")
                ratingSelection = 1
            if joy.getX() > -0.98 and joy.getX() < -0.3:
                num2.setColor("green")
                num1.setColor("white")
                num3.setColor("white")
                num4.setColor("white")
                num5.setColor("white")
                ratingSelection = 2
            if joy.getX() > -0.3 and joy.getX() <0.3:
                num4.setColor("white")
                num1.setColor("white")
                num3.setColor("green")
                num2.setColor("white")
                num5.setColor("white")
                ratingSelection = 3
            if joy.getX() >0.3 and joy.getX() <0.98:
                num4.setColor("green")
                num1.setColor("white")
                num3.setColor("white")
                num2.setColor("white")
                num5.setColor("white")
                ratingSelection = 4

            if qInst.status == NOT_STARTED:
                qInst.setAutoDraw(True)
            waitOnFlip = False
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
        thisExp.addData('Rating Selected', ratingSelection)
        routineTimer.reset()
        isiFunc(2.00)
        thisExp.nextEntry()
    isiFunc(3.000)
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
