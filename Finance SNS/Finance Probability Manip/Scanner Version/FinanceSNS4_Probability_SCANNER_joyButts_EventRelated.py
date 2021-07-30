#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import pandas as pd
import sys
import random
from psychopy.hardware import keyboard
from psychopy.tools.filetools import fromFile
from psychopy.hardware import joystick

from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from pyglet.window import key
keyState=key.KeyStateHandler()

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '2021.1.2'
expName = 'FinanceSNS'
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
    originPath='F:\\Moralizing Self-Regulation\\In-Person Study\\Finance SR\\ProbManip\\FinanceSNS4_Probability.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001

win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

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



InstructionsClock = core.Clock()
instructions1 = visual.TextStim(win=win, text='',font='Arial', pos=(0, 0), height=0.05, wrapWidth=1.4,color='white')
interRun = visual.TextStim(win=win, text='', font='Arial', pos=(0,0), height=0.06, wrapWidth=1.35, color='white')
space = keyboard.Keyboard()

instructions2 = visual.TextStim(win=win,
    text='Which type of video would you like to make decisions about? Please use the number keys 1, 2, and 3 to move to the video you would like, then press ENTER to continue.',
    font='Arial', pos=(0, 0.3), height=0.05, wrapWidth=1.4, color='white');
enter = keyboard.Keyboard()
chooseGameClock = core.Clock()

comedyVids = visual.TextStim(win=win, text='Comedy Videos', pos = (-0.5,-0.08), height=0.05)
musicVids = visual.TextStim(win=win, text='Music Videos', pos = (0.5,-0.08), height=0.05)
gameVids = visual.TextStim(win=win, text='Gaming Videos', pos = (0,-0.08), height=0.05)
lineStim = visual.Line(win=win,start=(-2.5, 0), end=(2.5, 0), ori=90.0, lineWidth=10.0, lineColor='black', fillColor='black')

comedy = visual.ImageStim(win=win, image='comedy.PNG', pos=(-0.5, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)
music = visual.ImageStim(win=win, image='music.PNG', pos=(0.5, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)
game = visual.ImageStim(win=win, image='gaming.PNG', pos=(0, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)

polygon = visual.Rect(win=win,size=(0.39, 0.28),
    ori=0.0, pos=(0, 0),lineWidth=8, lineColor='black', fillColor=None,interpolate=True)

instructions3 = visual.TextStim(win=win, text='Which type of finance tips would you like to make decisions about? Please use the number keys 1, 2, and 3 to move to the tips you would like, then press ENTER to continue.',
    font='Arial', pos=(0, 0.3), height=0.05, wrapWidth=1.4, color='white');

saveTips = visual.TextStim(win=win, text='Saving Tips',pos=(0, -0.08), height=0.05,color='white')
spendTips = visual.TextStim(win=win, text='Spending Tips',pos=(-0.5, -0.08), height=0.05,color='white')
investTips = visual.TextStim(win=win, text='Investing Tips',pos=(0.5, -0.08), height=0.05,color='white')

spendImg = visual.ImageStim(win=win, image='spending.PNG', pos=(-0.5, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)
saveImg = visual.ImageStim(win=win, image='saving.PNG', pos=(0, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)
investImg = visual.ImageStim(win=win, image='investing.PNG', pos=(0.5, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)

polygon_2 = visual.Rect(win=win,size=(0.39, 0.28),
    ori=0.0, pos=(0, 0),lineWidth=8, lineColor='black', fillColor=None,interpolate=True)
inst5A = visual.TextStim(win=win, text='',pos=(0, 0.016), height=0.05, wrapWidth=1.4, color='white')
inst5B = visual.TextStim(win=win, text='', pos=(0, 0.015), height=0.05, wrapWidth=1.4, color='white')

nameInstructions = visual.TextStim(win=win, text='', pos=(0,0.2), height=0.05, wrapWidth=1.4, color='white')
financeName=[]
friendName=[]
financeWord=[]
friendWord=[]
selectedGameTime = []
selectedQTime = []

selectedTipTime = []
selectedVidTime = []

financeNameStr = visual.TextStim(win=win, text='', pos=(0,0), height=0.045, wrapWidth=1.4, color='white')
friendNameStr = visual.TextStim(win=win, text='', pos=(0,0), height=0.045, wrapWidth=1.4, color='white')
financeWordStr = visual.TextStim(win=win, text='', pos=(0,0), height=0.045, wrapWidth=1.4, color='white')
friendWordStr = visual.TextStim(win=win, text='', pos=(0,0), height=0.045, wrapWidth=1.4, color='white')

ISIClock = core.Clock()
isi = visual.TextStim(win=win,text='+',font='Arial',pos=(0, 0), height=0.08, color='white');
ISI2Clock = core.Clock()
isi2 = visual.TextStim(win=win,text='+',font='Arial',pos=(0, 0), height=0.08, color='white');
text = visual.TextStim(win=win,text='+',font='Arial',pos=(0, 0), height=0.08, color='white');
isiClock = core.Clock()
itiClock = core.Clock()
blank = visual.TextStim(win=win, text='', pos=(0,0), height=0.001, color='white')

jitterArray = [1.16, 2.5, 3.30, 4.26, 5.94, 1.1, 0.96, 2.8, 2.5, 3.0, 1.1, 1.5, 2.13, 2.145, 4.18, 3.04, 1.16, 2.5, 3.30, 1.26, 2.94, 1.1, 0.96, 0.8, 3.5, 3.0, 1.1, 1.5, 2.13, 2.145, 1.18, 2.04, 1.16, 2.5, 1.30, 0.26, 0.94, 1.1, 0.96, 2.8, 3.5, 3.0, 1.1, 1.5, 2.13, 2.145, 2.18, 1.04]

cueScreenClock=core.Clock()
cuetext=visual.TextStim(win=win, text='', pos=(0,0), height=0.12, color='white')

selectedVidImgLeft = visual.ImageStim(win=win, image="comedy.PNG", pos = (-0.5, 0.15), size=(0.22, 0.15),
    color=[1,1,1], texRes=128.0, interpolate=True)
selectedVidImgRight = visual.ImageStim(win=win, image="comedy.PNG", pos = (0.5, 0.15), size=(0.22, 0.15),
    color=[1,1,1], texRes=128.0, interpolate=True)
selectedTipImgRight = visual.ImageStim(win=win, image="comedy.PNG", pos = (0.5, -0.4), size=(0.22, 0.15),
    color=[1,1,1], texRes=128.0, interpolate=True)
selectedTipImgLeft = visual.ImageStim(win=win, image="comedy.PNG", pos = (-0.5, -0.4), size=(0.22, 0.15),
    color=[1,1,1], texRes=128.0, interpolate=True)
topLeftText = visual.TextStim(win=win, text='', pos=(-0.5,0.4), height=0.07, color='white')
topLeftTime = visual.TextStim(win=win, text='', pos=(-0.5,0.3), height=0.07, color='white')
topRightText = visual.TextStim(win=win, text='', pos=(0.5,0.4), height=0.07, color='white')
topRightTime = visual.TextStim(win=win, text='', pos=(0.5,0.3), height=0.07, color='white')

botLeftText = visual.TextStim(win=win, text='', pos=(-0.5,-0.16), height=0.07, color='white')
botLeftTime = visual.TextStim(win=win, text='', pos=(-0.5,-0.25), height=0.07, color='white')
botRightText = visual.TextStim(win=win, text='', pos=(0.5,-0.16), height=0.07, color='white')
botRightTime = visual.TextStim(win=win, text='', pos=(0.5,-0.25), height=0.07, color='white')

andSignLeft = visual.TextStim(win=win, text='+', pos=(-0.5,0), height=0.065, color='white')
andSignRight = visual.TextStim(win=win, text='+', pos=(0.5,0), height=0.065, color='white')
regCue = visual.TextStim(win=win, text='default text', height=0.07, color='white', pos=(0,0), wrapWidth=1.2)

choiceSelection = keyboard.Keyboard()
ChoiceClock = core.Clock()
counterList = [1,2,3,4]
counterCode = random.choice(counterList)
counterCode = str(counterCode)
print("Counter Code: " + counterCode )

endText = visual.TextStim(win=win, text='', pos=(0,0), height=0.046, wrapWidth = 1.4, color='white')
endText1 = visual.TextStim(win=win, text='Thank you for participating, you have completed this part of the study!\n\nPlease press ENTER to submit your work and continue with the rest of the study.', pos=(0,0), height=0.001, color='white')

bucket = ["a","b","c","d","e", "f", "g", "h", "i","j","k","l", "m","n","o","p","q","r","s", "t", "u", "v", "w", "x", "y", "z", "za", "zb", "zc", "zd",
"a","b","c","d","e", "f", "g", "h", "i","j","k","l", "m","n","o","p","q","r","s", "t", "u", "v", "w", "x", "y", "z", "za", "zb", "zc", "zd",
"a","b","c","d","e", "f", "g", "h", "i","j","k","l", "m","n","o","p","q","r","s", "t", "u", "v", "w", "x", "y", "z", "za", "zb", "zc", "zd",
"a","b","c","d","e", "f", "g", "h", "i","j","k","l", "m","n","o","p","q","r","s", "t", "u", "v", "w", "x", "y", "z", "za", "zb", "zc", "zd"]


selectedTips=[]
selectedVid=[]

keyResp = keyboard.Keyboard()
globalClock = core.Clock()
routineTimer = core.CountdownTimer() 
def isiFunc():
    continueRoutine = True
#    timeVar = random.choice(jitterArray)
#    routineTimer.add(timeVar)
    routineTimer.add(2.000)
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
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance: # change 2 to timeVar when using jitter
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
#    jitterArray.remove(timeVar)

    thisExp.addData('isi Onset', text.tStartRefresh)
    thisExp.addData('isi Offset', globalClock.getTime())

def itiFunc():
    continueRoutine = True
    routineTimer.add(15.000)
    itiComponents = [text]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)
    frameN = -1

    # every frame isi
    while continueRoutine and routineTimer.getTime() > 0:
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            text.frameNStart = frameN
            text.tStart = t
            text.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(text, 'tStartRefresh')
            text.setAutoDraw(True)
        if text.status == STARTED:
            if tThisFlipGlobal > text.tStartRefresh + 15.000-frameTolerance:
                text.tStop = t
                text.frameNStop = frameN
                win.timeOnFlip(text, 'tStopRefresh')
                text.setAutoDraw(False)
        itiOffsetTime = text.tStartRefresh + itiClock.getTime()

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    # end iti
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    thisExp.addData('iti Onset', text.tStartRefresh)
    thisExp.addData('iti Offset', globalClock.getTime())

def cueScreenFunc(bucketCue):
    continueRoutine = True
    routineTimer.add(2)
    CueScreenComponents = [cuetext]
    for thisComponent in CueScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cueScreenClock.reset(-_timeToFirstFrame)
    frameN = -1

    # every frame isi
    while continueRoutine and routineTimer.getTime() > 0:
        t = cueScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cueScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if cuetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            cuetext.setText(bucketCue)
            cuetext.frameNStart = frameN
            cuetext.tStart = t
            cuetext.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(cuetext, 'tStartRefresh')
            cuetext.setAutoDraw(True)
        if cuetext.status == STARTED:
            if t> 2:
                cuetext.tStop = t
                cuetext.setAutoDraw(False)
                cuetext.frameNStop = frameN
                win.timeOnFlip(cuetext, 'tStopRefresh')

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in CueScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    # end cue
    for thisComponent in CueScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Cuetext.started', cuetext.tStartRefresh)
    thisExp.addData('Cuetext.stopped', globalClock.getTime())


instText1 = 'In this part of the study, you will be making choices to allocate 20 minutes between reading finance tips and watching youtube videos. \n\nBefore making these decisions, you will first be prompted to choose what type of videos and what type of finance tips you want to make these allocations between.\n\nPress 1 to continue.'
instText2a = 'You will be presented with one allocation of 20 minutes on the left side of the screen and another allocation of 20 minutes on the right side of your screen. \n You can press the "1" key to select the allocation on the left, or you can press the "2" key to select the allocation on the right. \n\n You will only have 6 seconds to make your selection once the allocations appear on the screen.\n\nPress 1 to continue.'
instText2b= 'At the end of the task, one trial will be selected at random. The allocation you chose in that trial will be used to determine how long you spend on each activity at the end of the study.\n\n Some trials have a higher likelihood of being selected, while other trials have a lower likelihood of being selected. \n\nPress 1 to continue.'
instText3= 'When making your decisions, you will be cued with specific names and words. On the following screens, you will be instructed to type out the names of two different, independent people in your life.\n\nPress 1 to continue.'
instText4= "Throughout these decisions, you will either see one of the names you typed, the word 'High', the word 'Low', the word 'Unknown', or the word 'Choice' in the center of the screen. \n\nPress 1 to continue."
instText5="Each decision will consist of making allocations of 20 minutes towards watching the videos you chose and reading the financial tips you chose. You will be presented with two different allocations - one on the left side of your screen and one on the right side of your screen. \n\nTo choose the allocation on the left side, press the 1 key. \nTo choose the allocation on the right side, press the 2 key.\nYou will have 6 seconds to make your choice before the trials move on. \n\nPress 1 to continue."

def instructionsFunc(instText):
    continueRoutine = True
    space.keys = []
    space.rt = []
    _space_allKeys = []
    InstructionsComponents = [instructions1, space]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if instructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            instructions1.frameNStart = frameN
            instructions1.tStart = t
            instructions1.tStartRefresh = tThisFlipGlobal
            instructions1.setText(instText)
            win.timeOnFlip(instructions1, 'tStartRefresh')
            instructions1.setAutoDraw(True)

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
                continueRoutine = False

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    # end Instructions
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if space.keys in ['', [], None]:
        space.keys = None
    thisExp.addData('space.keys',space.keys)
    thisExp.addData('space.RT',space.rt)
    thisExp.nextEntry()
    routineTimer.reset()

instructionsFunc(instText1)

# start vid choice
continueRoutine = True
x = []
v=[]
x=0
if keyResp.keys == '1':
    x = -0.5
if keyResp.keys == '2':
    x = 0
if keyResp.keys == '3':
    x=0.5

ypos = (-0.25)
ypos = float(ypos)

enter.keys = []
enter.rt = []
_enter_allKeys = []
GameChoiceClock = core.Clock()
GameChoiceComponents = [enter, instructions2,GameChoiceClock, polygon, v,x, musicVids, gameVids, comedyVids, game, music, comedy, keyResp]
for thisComponent in GameChoiceComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
GameChoiceClock=core.Clock()
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GameChoiceClock.reset(-_timeToFirstFrame)
frameN = -1
_keyResp_allKeys = []
# begin game choice
while continueRoutine:
    t = GameChoiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GameChoiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        enter.frameNStart = frameN
        enter.tStart = t
        enter.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(enter, 'tStartRefresh')
        enter.status = STARTED

        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)
        win.callOnFlip(enter.clearEvents, eventType='keyboard')
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name
            enter.rt = _enter_allKeys[-1].rt

            continueRoutine = False
    if keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        keyResp.frameNStart = frameN
        keyResp.tStart = t
        keyResp.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(keyResp, 'tStartRefresh')
        keyResp.status = STARTED

        waitOnFlip = True
        win.callOnFlip(keyResp.clock.reset)
        win.callOnFlip(keyResp.clearEvents, eventType='keyboard')
    if keyResp.status == STARTED and not waitOnFlip:
        theseKeys = keyResp.getKeys(keyList=['1', '2', '3', 'return'], waitRelease=False)
        _keyResp_allKeys.extend(theseKeys)
        if len(_keyResp_allKeys):
            keyResp.keys = _keyResp_allKeys[-1].name
            keyResp.rt = _keyResp_allKeys[-1].rt

    if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instructions2.frameNStart = frameN
        instructions2.tStart = t
        instructions2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(instructions2, 'tStartRefresh')
        instructions2.setAutoDraw(True)

    if comedy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        comedy.frameNStart = frameN
        comedy.tStart = t
        comedy.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(comedy, 'tStartRefresh')
        comedy.setAutoDraw(True)

    if game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        game.frameNStart = frameN
        game.tStart = t
        game.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(game, 'tStartRefresh')
        game.setAutoDraw(True)

    if music.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        music.frameNStart = frameN
        music.tStart = t
        music.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(music, 'tStartRefresh')
        music.setAutoDraw(True)

    if comedyVids.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        comedyVids.frameNStart = frameN
        comedyVids.tStart = t
        comedyVids.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(comedyVids, 'tStartRefresh')
        comedyVids.setAutoDraw(True)

    if musicVids.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        musicVids.frameNStart = frameN
        musicVids.tStart = t
        musicVids.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(musicVids, 'tStartRefresh')
        musicVids.setAutoDraw(True)

    if gameVids.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:

        gameVids.frameNStart = frameN
        gameVids.tStart = t
        gameVids.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(gameVids, 'tStartRefresh')
        gameVids.setAutoDraw(True)
    if polygon.status == NOT_STARTED and asarray(keyResp.keys == '1' or keyResp.keys == '2' or keyResp.keys == '3'):
        polygon.frameNStart = frameN
        polygon.tStart = t
        polygon.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(polygon, 'tStartRefresh')
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        polygon.setPos((x, -0.25))
    if keyResp.keys == '1':
        x = -0.5
    if keyResp.keys == '2':
        x = 0
    if keyResp.keys == '3':
        x=0.5


    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in GameChoiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

#end vid choice
for thisComponent in GameChoiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if keyResp.keys in ['', [], None]:
    keyResp.keys = None
if keyResp.keys != None:
    thisExp.addData('keyResp.rt', keyResp.rt)
    thisExp.addData('keyResp Keys', keyResp.keys)
if x ==-0.5 and enter.keys != None:
    v = 1
#    selectedVid = 'Comedy Videos'
    print("selected vid text: comedy vids")
    selectedVidImgLeft.setImage('comedy.PNG')
    selectedVidImgRight.setImage('comedy.PNG')
if x == 0 and enter.keys != None:
    v = 2
#    selectedVid = 'Gaming Videos'
    print("selected vid text: gaming vid")
    selectedVidImgLeft.setImage('gaming.PNG')
    selectedVidImgRight.setImage('gaming.PNG')
if x == 0.5 and enter.keys != None:
    v = 3
#    selectedVid = 'Music Videos'
    print("selected vid text: music videos")
    selectedVidImgLeft.setImage('music.PNG')
    selectedVidImgRight.setImage('music.PNG')
if keyResp.keys == None and enter.keys != None:
    v = 1
    print("selected vid text: comedy vids")
    selectedVidImgLeft.setImage('comedy.PNG')
    selectedVidImgRight.setImage('comedy.PNG')
thisExp.addData('Video Choice',keyResp.keys)
thisExp.nextEntry()
if enter.keys in ['', [], None]:
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
if enter.keys != None:
    thisExp.addData('enter.rt', enter.rt)
thisExp.nextEntry()
routineTimer.reset()

continueRoutine = True
x1 = []

enter1 = keyboard.Keyboard()
chooseQClock = core.Clock()
FinTipChoiceClock = core.Clock()
keyResp1 = keyboard.Keyboard()
FinTipChoiceComponents = [enter1, keyResp1, spendTips, saveImg, saveTips, spendImg, investImg, investTips, instructions3, polygon_2, x1, t]
q=[]
x1 = 0

if keyResp1.keys == '1':
    x1 = -0.5
if keyResp1.keys == '2':
    x1 = 0
if keyResp1.keys == '3':
    x1 = 0.5

for thisComponent in FinTipChoiceComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinTipChoiceClock.reset(-_timeToFirstFrame)
frameN = -1
_enter1_allKeys = []
_keyResp1_allKeys = []
while continueRoutine:
    t = FinTipChoiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinTipChoiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if instructions3.status == NOT_STARTED:
        instructions3.status = STARTED
        instructions3.setAutoDraw(True)
    if saveImg.status == NOT_STARTED:
        saveImg.status = STARTED
        saveImg.setAutoDraw(True)
    if spendImg.status == NOT_STARTED:
        spendImg.status = STARTED
        spendImg.setAutoDraw(True)
    if investImg.status == NOT_STARTED:
        investImg.setAutoDraw(True)
    if investTips.status == NOT_STARTED:
        investTips.setAutoDraw(True)
    if saveTips.status == NOT_STARTED:
        saveTips.setAutoDraw(True)
    if spendTips.status == NOT_STARTED:
        spendTips.setAutoDraw(True)
    if keyResp1.status == NOT_STARTED:
        keyResp1.status = STARTED
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name
            keyResp1.rt = _keyResp1_allKeys[-1].rt
    if polygon_2.status == NOT_STARTED and asarray(keyResp1.keys == '1' or keyResp1.keys == '2' or keyResp1.keys == '3'):
        polygon_2.frameNStart = frameN
        polygon_2.tStart = t
        polygon_2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(polygon_2, 'tStartRefresh')
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:
        polygon_2.setPos((x1, -0.25))
    if keyResp1.keys == '1':
        x1 = -0.5
    if keyResp1.keys == '2':
        x1 = 0
    if keyResp1.keys == '3':
        x1 = 0.5

    if keyResp1.keys == '1' or keyResp1.keys == '2' or keyResp1.keys == '3' and polygon_2.status == NOT_STARTED:
        polygon_2.status == STARTED
        polygon_2.setAutoDraw(True)
    waitOnFlip = False
    if enter1.status == NOT_STARTED:
        enter1.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter1.clock.reset)
        win.callOnFlip(enter1.clearEvents, eventType='keyboard')
    if enter1.status == STARTED and not waitOnFlip:
        theseKeys = enter1.getKeys(keyList=['return'], waitRelease=False)
        _enter1_allKeys.extend(theseKeys)
        if len(_enter1_allKeys):
            enter1.keys = _enter1_allKeys[-1].name
            enter1.rt = _enter1_allKeys[-1].rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    for thisComponent in FinTipChoiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

for thisComponent in FinTipChoiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if x1 == -0.5 and enter1.keys != None:
    q=1
#    selectedTips = 'Saving Tips'
    print('selected tip text: saving tips')
#    selectedTipImg = 'saving.PNG'
    selectedTipImgLeft.setImage('saving.PNG')
    selectedTipImgRight.setImage('saving.PNG')
if x1 == 0 and enter1.keys != None:
    q = 2
    print('selected tip text: investing')
    selectedTipImgLeft.setImage('investing.PNG')
    selectedTipImgRight.setImage('investing.PNG')
if x1 == 0.5 and enter1.keys != None:
    q=3
    print('selected tip text: spending')
    selectedTipImgLeft.setImage('spending.PNG')
    selectedTipImgRight.setImage('spending.PNG')
if keyResp1.keys == None and enter1.keys != None:
    q=1
thisExp.addData('Finance Tip Choice', keyResp1.keys)
thisExp.nextEntry()
if enter.keys in ['', [], None]:
    enter.keys = None
thisExp.addData('enter.keys',enter1.keys)
if enter.keys != None:
    thisExp.addData('enter.rt', enter1.rt)
thisExp.nextEntry()
routineTimer.reset()

instructionsFunc(instText2a)
instructionsFunc(instText2b)
instructionsFunc(instText3)


#begin typing for finance person
modify = False
typeFinNameClock = core.Clock()
finName = visual.TextStim(win=win, text='default text', height=0.1, color='white', pos=[0,-0.05], wrapWidth=1.2)
finName.text = ""
event.clearEvents('keyboard')
_enter_allKeys_ = []
typeFinNameComponents = [nameInstructions, enter, finName]
nameInstructions.setText("Think of the person who has been the most instrumental to your financial success.\n\nPlease type their name below, then press ENTER to continue:\n\n")
for thisComponent in typeFinNameComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
typeFinNameClock.reset(-_timeToFirstFrame)
frameN = -1

continueRoutine = True
while continueRoutine:
    t = typeFinNameClock.getTime()
    frameN = frameN + 1
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)
        win.callOnFlip(enter.clearEvents, eventType='keyboard')
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name
            enter.rt = _enter_allKeys[-1].rt
            continueRoutine = False
    if nameInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        nameInstructions.setAutoDraw(True)
    if t >= 0.0 and finName.status == NOT_STARTED:
        finName.tStart = t
        finName.frameNStart = frameN
        finName.setAutoDraw(True)

    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            finName.text = finName.text + ' '
        elif 'backspace' in keys:
            finName.text = finName.text[:-1]
        elif 'apostrophe' in keys:
            finName.text = finName.text + "'"
        elif 'lshift' in keys or 'rshift'  in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                finName.text = finName.text + keys[0].upper()
                modify = False
            else:
                finName.text = finName.text + keys[0]
    if finName.text == '' and enter.keys != None:
        continueRoutine = True
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in typeFinNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

# end typeFinName
for thisComponent in typeFinNameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:
    enter.keys = None
finName = finName.text
finNameStr = str(finName)
thisExp.addData('Finance Name', finNameStr)
thisExp.addData('enter.keys',enter.keys)
print("finance name: ", finNameStr)
thisExp.nextEntry()
routineTimer.reset()


#Begin name typing for friendName
typefriendNameClock=core.Clock()
event.clearEvents('keyboard')
_enter_allKeys_ = []
modify = False
friendName = visual.TextStim(win=win, text='default text', height=0.1, color='white', pos=[0,-0.05], wrapWidth=1.2)
friendName.text = ""

typefriendNameComponents = [enter, nameInstructions, friendName]
nameInstructions.setText("Think of the person you hang out with the most socially.\n\nPlease type their name below, then press ENTER to continue:")
for thisComponent in typefriendNameComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
typefriendNameClock.reset(-_timeToFirstFrame)
frameN = -1

continueRoutine = True
while continueRoutine:
    t = typefriendNameClock.getTime()
    frameN = frameN + 1
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)
        win.callOnFlip(enter.clearEvents, eventType='keyboard')
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name
            enter.rt = _enter_allKeys[-1].rt
            continueRoutine = False
    if nameInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        nameInstructions.setAutoDraw(True)
    if t >= 0.0 and friendName.status == NOT_STARTED:
        friendName.tStart = t
        friendName.frameNStart = frameN
        friendName.setAutoDraw(True)

    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            friendName.text = friendName.text + ' '
        elif 'backspace' in keys:
            friendName.text = friendName.text[:-1]
        elif 'apostrophe' in keys:
            friendName.text = friendName.text + "'"
        elif 'lshift' in keys or 'rshift'  in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                friendName.text = friendName.text + keys[0].upper()
                modify = False
            else:
                friendName.text = friendName.text + keys[0]

    if friendName.text == '' and enter.keys != None:
        continueRoutine = True
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in typefriendNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in typefriendNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

for thisComponent in typefriendNameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
thisExp.addData('Friend Name', friendName.text)
friendName = friendName.text
friendNameStr = str(friendName)
print("friend name: ", friendNameStr)
thisExp.nextEntry()
routineTimer.reset()

text1= 'The first run will begin momentarily....'
text2= 'The second run will begin momentarily...'
text3 = 'The third run will begin momentarily...'
text4 = 'The last run will begin momentarily...'

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


regCueStr = []
def getRandomFromBucket():
    randomIndex = random.choice(bucket)
    print("random index from bucket = ", randomIndex)
    if randomIndex == "a" or randomIndex =="b" or randomIndex =="c" or randomIndex =="d" or randomIndex=="e":
        regCue.setText(finNameStr)

    if randomIndex == "m" or randomIndex == "n" or randomIndex == "k" or randomIndex == "l" or randomIndex=="o":
        regCue.setText(friendNameStr)

    if randomIndex == "u" or randomIndex == "v" or randomIndex == "w" or randomIndex == "x" or randomIndex=="y" :
        regCue.setText("Choice")
        
    if randomIndex == "i" or randomIndex =="f"or randomIndex =="g"or randomIndex =="h" or randomIndex=="j":
        regCue.setText('High')

    if randomIndex == "z" or randomIndex == "za" or randomIndex == "zb" or randomIndex == "zc" or randomIndex=="zd":
        regCue.setText('Low')

    if randomIndex == "q" or randomIndex == "r" or randomIndex == "s" or randomIndex == "p" or randomIndex=="t" :
        regCue.setText("Unknown")

    bucket.remove(randomIndex)
    return regCueStr
    print(regCueStr)
    print(bucket)

instructionsFunc(instText4)


#instruction with color text loop
primeText = ["During the blocks in which you're presented with one of the names you typed, \n\n\n\nPress 1 to continue.", "During the blocks in which you're presented with the word 'High',\n\n\n\nPress 1 to continue.", \
    "During the blocks in which you're presented with the word 'Low',\n\n\n\nPress 1 to continue.", "During the blocks in which you're presented with the word 'Unknown', \n\n\n\nPress 1 to continue.", \
    "During the blocks in which you see the word 'Choice',\n\n\n\nPress 1 to continue."]
imagineText = ['please make your decisions while imagining that person is in the room with you.', 'please make your decisions while considering that these trials have a high probability of being selected.', 'please make your decisions while considering that these trials have a low probability of being selected.', \
    'please make your decisions while considering that the probability of selecting one of these trials is unknown.', 'please make your decisions as you normally would, without any additional considerations.']
colorText = ['lightcoral', 'lightgreen', 'skyblue', 'orchid', 'gold']

for (a, b, c) in zip(primeText, imagineText, colorText):
    continueRoutine = True
    space.keys = []
    space.rt = []
    _space_allKeys = []
    trialClock=core.Clock()
    trialComponents = [inst5A, inst5B, space]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if inst5A.status == NOT_STARTED:
            inst5A.setAutoDraw(True)
            inst5A.setText(b)
            inst5A.setColor(c)
        if inst5B.status == NOT_STARTED:
            inst5B.setAutoDraw(True)
            inst5B.setText(a)
        waitOnFlip = False
        if space.status == NOT_STARTED:
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
                continueRoutine = False
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
    if space.keys in ['', [], None]:
        space.keys = None
    routineTimer.reset()
    thisExp.nextEntry()

#last bit of instructions
instructionsFunc(instText5)

choiceResp = keyboard.Keyboard()
CueClock = core.Clock()
blank.setText("")
#offsetTime=[]
def choiceTrials():
    
    # trials components
    continueRoutine = True
    routineTimer.add(6.000)
    ChoiceClock=core.Clock()
    randomString=[]
    selectedVidStr = str(selectedVid)
    selectedTipStr = str(selectedTips)
    choiceSelection.keys = []
    choiceSelection.rt = []
    _choiceSelection_allKeys = []
    choiceOffsetTime=[]
    offsetTime=[]
    button_resp.oldButtonState = button_resp.device.getAllButtons()[:]
    button_resp.keys = []
    button_resp.rt = []
    buttonPressTime=[]
    andSignLeft.setText('+')
    andSignRight.setText('+')
    blank.setText('')
    MoreGameAmt1 = MoreGameAmt
    MoreQuestionAmt1 = MoreQuestionAmt
    LessGameAmt1 = LessGameAmt
    LessQuestionAmt1 = LessQuestionAmt
    topRightTime.setText(MoreGame)
    topLeftTime.setText(LessGame)
    botLeftTime.setText(MoreQuestion)
    botRightTime.setText(LessQuestion)
    if v == 1:
        selectedVidImgLeft.setImage("comedy.PNG")
        selectedVidImgRight.setImage("comedy.PNG")
        topRightText.setText("Comedy Videos")
        topLeftText.setText("Comedy Videos")
    if v == 3:
        selectedVidImgLeft.setImage("music.PNG")
        selectedVidImgRight.setImage("music.PNG")
        topRightText.setText("Music Videos")
        topLeftText.setText("Music Videos")
    if v == 2:
        selectedVidImgLeft.setImage("gaming.PNG")
        selectedVidImgRight.setImage("gaming.PNG")
        topRightText.setText("Gaming Videos")
        topLeftText.setText("Gaming Videos")
    if q == 1:
        selectedTipImgLeft.setImage("spending.PNG")
        selectedTipImgRight.setImage("spending.PNG")
        botRightText.setText("Spending Tips")
        botLeftText.setText("Spending Tips")
    if q == 2:
        selectedTipImgLeft.setImage("saving.PNG")
        selectedTipImgRight.setImage("saving.PNG")
        botRightText.setText("Saving Tips")
        botLeftText.setText("Saving Tips")
    if  q == 3:
        selectedTipImgRight.setImage("investing.PNG")
        selectedTipImgLeft.setImage("investing.PNG")
        botRightText.setText("Investing Tips")
        botLeftText.setText("Investing Tips")

    trialComponents = [andSignLeft, andSignRight, button_resp, selectedVidImgLeft, lineStim, selectedVidImgRight, selectedTipImgLeft, selectedTipImgRight, topLeftText, topLeftTime, topRightText, topRightTime, botLeftText, botLeftTime, botRightText, botRightTime, blank]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)
    frameN = -1

    # begin trial
    while continueRoutine and routineTimer.getTime() > 0:
        t = ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if lineStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            lineStim.frameNStart = frameN
            lineStim.tStart = t
            lineStim.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(lineStim, 'tStartRefresh')
            lineStim.setAutoDraw(True)
        if lineStim.status == STARTED:
            if tThisFlipGlobal > lineStim.tStartRefresh + 6.0-frameTolerance:
                lineStim.tStop = t
                lineStim.frameNStop = frameN
                win.timeOnFlip(lineStim, 'tStopRefresh')
                lineStim.setAutoDraw(False)
        if botLeftTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            botLeftTime.frameNStart = frameN
            botLeftTime.tStart = t
            botLeftTime.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(botLeftTime, 'tStartRefresh')
            botLeftTime.setAutoDraw(True)
        if botLeftTime.status == STARTED:
            if tThisFlipGlobal > botLeftTime.tStartRefresh + 6.0-frameTolerance:
                botLeftTime.tStop = t
                botLeftTime.frameNStop = frameN
                win.timeOnFlip(botLeftTime, 'tStopRefresh')
                botLeftTime.setAutoDraw(False)

        if botRightTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            botRightTime.frameNStart = frameN
            botRightTime.tStart = t
            botRightTime.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(botRightTime, 'tStartRefresh')
            botRightTime.setAutoDraw(True)
        if botRightTime.status == STARTED:
            if tThisFlipGlobal > botRightTime.tStartRefresh + 6.0-frameTolerance:
                botRightTime.tStop = t
                botRightTime.frameNStop = frameN
                win.timeOnFlip(botRightTime, 'tStopRefresh')
                botRightTime.setAutoDraw(False)

        if topRightTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            topRightTime.frameNStart = frameN
            topRightTime.tStart = t
            topRightTime.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(topRightTime, 'tStartRefresh')
            topRightTime.setAutoDraw(True)
        if topRightTime.status == STARTED:
            if tThisFlipGlobal > topRightTime.tStartRefresh + 6.0-frameTolerance:
                topRightTime.tStop = t
                topRightTime.frameNStop = frameN
                win.timeOnFlip(topRightTime, 'tStopRefresh')
                topRightTime.setAutoDraw(False)

        if topLeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            topLeftText.frameNStart = frameN
            topLeftText.tStart = t
            topLeftText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(topLeftText, 'tStartRefresh')
            topLeftText.setAutoDraw(True)
        if topLeftText.status == STARTED:
            if tThisFlipGlobal > topLeftText.tStartRefresh + 6.0-frameTolerance:
                topLeftText.tStop = t
                topLeftText.frameNStop = frameN
                win.timeOnFlip(topLeftText, 'tStopRefresh')
                topLeftText.setAutoDraw(False)

        if topRightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            topRightText.frameNStart = frameN
            topRightText.tStart = t
            topRightText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(topRightText, 'tStartRefresh')
            topRightText.setAutoDraw(True)
        if topRightText.status == STARTED:
            if tThisFlipGlobal > topRightText.tStartRefresh + 6.0-frameTolerance:
                topRightText.tStop = t
                topRightText.frameNStop = frameN
                win.timeOnFlip(topRightText, 'tStopRefresh')
                topRightText.setAutoDraw(False)

        if botLeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:

            botLeftText.frameNStart = frameN
            botLeftText.tStart = t
            botLeftText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(botLeftText, 'tStartRefresh')
            botLeftText.setAutoDraw(True)
        if botLeftText.status == STARTED:
            if tThisFlipGlobal > botLeftText.tStartRefresh + 6.0-frameTolerance:
                botLeftText.tStop = t
                botLeftText.frameNStop = frameN
                win.timeOnFlip(botLeftText, 'tStopRefresh')
                botLeftText.setAutoDraw(False)

        if botRightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            botRightText.frameNStart = frameN
            botRightText.tStart = t
            botRightText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(botRightText, 'tStartRefresh')
            botRightText.setAutoDraw(True)
        if botRightText.status == STARTED:
            if tThisFlipGlobal > botRightText.tStartRefresh + 6.0-frameTolerance:
                botRightText.tStop = t
                offsetTime = globalClock.getTime()
                botRightText.frameNStop = frameN
                win.timeOnFlip(botRightText, 'tStopRefresh')
                botRightText.setAutoDraw(False)

        if topLeftTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            topLeftTime.frameNStart = frameN
            topLeftTime.tStart = t
            topLeftTime.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(topLeftTime, 'tStartRefresh')
            topLeftTime.setAutoDraw(True)
        if topLeftTime.status == STARTED:
            if tThisFlipGlobal > topLeftTime.tStartRefresh + 6.0-frameTolerance:
                topLeftTime.tStop = t
                topLeftTime.frameNStop = frameN
                win.timeOnFlip(topLeftTime, 'tStopRefresh')
                topLeftTime.setAutoDraw(False)

        if selectedVidImgLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            selectedVidImgLeft.frameNStart = frameN
            selectedVidImgLeft.tStart = t
            selectedVidImgLeft.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(selectedVidImgLeft, 'tStartRefresh')
            selectedVidImgLeft.setAutoDraw(True)
        if selectedVidImgLeft.status == STARTED:
            if tThisFlipGlobal > selectedVidImgLeft.tStartRefresh + 6.0-frameTolerance:
                selectedVidImgLeft.tStop = t
                selectedVidImgLeft.frameNStop = frameN
                win.timeOnFlip(selectedVidImgLeft, 'tStopRefresh')
                selectedVidImgLeft.setAutoDraw(False)

        if selectedVidImgRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            selectedVidImgRight.frameNStart = frameN
            selectedVidImgRight.tStart = t
            selectedVidImgRight.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(selectedVidImgRight, 'tStartRefresh')
            selectedVidImgRight.setAutoDraw(True)
        if selectedVidImgRight.status == STARTED:
            if tThisFlipGlobal > selectedVidImgRight.tStartRefresh + 6.0-frameTolerance:
                selectedVidImgRight.tStop = t
                selectedVidImgRight.frameNStop = frameN
                win.timeOnFlip(selectedVidImgRight, 'tStopRefresh')
                selectedVidImgRight.setAutoDraw(False)

        if selectedTipImgLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            selectedTipImgLeft.frameNStart = frameN
            selectedTipImgLeft.tStart = t
            selectedTipImgLeft.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(selectedTipImgLeft, 'tStartRefresh')
            selectedTipImgLeft.setAutoDraw(True)
        if selectedTipImgLeft.status == STARTED:
            if tThisFlipGlobal > selectedTipImgLeft.tStartRefresh + 6.0-frameTolerance:
                selectedTipImgLeft.tStop = t
                selectedTipImgLeft.frameNStop = frameN
                win.timeOnFlip(selectedTipImgLeft, 'tStopRefresh')
                selectedTipImgLeft.setAutoDraw(False)

        if selectedTipImgRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            selectedTipImgRight.frameNStart = frameN
            selectedTipImgRight.tStart = t
            selectedTipImgRight.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(selectedTipImgRight, 'tStartRefresh')
            selectedTipImgRight.setAutoDraw(True)
        if selectedTipImgRight.status == STARTED:
            if tThisFlipGlobal > selectedTipImgRight.tStartRefresh + 6.0-frameTolerance:
                selectedTipImgRight.tStop = t
                selectedTipImgRight.frameNStop = frameN
                win.timeOnFlip(selectedTipImgRight, 'tStopRefresh')
                selectedTipImgRight.setAutoDraw(False)

        waitOnFlip = False
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
                button_resp.newPressedButtons = [i for i in [1,2] if i in button_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(button_resp.device_number,i)) for i in button_resp.pressedButtons]
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:  
                button_resp.keys = theseKeys[-1] 
                button_resp.rt = button_resp.clock.getTime()
                buttonPressTime = globalClock.getTime()
#                continueRoutine = False


        if andSignLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            andSignLeft.frameNStart = frameN
            andSignLeft.tStart = t
            andSignLeft.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(andSignLeft, 'tStartRefresh')
            andSignLeft.setAutoDraw(True)
        if andSignLeft.status == STARTED:
            if tThisFlipGlobal > andSignLeft.tStartRefresh + 6.0-frameTolerance:
                andSignLeft.tStop = t
                andSignLeft.frameNStop = frameN
                win.timeOnFlip(andSignLeft, 'tStopRefresh')
                andSignLeft.setAutoDraw(False)

        if andSignRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            andSignRight.frameNStart = frameN
            andSignRight.tStart = t
            andSignRight.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(andSignRight, 'tStartRefresh')
            andSignRight.setAutoDraw(True)
        if andSignRight.status == STARTED:
            if tThisFlipGlobal > andSignRight.tStartRefresh + 6.0-frameTolerance:
                andSignRight.tStop = t
                andSignRight.frameNStop = frameN
                win.timeOnFlip(andSignRight, 'tStopRefresh')
                andSignRight.setAutoDraw(False)

        if andSignLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            andSignLeft.frameNStart = frameN
            andSignLeft.tStart = t
            andSignLeft.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(andSignLeft, 'tStartRefresh')
            andSignLeft.setAutoDraw(True)
        if andSignLeft.status == STARTED:
            if tThisFlipGlobal > andSignLeft.tStartRefresh + 6.0-frameTolerance:
                andSignLeft.tStop = t
                andSignLeft.frameNStop = frameN
                win.timeOnFlip(andSignLeft, 'tStopRefresh')
                andSignLeft.setAutoDraw(False)
        if andSignRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            andSignRight.frameNStart = frameN
            andSignRight.tStart = t
            andSignRight.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(andSignRight, 'tStartRefresh')
            andSignRight.setAutoDraw(True)
        if andSignRight.status == STARTED:
            if tThisFlipGlobal > andSignRight.tStartRefresh + 6.0-frameTolerance:
                andSignRight.tStop = t
                andSignRight.frameNStop = frameN
                win.timeOnFlip(andSignRight, 'tStopRefresh')
                andSignRight.setAutoDraw(False)
                offsetTime = globalClock.getTime()

        if button_resp.keys == 1:
            randomString = "favoredTips"
        if button_resp.keys == 2:
            randomString  = "favoredVideo"

        if button_resp.keys == 1:
            topLeftText.setColor('green')
            topLeftTime.setColor('green')
            botLeftText.setColor('green')
            botLeftTime.setColor('green')
            andSignLeft.setColor("green")
            choiceSelection.status = FINISHED

        if button_resp.keys == 2:
            topRightText.setColor('green')
            topRightTime.setColor('green')
            botRightText.setColor('green')
            botRightTime.setColor('green')
            andSignRight.setColor("green")
            button_resp.status = FINISHED
        if button_resp.keys == 2 or button_resp.keys == 1:
            button_resp.status = FINISHED
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        offsetTime=topRightTime.tStartRefresh + ChoiceClock.getTime()
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    # end routine in inner loop
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('regCue', regCue.text)

    thisExp.addData("Random String", randomString)
    # check responses
    if button_resp.keys in ['', [], None]:
        button_resp.keys = None
    thisExp.addData('choiceSelection.keys',button_resp.keys)
    if button_resp.keys != None:
        thisExp.addData('choiceSelection.rt', button_resp.rt)
    thisExp.addData("Choice Button Press Time", buttonPressTime)
    thisExp.addData("choiceSelection Onset", button_resp.tStartRefresh)
    thisExp.addData('choiceSelection Offset', choiceOffsetTime)
    if randomString == "favoredTips":
        selectedTipTime.append(MoreQuestionAmt1)
        selectedVidTime.append(LessGameAmt1)
    if randomString == "favoredVideo":
        selectedTipTime.append(LessQuestionAmt1)
        selectedVidTime.append(MoreGameAmt1)
    topRightText.setColor('white')
    topRightTime.setColor('white')
    botRightText.setColor('white')
    botRightTime.setColor('white')
    topLeftText.setColor('white')
    topLeftTime.setColor('white')
    botLeftText.setColor('white')
    botLeftTime.setColor('white')
    andSignLeft.setColor('white')
    andSignRight.setColor('white')
#    lineStim.setAutoDraw(False)
    thisExp.addData("All Stimuli Onset", topRightTime.tStartRefresh)
    thisExp.addData('All Stimuli Offset', globalClock.getTime())
    routineTimer.reset()


MainLoop = data.TrialHandler(nReps=1.0, method='random', extraInfo=expInfo, originPath=-1, trialList=None)
thisExp.addLoop(MainLoop)
thisMainLoop = MainLoop.trialList[0]
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in MainLoop:
    currentLoop = MainLoop
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    if not bucket:
        MainLoop.finished=True
        MainLoop.finished=True
    continueRoutine = True
    trialInstFunc(text1)
    itiFunc()
    trials_1 = data.TrialHandler(nReps=1.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Rows.csv'),
        seed=None, name='trials_1')
    thisExp.addLoop(trials_1)
    thisTrial_1 = trials_1.trialList[0]
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))

    for thisTrial_1 in trials_1:
        currentLoop = trials_1
        if thisTrial_1 != None:
            for paramName in thisTrial_1:
                exec('{} = thisTrial_1[paramName]'.format(paramName))


        trials = data.TrialHandler(nReps=1.0, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('TimeDivisions.csv', selection=Rows),
            seed=None, name='trials')
        thisExp.addLoop(trials)
        thisTrial = trials.trialList[0]
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        if not bucket:
            trials.finished=True
            trials_1.finished=True
            continueRoutine = False
        for thisTrial in trials:
            currentLoop = trials
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            continueRoutine = True

            isiFunc()
            getRandomFromBucket()
            print(bucket)
            print("regcue string=", regCue.text)
            cueScreenFunc(regCue.text)
            isiFunc()
            choiceTrials()
            continueRoutine = True
            isiFunc()
            thisExp.nextEntry()
        itiFunc()
    trialInstFunc(text2)
    itiFunc()
    trials_2 = data.TrialHandler(nReps=1.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Rows2.csv'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)
    thisTrial_2 = trials_2.trialList[0]
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))

        trials2 = data.TrialHandler(nReps=1.0, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('TimeDivisions.csv', selection=Rows2),
            seed=None, name='trials2')
        thisExp.addLoop(trials2)
        thisTrial2 = trials2.trialList[0]
        if thisTrial2 != None:
            for paramName in thisTrial2:
                exec('{} = thisTrial2[paramName]'.format(paramName))
        if not bucket:
            trials2.finished=True
            trials_2.finished=True    
        for thisTrial2 in trials2:
            currentLoop = trials2
            if thisTrial2 != None:
                for paramName in thisTrial2:
                    exec('{} = thisTrial2[paramName]'.format(paramName))
            continueRoutine = True
            isiFunc()            
            getRandomFromBucket()
            print(bucket)
            print("regcue string=", regCue.text)
            cueScreenFunc(regCue.text)
            isiFunc()
            choiceTrials()
            continueRoutine = True
            isiFunc()
            thisExp.nextEntry()
#
#    #        if not bucket:
#    #            trials.finished=True
#    #            trials_2.finished=True
#        if not bucket:
#            trials2.finished=True
#            trials_2.finished=True
#        thisExp.nextEntry()
        itiFunc()
    trialInstFunc(text3)
    itiFunc()
    trials_3 = data.TrialHandler(nReps=1.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Rows3.csv'),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)
    thisTrial_3 = trials_3.trialList[0]
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))

    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))


        trials3 = data.TrialHandler(nReps=1.0, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('TimeDivisions.csv', selection=Rows3),
            seed=None, name='trials3')
        thisExp.addLoop(trials3)
        thisTrial3 = trials3.trialList[0]
        if thisTrial3 != None:
            for paramName in thisTrial3:
                exec('{} = thisTrial[paramName]'.format(paramName))
        if not bucket:
            trials3.finished=True
            trials_3.finished=True
        for thisTrial3 in trials3:
            currentLoop = trials3
            if thisTrial3 != None:
                for paramName in thisTrial3:
                    exec('{} = thisTrial3[paramName]'.format(paramName))
            continueRoutine = True
            isiFunc()
            getRandomFromBucket()
            print(bucket)
            print("regcue string=", regCue.text)
            cueScreenFunc(regCue.text)
            isiFunc()
            choiceTrials()
            # isi
            continueRoutine = True
            isiFunc()
            thisExp.nextEntry()
        itiFunc()
    trialInstFunc(text4)
    itiFunc()
    trials_4 = data.TrialHandler(nReps=1.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Rows4.csv'),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)
    thisTrial_4 = trials_4.trialList[0]
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))

    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))


        trials4 = data.TrialHandler(nReps=1.0, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('TimeDivisions.csv', selection=Rows4),
            seed=None, name='trials4')
        thisExp.addLoop(trials4)
        thisTrial4 = trials4.trialList[0]
        if thisTrial4 != None:
            for paramName in thisTrial4:
                exec('{} = thisTrial[paramName]'.format(paramName))
        if not bucket:
            trials4.finished=True
            trials_4.finished=True
        for thisTrial4 in trials4:
            currentLoop = trials4
            if thisTrial4 != None:
                for paramName in thisTrial4:
                    exec('{} = thisTrial4[paramName]'.format(paramName))
            continueRoutine = True
            isiFunc()
            getRandomFromBucket()
            print(bucket)
            print("regcue string=", regCue.text)
            cueScreenFunc(regCue.text)
            isiFunc()
            choiceTrials()
            # isi
            continueRoutine = True
            isiFunc()
            thisExp.nextEntry()
        itiFunc()
    #        if not bucket:
    #            trials.finished=True
    #            trials_2.finished=True
    if not bucket:
        MainLoop.finished=True
        MainLoop.finished=True
    thisExp.nextEntry()


#ADD ENDING TEXT!!!!
endComponents = []
endClock= core.Clock()
continueRoutine = True
enter.keys = []
enter.rt = []
_enter_allKeys = []
randomVidTime = random.choice(selectedVidTime)
randomVidTime = int(randomVidTime)
randomTipTime = (20 - randomVidTime)
randomTipTimeStr = str(randomTipTime)
randomVidTimeStr = str(randomVidTime)

print("Random Vid Time String :", randomVidTimeStr)
print("Random Tip Time String :", randomTipTimeStr)
print("The trial randomly selected your choice to watch the video for ", randomVidTimeStr, "minutes, and to read financial tips for ", randomTipTimeStr)
endText.setText("Thank you for participating! \n\n One trial was selected at random, and in that trial you chose to allot the 20 minutes as: \n\n" + randomVidTimeStr + " minutes watching the videos, and \n\n" + randomTipTimeStr + " minutes reading financial tips.\n\n You will be reminded of this allotment at the end of the study, when you will be prompted to complete these activities. For now, please press ENTER to continue with the study." )

endComponents = [endText, enter]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)
frameN = -1
while continueRoutine:
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        endText.frameNStart = frameN
        endText.tStart = t
        endText.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(endText, 'tStartRefresh')
        endText.setAutoDraw(True)
        endText.setText("Thank you for participating! \n\n One trial was selected at random, and in that trial you chose to allot the 20 minutes as: \n\n" + randomVidTimeStr + " minutes watching the videos, and \n\n" + randomTipTimeStr + " minutes reading financial tips.\n\n You will be reminded of this allotment at the end of the study, when you will be prompted to complete these activities." )
    waitOnFlip = False
    if enter.status == NOT_STARTED:
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)
        win.callOnFlip(enter.clearEvents, eventType='keyboard')
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name
            enter.rt = _enter_allKeys[-1].rt
            continueRoutine = False
    if enter.keys == 'return':
        continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()
#end routine
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:
    enter.keys = None
thisExp.nextEntry()
routineTimer.reset()

win.flip()

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
