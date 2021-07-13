#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys

from psychopy.hardware import keyboard
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '2021.1.2'
expName = 'SlotMachTest'
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
    originPath='C:\\Users\\joann\\Downloads\\Self-Regulation-Psychopy-Files-master\\Self-Regulation-Psychopy-Files-master\\Slot MachineTask\\SlotMachTest.py',
    savePickle=True, saveWideText=True, dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001


win = visual.Window(size=(1024, 768), fullscr=True, screen=0,winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True,units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0 

defaultKeyboard = keyboard.Keyboard()

InstrClock = core.Clock()
Instructions = visual.TextStim(win=win, text='',pos=[0,0], height=1.0, wrapWidth=1.5,color='white');
space = keyboard.Keyboard()
import numpy
from numpy import random

earnings = 0
earningsStr = "$" + '%.2f' % earnings

subID = int(expInfo['Participant*'])

FiftyGamble = [1,0]
SixtyGamble = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
ThirtyGamble = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

earning=0
chosenMoney = 0


#probability =[]
def gamProbability(gamProb):
    probs = int(gamProb)
    if probs == 65:
        probability = SixtyGamble
        print('65% gamble')
    if probs == 35:
        probability = ThirtyGamble
        print('35% gamble')
    if probs == 50:
        probability = FiftyGamble
        print('50% gamble')
def gambleFunc(gamProb):
    probs = int(gamProb)
    if probs == 65:
        probability = SixtyGamble
        #print('65% gamble')
    if probs == 35:
        probability = ThirtyGamble
        print('35% gamble')
    if probs == 50:
        probability = FiftyGamble
        print('50% gamble')
    result = random.choice(probability)
    print('gamble result:')
    print(result)

def loseFunc(chosenMoney, earning):
    earning -= chosenMoney
    print('Lost Money earnings:')
    print(earning)
def winFunc(chosenMoney, earning):
    earning += chosenMoney
    print('Won money earnings:')
    print(earning)

def earningsFunct(gamProb, chosenMoney, WinLossType, earning):
   if subID%2==0:   #gambles are on left side of screen
       if choice.keys == '1' and WinLossType== 1 :
           print('gambled during win condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
               print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)
           if result == 1:   #win
               earning += chosenMoney
               print('Won money earnings:')
               print(earning)
       #    if result == 0: #lose
        #       earnings += 0

       if choice.keys == '1' and WinLossType==0:
           print('gambled during lose condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
        #print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)
           if result == 1: #lose
               earning -= chosenMoney
               print('Lost Money earnings:')
               print(earning)
     #      if result == 0: #win
     #          earnings += 0

       if choice.keys == '2'and WinLossType ==1:
           print('did not gamble for win')
           earning += chosenMoney
           print('Won money earnings:')
           print(earning)
       if choice.keys == '2' and WinLossType == 0:
           print('did not gamble for loss')
           earning -= chosenMoney
           print('Lost Money earnings:')
           print(earning)


   if subID%2==1:  #gambles are on right side of scree
       if choice.keys == '2' and WinLossType == 1:
           print('gambled during win condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
               print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)
           if result == 1: #win
               winFunc(chosenMoney, earning)
    #       if result == 0: #lost
    #           earnings += 0


       if choice.keys == '2' and WinLossType == 0:
           print('gambled during lose condition')
           #gamProbability(gamProb)
           probs = int(gamProb)
           if probs == 65:
               probability = SixtyGamble
               print('65% gamble')
           if probs == 35:
               probability = ThirtyGamble
               print('35% gamble')
           if probs == 50:
               probability = FiftyGamble
               print('50% gamble')
           result = random.choice(probability)
           print('gamble result:')
           print(result)
           if result == 1: #lose
               earning -= chosenMoney
               print('Lost Money earnings:')
               print(earning)
     #      if result == 0: #win
     #          earnings += 0

       if choice.keys == '1' and WinLossType == 1:
           print('did not gamble for win')
           earning += chosenMoney
           print('Won money earnings:')
           print(earning)
       if choice.keys == '1' and WinLossType == 0:
           print('did not gamble for lose condition')
           earning -= chosenMoney
           print('Lost Money earnings:')
           print(earning)

enter = keyboard.Keyboard()
inst3Clock = core.Clock()
text_4 = visual.TextStim(win=win,
    text='You will have four seconds to make your choice upon seeing the options. \n\nTo choose the option on the left, press "1". To choose the option on the right, press "2".\n\nYou will first be playing some practice rounds. To begin the practice, press ENTER!',
    font='Arial', pos=(0, 0), height=0.045, wrapWidth=1.4, color='white');
key_resp_2 = keyboard.Keyboard()
ISIClock = core.Clock()
PracticeCueClock = core.Clock()
text = visual.TextStim(win=win,text='EMPHASIZE',font='Arial', pos=(0, 0), height=0.12,color='white', depth=0.0);
isi_text = visual.TextStim(win=win, text='+',font='Arial', pos=(0, 0), height=0.13, color='white');

PracticeClock = core.Clock()
Line = visual.Line(win=win, name='Line',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=90, pos=(0, 0), lineWidth=1.0,  colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
choice = keyboard.Keyboard()
GambleAmt = visual.TextStim(win=win,text=None,font='Arial', pos=[0,0], height=1.0, color='white');
SureAmt = visual.TextStim(win=win, text=None,font='Arial', pos=[0,0], height=1.0, color='white', colorSpace='rgb', depth=-3.0);
GambleProb = visual.TextStim(win=win, text=None,font='Arial',pos=[0,0], height=1.0, color='white');
SureProb = visual.TextStim(win=win, text=None,font='Arial',pos=[0,0], height=1.0,color='white');
blank = visual.TextStim(win=win, text=None,font='Arial',pos=(0, 0), height=0.1, color='white');
moneyBank = visual.Rect(
    win=win, width=(0.46, 0.24)[0], height=(0.46, 0.24)[1],
    ori=0, pos=(0.68, -0.42), lineWidth=8, colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=None,
    opacity=1, depth=-8.0, interpolate=True)
earningsText = visual.TextStim(win=win, text='',font='Arial', pos=(0.64, -0.42), height=0.09, color='white');
FeedbackClock = core.Clock()
text_3 = visual.TextStim(win=win, text='', font='Arial', pos=(0, 0), height=0.09, wrapWidth=1.4,color='white');

BeginInstClock = core.Clock()
text_2 = visual.TextStim(win=win,
    text='You will now be completing the full task. Your money bank will begin with the $4.00 you earned from the card task\n\nPress SPACE to start!',
    font='Arial', pos=(0, 0), height=0.085, wrapWidth=1.4, ori=0,color='white');
key_resp = keyboard.Keyboard()

CueClock = core.Clock()
cue = visual.TextStim(win=win, text='',font='Arial', pos=(0, 0), height=0.12, color='white');

PracticeClock = core.Clock()
GambleAmt = visual.TextStim(win=win,text=None,font='Arial',pos=[0,0], height=1.0,color='white');
SureAmt = visual.TextStim(win=win,text=None,font='Arial',pos=[0,0], height=1.0, color='white');
GambleProb = visual.TextStim(win=win,text=None,font='Arial',pos=[0,0], height=1.0, color='white');
SureProb = visual.TextStim(win=win,text=None,font='Arial',pos=[0,0], height=1.0, color='white');
moneyBank = visual.Rect(
    win=win, width=(0.46, 0.24)[0], height=(0.46, 0.24)[1],
    ori=0, pos=(0.68, -0.42), lineWidth=8,  colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=None,
    opacity=1, depth=-8.0, interpolate=True)
earningsText = visual.TextStim(win=win, text='',font='Arial',pos=(0.64, -0.42), height=0.09,color='white');

FeedbackClock = core.Clock()
text_3 = visual.TextStim(win=win,text='',font='Arial', pos=(0, 0), height=0.09, wrapWidth=1.4,color='white');

ThankYouClock = core.Clock()
tyText = visual.TextStim(win=win, text=None,font='Arial', pos=(0, 0), height=0.1, color='white');

globalClock = core.Clock()
routineTimer = core.CountdownTimer()

#begin instr
continueRoutine = True
Instructions.setColor('white', colorSpace='rgb')
Instructions.setPos((0, 0))
Instructions.setText('In this part of the study, you will be making a series of monetary decisions.\n\nYou will have the choice between taking a gamble or choosing a sure option. For each gamble, you will have a chance of either winning money, losing money, or gaining nothing, while the sure option guarantees a win or loss. \n\nPress SPACE to continue. ')
Instructions.setFont('Arial')
Instructions.setHeight(0.045)
space.keys = []
space.rt = []
_space_allKeys = []
InstrComponents = [Instructions, space]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)
frameN = -1

def isiFunc(time):
    continueRoutine = True
    routineTimer.add(time)
    isi_text.setText('+')
    ISIComponents = [isi_text]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine and routineTimer.getTime() > 0:
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if isi_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            isi_text.frameNStart = frameN
            isi_text.tStart = t
            isi_text.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(isi_text, 'tStartRefresh')
            isi_text.setAutoDraw(True)
        if isi_text.status == STARTED:
            if tThisFlipGlobal > isi_text.tStartRefresh + time-frameTolerance:
                isi_text.tStop = t
                isi_text.frameNStop = frameN
                win.timeOnFlip(isi_text, 'tStopRefresh')
                isi_text.setAutoDraw(False)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('isi_text.started', isi_text.tStartRefresh)
    thisExp.addData('isi_text.stopped', isi_text.tStopRefresh)

#every frame instr
while continueRoutine:
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        Instructions.frameNStart = frameN
        Instructions.tStart = t
        Instructions.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(Instructions, 'tStartRefresh')
        Instructions.setAutoDraw(True)
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
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

# end Instr
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
if space.keys in ['', [], None]:
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()

#begin inst2
continueRoutine = True
enter.keys = []
enter.rt = []
_enter_allKeys = []

# begin inst3
continueRoutine = True
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
inst3Components = [text_4, key_resp_2]
for thisComponent in inst3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst3Clock.reset(-_timeToFirstFrame)
frameN = -1

# every frame inst3
while continueRoutine:
    t = inst3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        text_4.frameNStart = frameN
        text_4.tStart = t
        text_4.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(text_4, 'tStartRefresh')
        text_4.setAutoDraw(True)
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        key_resp_2.frameNStart = frameN
        key_resp_2.tStart = t
        key_resp_2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(key_resp_2, 'tStartRefresh')
        key_resp_2.status = STARTED
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in inst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()

#end inst3
for thisComponent in inst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
if key_resp_2.keys in ['', [], None]:
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()

# begin isi
isiFunc(2.000)

PracticeLoop = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeSlotMach_Localizer.xlsx', selection='0:3'),
    seed=None, name='PracticeLoop')
thisExp.addLoop(PracticeLoop)
thisPracticeLoop = PracticeLoop.trialList[0]
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in PracticeLoop:
    currentLoop = PracticeLoop
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))

    #begin isi
    isiFunc(2.000)
    
    # begin Practice
    continueRoutine = True
    Line.setFillColor([-1.000,-1.000,-1.000])
    Line.setSize((3, 0.5))
    Line.setLineColor([-1.000,-1.000,-1.000])
    Line.setLineWidth(7)
    choice.keys = []
    choice.rt = []
    _choice_allKeys = []
    GambleAmt.setColor('white', colorSpace='rgb')
    GambleAmt.setPos((-0.41, -0.1))
    GambleAmt.setText('')
    GambleAmt.setFont('Arial')
    GambleAmt.setHeight(0.11)
    SureAmt.setColor('white', colorSpace='rgb')
    SureAmt.setPos((0.41, -0.1))
    SureAmt.setText('')
    SureAmt.setFont('Arial')
    SureAmt.setHeight(0.11)
    GambleProb.setColor('white', colorSpace='rgb')
    GambleProb.setPos((-0.41, 0.3))
    GambleProb.setText('')
    GambleProb.setFont('Arial')
    GambleProb.setHeight(0.13)
    SureProb.setColor('white', colorSpace='rgb')
    SureProb.setPos((0.41, 0.3))
    SureProb.setText('')
    SureProb.setFont('Arial')
    SureProb.setHeight(0.13)
    feedbackVar = []
    leftVarText=[]
    leftVarMoney = []
    rightVarText = []
    rightVarMoney = []
    result = []

    if subID%2 == 1 :
        leftVarText = (gambleWinLoss)
        leftVarMoney = (gamble)
        rightVarText = (sureWinLoss)
        rightVarMoney = (sure)
    if subID%2 == 0:
        rightVarText= (gambleWinLoss)
        rightVarMoney= (gamble)
        leftVarText= (sureWinLoss)
        leftVarMoney= (sure)

    GambleAmtVar = "$" + '%.2f' % leftVarMoney
    GambleAmt.setText(GambleAmtVar)
    SureAmtVar = "$" + '%.2f' % rightVarMoney
    SureAmt.setText(SureAmtVar)
    GambleProb.setText(leftVarText)
    SureProb.setText(rightVarText)

    leftMoney = float(leftVarMoney)
    rightMoney = float(rightVarMoney)
    WinLossType = int(WinLossCode)


    blank.setText('')
    earningsText.setText(earningsStr)
    PracticeComponents = [Line, choice, GambleAmt, SureAmt, GambleProb, SureProb, blank, moneyBank, earningsText]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeClock.reset(-_timeToFirstFrame)
    frameN = -1

    # -------Run Routine "Practice"-------
    while continueRoutine:
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if Line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            Line.frameNStart = frameN
            Line.tStart = t
            Line.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(Line, 'tStartRefresh')
            Line.setAutoDraw(True)
        if Line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Line.tStartRefresh + 4-frameTolerance:
                Line.tStop = t
                Line.frameNStop = frameN
                win.timeOnFlip(Line, 'tStopRefresh')
                Line.setAutoDraw(False)

        waitOnFlip = False
        if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            choice.frameNStart = frameN
            choice.tStart = t
            choice.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(choice, 'tStartRefresh')
            choice.status = STARTED
            waitOnFlip = True
            win.callOnFlip(choice.clock.reset)
            win.callOnFlip(choice.clearEvents, eventType='keyboard')
        if choice.status == STARTED:
            if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                choice.tStop = t
                choice.frameNStop = frameN
                win.timeOnFlip(choice, 'tStopRefresh')
                choice.status = FINISHED
        if choice.status == STARTED and not waitOnFlip:
            theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
            _choice_allKeys.extend(theseKeys)
            if len(_choice_allKeys):
                choice.keys = _choice_allKeys[-1].name
                choice.rt = _choice_allKeys[-1].rt
        if GambleAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            GambleAmt.frameNStart = frameN
            GambleAmt.tStart = t
            GambleAmt.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(GambleAmt, 'tStartRefresh')
            GambleAmt.setAutoDraw(True)
        if GambleAmt.status == STARTED:
            if tThisFlipGlobal > GambleAmt.tStartRefresh + 4-frameTolerance:
                GambleAmt.tStop = t
                GambleAmt.frameNStop = frameN
                win.timeOnFlip(GambleAmt, 'tStopRefresh')
                GambleAmt.setAutoDraw(False)

        if SureAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            SureAmt.frameNStart = frameN
            SureAmt.tStart = t
            SureAmt.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(SureAmt, 'tStartRefresh')
            SureAmt.setAutoDraw(True)
        if SureAmt.status == STARTED:
            if tThisFlipGlobal > SureAmt.tStartRefresh + 4-frameTolerance:
                SureAmt.tStop = t
                SureAmt.frameNStop = frameN
                win.timeOnFlip(SureAmt, 'tStopRefresh')
                SureAmt.setAutoDraw(False)

        if GambleProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            GambleProb.frameNStart = frameN
            GambleProb.tStart = t
            GambleProb.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(GambleProb, 'tStartRefresh')
            GambleProb.setAutoDraw(True)
        if GambleProb.status == STARTED:
            if tThisFlipGlobal > GambleProb.tStartRefresh + 4-frameTolerance:
                GambleProb.tStop = t
                GambleProb.frameNStop = frameN
                win.timeOnFlip(GambleProb, 'tStopRefresh')
                GambleProb.setAutoDraw(False)

        if SureProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            SureProb.frameNStart = frameN
            SureProb.tStart = t
            SureProb.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(SureProb, 'tStartRefresh')
            SureProb.setAutoDraw(True)
        if SureProb.status == STARTED:
            if tThisFlipGlobal > SureProb.tStartRefresh + 4-frameTolerance:
                SureProb.tStop = t
                SureProb.frameNStop = frameN
                win.timeOnFlip(SureProb, 'tStopRefresh')
                SureProb.setAutoDraw(False)
        if choice.keys == '1':
            GambleAmt.setColor('green')
            chosenMoney = leftMoney
            choice.status = FINISHED
        if choice.keys == '2':
            SureAmt.setColor('green')
            chosenMoney = rightMoney
            choice.status = FINISHED
        if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
            blank.tStart = t
            blank.frameNStart = frameN
            blank.setAutoDraw(True)



        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            blank.frameNStart = frameN
            blank.tStart = t
            blank.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(blank, 'tStartRefresh')
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                blank.tStop = t
                blank.frameNStop = frameN
                win.timeOnFlip(blank, 'tStopRefresh')
                blank.setAutoDraw(False)

        if moneyBank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            moneyBank.frameNStart = frameN
            moneyBank.tStart = t
            moneyBank.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(moneyBank, 'tStartRefresh')
            moneyBank.setAutoDraw(True)
        if moneyBank.status == STARTED:
            if tThisFlipGlobal > moneyBank.tStartRefresh + 4-frameTolerance:
                moneyBank.tStop = t
                moneyBank.frameNStop = frameN
                win.timeOnFlip(moneyBank, 'tStopRefresh')
                moneyBank.setAutoDraw(False)

        if earningsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            earningsText.frameNStart = frameN
            earningsText.tStart = t
            earningsText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(earningsText, 'tStartRefresh')
            earningsText.setAutoDraw(True)
        if earningsText.status == STARTED:
            if tThisFlipGlobal > earningsText.tStartRefresh + 4-frameTolerance:
                earningsText.tStop = t
                earningsText.frameNStop = frameN
                win.timeOnFlip(earningsText, 'tStopRefresh')
                earningsText.setAutoDraw(False)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    # end Practice
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('Line.started', Line.tStartRefresh)
    PracticeLoop.addData('Line.stopped', Line.tStopRefresh)
    # check responses
    if choice.keys in ['', [], None]:
        choice.keys = None
    PracticeLoop.addData('choice.keys',choice.keys)
    if choice.keys != None:
        PracticeLoop.addData('choice.rt', choice.rt)
    PracticeLoop.addData('choice.started', choice.tStartRefresh)
    PracticeLoop.addData('choice.stopped', choice.tStopRefresh)
    PracticeLoop.addData('GambleAmt.started', GambleAmt.tStartRefresh)
    PracticeLoop.addData('GambleAmt.stopped', GambleAmt.tStopRefresh)
    PracticeLoop.addData('SureAmt.started', SureAmt.tStartRefresh)
    PracticeLoop.addData('SureAmt.stopped', SureAmt.tStopRefresh)
    PracticeLoop.addData('GambleProb.started', GambleProb.tStartRefresh)
    PracticeLoop.addData('GambleProb.stopped', GambleProb.tStopRefresh)
    PracticeLoop.addData('SureProb.started', SureProb.tStartRefresh)
    PracticeLoop.addData('SureProb.stopped', SureProb.tStopRefresh)

    if choice.keys == '1':
        chosenMoney = leftMoney
    if choice.keys == '2':
        chosenMoney = rightMoney
    if choice.keys != None:
        if subID%2==1:   #gambles are on left side of screen
           if choice.keys == '1' and WinLossCode== 1 :
               print('gambled during win condition')
               probs = int(gambleProb)
               if probs == 65:
                   probability = SixtyGamble
                   print('65% gamble')
               if probs == 35:
                   probability = ThirtyGamble
                   print('35% gamble')
               if probs == 50:
                   probability = FiftyGamble
                   print('50% gamble')
               result = random.choice(probability)
               print('gamble result:')
               print(result)
               if result == 1:   #win
                   feedbackVar = 1 #gambled during win and won
                   earnings = earnings + chosenMoney
                   print('Won money earnings:')
                   print(earnings)
               if result == 0: #lose
                   feedbackVar = 3
                #       earnings += 0

           if choice.keys == '1' and WinLossCode==0:
               print('gambled during lose condition')
              #gamProbability(gamProb)
               probs = int(gambleProb)
               if probs == 65:
                   probability = SixtyGamble
                   print('65% gamble')
               if probs == 35:
                   probability = ThirtyGamble
                   print('35% gamble')
               if probs == 50:
                   probability = FiftyGamble
                   print('50% gamble')
               result = random.choice(probability)
               print('gamble result:')
               print(result)
               if result == 1: #lose
                  feedbackVar = 2 #gambled during loss and lost
                  earnings = earnings - chosenMoney
                  print('Lost Money earnings:')
                  print(earnings)
               if result == 0: #win
                  feedbackVar = 3
             #          earnings += 0

           if choice.keys == '2'and WinLossCode ==1:
               print('did not gamble for win condition')
               earnings = earnings + chosenMoney
               feedbackVar = 1
               print('Won sure money earnings:')
               print(earnings)
           if choice.keys == '2' and WinLossCode == 0: #did not gamble for lose condition
               earnings = earnings - chosenMoney
               feedbackVar = 2
               print('Lost sure Money earnings:')
               print(earnings)


        if subID%2==0:  #gambles are on right side of screen
           if choice.keys == '2' and WinLossCode == 1:
               print('gambled during win condition')
               probs = int(gambleProb)
               if probs == 65:
                   probability = SixtyGamble
                   print('65% gamble')
               if probs == 35:
                   probability = ThirtyGamble
                   print('35% gamble')
               if probs == 50:
                   probability = FiftyGamble
                   print('50% gamble')
               result = random.choice(probability)
               print('gamble result:')
               print(result)
               if result == 1: #win
                   feedbackVar = 1
                   earnings = earnings + chosenMoney
                   print('won money earnings:')
                   print(earnings)
               if result == 0: #lost
                   feedbackVar = 3
            #           earnings += 0


           if choice.keys == '2' and WinLossCode == 0:
               print('gambled during lose condition')
                  #gamProbability(gamProb)
               probs = int(gambleProb)
               if probs == 65:
                   probability = SixtyGamble
                   print('65% gamble')
               if probs == 35:
                   probability = ThirtyGamble
                   print('35% gamble')
               if probs == 50:
                   probability = FiftyGamble
                   print('50% gamble')
               result = random.choice(probability)
               print('gamble result:')
               print(result)
               if result == 1: #lose
                   feedbackVar = 2
                   earnings = earnings - chosenMoney
                   print('Lost Money earnings:')
                   print(earnings)
               if result == 0: #win
                   feedbackVar = 3
             #          earnings += 0

           if choice.keys == '1' and WinLossCode == 1:
               print('did not gamble during win condition')
               earnings = earnings + chosenMoney
               feedbackVar = 1
               print('Won sure money earnings:')
               print(earnings)
           if choice.keys == '1' and WinLossCode == 0:
               print('did not gamble for loss condition')
               feedbackVar = 2
               earnings = earnings - chosenMoney
               print('Lost sure Money earnings:')
               print(earnings)
        earningsStr = "$" + '%.2f' % earnings
        earningsText.setText('$' + earningsStr)
    if choice.keys == None:
        feedbackVar = 4;

    GambleAmt.setColor('white')
    SureAmt.setColor('white')

    if (blank.status==FINISHED):
        GambleAmt.setAutoDraw(False)
        SureAmt.setAutoDraw(False)
        SureProb.setAutoDraw(False)
        GambleProb.setAutoDraw(False)
        Line.setAutoDraw(False)
        moneyBank.setAutoDraw(False)
    PracticeLoop.addData('blank.started', blank.tStartRefresh)
    PracticeLoop.addData('blank.stopped', blank.tStopRefresh)
    PracticeLoop.addData('moneyBank.started', moneyBank.tStartRefresh)
    PracticeLoop.addData('moneyBank.stopped', moneyBank.tStopRefresh)
    PracticeLoop.addData('earningsText.started', earningsText.tStartRefresh)
    PracticeLoop.addData('earningsText.stopped', earningsText.tStopRefresh)
    routineTimer.reset()

    #begin isi
    isiFunc(2.000)
    
#begin feedback
    continueRoutine = True
    routineTimer.add(2.500000)
    text_3.setText('placeholder')
    chosenStr = "$" + '%.2f' % chosenMoney
    winVar = []
    if WinLossCode == 1:
        winVar = "won "
    if WinLossCode == 0:
        winVar = 'lost '
    if feedbackVar == 1:
        text_3.setText("You won " + chosenStr)
    if feedbackVar == 2:
        text_3.setText("You lost " + chosenStr)
    if feedbackVar == 3 and WinLossCode == 1:
        text_3.setText("You won $0.00")
    if feedbackVar == 3 and WinLossCode == 0:
        text_3.setText("You lost $0.00")
    if feedbackVar ==4 :
        text_3.setText("No response made")
    FeedbackComponents = [text_3]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  
    frameN = -1

    #every frame Feedback
    while continueRoutine and routineTimer.getTime() > 0:
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:

            text_3.frameNStart = frameN
            text_3.tStart = t
            text_3.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(text_3, 'tStartRefresh')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            if tThisFlipGlobal > text_3.tStartRefresh + 2.5-frameTolerance:
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN
                win.timeOnFlip(text_3, 'tStopRefresh')
                text_3.setAutoDraw(False)

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine: 
            break
        continueRoutine = False 
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('text_3.started', text_3.tStartRefresh)
    PracticeLoop.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()


#begin BeginInst
continueRoutine = True
earning = 5
earnings = 5
earningsStr = "$" + '%.2f' % earnings
earningsText.setText('$' + earningsStr)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
BeginInstComponents = [text_2, key_resp]
for thisComponent in BeginInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginInstClock.reset(-_timeToFirstFrame) 
frameN = -1

# every frame BeginInst
while continueRoutine:
    t = BeginInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1 

    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        text_2.frameNStart = frameN
        text_2.tStart = t
        text_2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(text_2, 'tStartRefresh')
        text_2.setAutoDraw(True)

    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        key_resp.frameNStart = frameN
        key_resp.tStart = t
        key_resp.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(key_resp, 'tStartRefresh')
        key_resp.status = STARTED
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name
            key_resp.rt = _key_resp_allKeys[-1].rt
            continueRoutine = False

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in BeginInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

#end instructions
for thisComponent in BeginInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
earnings = 4
earning = 4
earningsStr = "$" + '%.2f' % earnings
earningsText.setText('$' + earningsStr)
if key_resp.keys in ['', [], None]:
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()

mainLoop = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeSlotMach_Localizer.xlsx'),
    seed=None, name='mainLoop')
thisExp.addLoop(mainLoop)
thisMainLoop = mainLoop.trialList[0]
if thisMainLoop != None:
    for paramName in thisMainLoop:
        exec('{} = thisMainLoop[paramName]'.format(paramName))

for thisMainLoop in mainLoop:
    currentLoop = mainLoop
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))

    # begin isi
    isiFunc(2.000)
    
    earning = 4
    earnings = 4

    trials = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SlotMachine.csv', selection=Rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)
    thisTrial = trials.trialList[0]
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    for thisTrial in trials:
        currentLoop = trials
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))

        #begin isi
        isiFunc(2.0000)

        #begin routine Practice
        continueRoutine = True
        routineTimer.add(4.000000)
        Line.setFillColor([-1.000,-1.000,-1.000])
        Line.setSize((3, 0.5))
        Line.setLineColor([-1.000,-1.000,-1.000])
        Line.setLineWidth(7)
        choice.keys = []
        choice.rt = []
        _choice_allKeys = []
        GambleAmt.setColor('white', colorSpace='rgb')
        GambleAmt.setPos((-0.41, -0.1))
        GambleAmt.setText('')
        GambleAmt.setFont('Arial')
        GambleAmt.setHeight(0.11)
        SureAmt.setColor('white', colorSpace='rgb')
        SureAmt.setPos((0.41, -0.1))
        SureAmt.setText('')
        SureAmt.setFont('Arial')
        SureAmt.setHeight(0.11)
        GambleProb.setColor('white', colorSpace='rgb')
        GambleProb.setPos((-0.41, 0.3))
        GambleProb.setText('')
        GambleProb.setFont('Arial')
        GambleProb.setHeight(0.13)
        SureProb.setColor('white', colorSpace='rgb')
        SureProb.setPos((0.41, 0.3))
        SureProb.setText('')
        SureProb.setFont('Arial')
        SureProb.setHeight(0.13)
        feedbackVar = []
        leftVarText=[]
        leftVarMoney = []
        rightVarText = []
        rightVarMoney = []
        result = []

        if subID%2 == 1 :
            leftVarText = (gambleWinLoss)
            leftVarMoney = (gamble)
            rightVarText = (sureWinLoss)
            rightVarMoney = (sure)
        if subID%2 == 0:
            rightVarText= (gambleWinLoss)
            rightVarMoney= (gamble)
            leftVarText= (sureWinLoss)
            leftVarMoney= (sure)

        GambleAmtVar = "$" + '%.2f' % leftVarMoney
        GambleAmt.setText(GambleAmtVar)
        SureAmtVar = "$" + '%.2f' % rightVarMoney
        SureAmt.setText(SureAmtVar)
        GambleProb.setText(leftVarText)
        SureProb.setText(rightVarText)

        leftMoney = float(leftVarMoney)
        rightMoney = float(rightVarMoney)
        WinLossType = int(WinLossCode)


        blank.setText('')
        earningsText.setText(earningsStr)
        PracticeComponents = [Line, choice, GambleAmt, SureAmt, GambleProb, SureProb, blank, moneyBank, earningsText]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeClock.reset(-_timeToFirstFrame)
        frameN = -1

        #every frame routine Practice
        while continueRoutine and routineTimer.getTime() > 0:
            t = PracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            if Line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                Line.frameNStart = frameN
                Line.tStart = t
                Line.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(Line, 'tStartRefresh')
                Line.setAutoDraw(True)
            if Line.status == STARTED:
                if tThisFlipGlobal > Line.tStartRefresh + 4-frameTolerance:
                    Line.tStop = t
                    Line.frameNStop = frameN
                    win.timeOnFlip(Line, 'tStopRefresh')
                    Line.setAutoDraw(False)

            waitOnFlip = False
            if choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                choice.frameNStart = frameN
                choice.tStart = t
                choice.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(choice, 'tStartRefresh')
                choice.status = STARTED
                waitOnFlip = True
                win.callOnFlip(choice.clock.reset)
                win.callOnFlip(choice.clearEvents, eventType='keyboard')
            if choice.status == STARTED:
                if tThisFlipGlobal > choice.tStartRefresh + 4-frameTolerance:
                    choice.tStop = t
                    choice.frameNStop = frameN
                    win.timeOnFlip(choice, 'tStopRefresh')
                    choice.status = FINISHED
            if choice.status == STARTED and not waitOnFlip:
                theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
                _choice_allKeys.extend(theseKeys)
                if len(_choice_allKeys):
                    choice.keys = _choice_allKeys[-1].name
                    choice.rt = _choice_allKeys[-1].rt

            if GambleAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                GambleAmt.frameNStart = frameN
                GambleAmt.tStart = t
                GambleAmt.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(GambleAmt, 'tStartRefresh')
                GambleAmt.setAutoDraw(True)
            if GambleAmt.status == STARTED:
                if tThisFlipGlobal > GambleAmt.tStartRefresh + 4-frameTolerance:
                    GambleAmt.tStop = t
                    GambleAmt.frameNStop = frameN
                    win.timeOnFlip(GambleAmt, 'tStopRefresh')
                    GambleAmt.setAutoDraw(False)

            if SureAmt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                SureAmt.frameNStart = frameN
                SureAmt.tStart = t
                SureAmt.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(SureAmt, 'tStartRefresh')
                SureAmt.setAutoDraw(True)
            if SureAmt.status == STARTED:
                if tThisFlipGlobal > SureAmt.tStartRefresh + 4-frameTolerance:
                    SureAmt.tStop = t
                    SureAmt.frameNStop = frameN
                    win.timeOnFlip(SureAmt, 'tStopRefresh')
                    SureAmt.setAutoDraw(False)

            if GambleProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                GambleProb.frameNStart = frameN
                GambleProb.tStart = t
                GambleProb.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(GambleProb, 'tStartRefresh')
                GambleProb.setAutoDraw(True)
            if GambleProb.status == STARTED:
                if tThisFlipGlobal > GambleProb.tStartRefresh + 4-frameTolerance:
                    GambleProb.tStop = t
                    GambleProb.frameNStop = frameN
                    win.timeOnFlip(GambleProb, 'tStopRefresh')
                    GambleProb.setAutoDraw(False)

            if SureProb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                SureProb.frameNStart = frameN
                SureProb.tStart = t
                SureProb.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(SureProb, 'tStartRefresh')
                SureProb.setAutoDraw(True)
            if SureProb.status == STARTED:
                if tThisFlipGlobal > SureProb.tStartRefresh + 4-frameTolerance:
                    SureProb.tStop = t
                    SureProb.frameNStop = frameN
                    win.timeOnFlip(SureProb, 'tStopRefresh')
                    SureProb.setAutoDraw(False)

            if choice.keys == '1':
                GambleAmt.setColor('green')
                chosenMoney = leftMoney
                choice.status = FINISHED
            if choice.keys == '2':
                SureAmt.setColor('green')
                chosenMoney = rightMoney
                choice.status = FINISHED

            if (choice.keys == '1' or choice.keys == '2') and blank.status == NOT_STARTED:
                blank.tStart = t
                blank.frameNStart = frameN
                blank.setAutoDraw(True)
            #gamProbability(gambleProb)
            #gambleFunc(gambleProb)
            #earningsFunct(gambleProb, chosenMoney, WinLossCode, earnings)
            #print(earnings)




            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                blank.frameNStart = frameN
                blank.tStart = t
                blank.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(blank, 'tStartRefresh')
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                    blank.tStop = t
                    blank.frameNStop = frameN
                    win.timeOnFlip(blank, 'tStopRefresh')
                    blank.setAutoDraw(False)

            if moneyBank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                moneyBank.frameNStart = frameN
                moneyBank.tStart = t
                moneyBank.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(moneyBank, 'tStartRefresh')
                moneyBank.setAutoDraw(True)
            if moneyBank.status == STARTED:
                if tThisFlipGlobal > moneyBank.tStartRefresh + 4-frameTolerance:
                    moneyBank.tStop = t
                    moneyBank.frameNStop = frameN
                    win.timeOnFlip(moneyBank, 'tStopRefresh')
                    moneyBank.setAutoDraw(False)

            if earningsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:

                earningsText.frameNStart = frameN
                earningsText.tStart = t
                earningsText.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(earningsText, 'tStartRefresh')
                earningsText.setAutoDraw(True)
            if earningsText.status == STARTED:
                if tThisFlipGlobal > earningsText.tStartRefresh + 4-frameTolerance:
                    earningsText.tStop = t
                    earningsText.frameNStop = frameN
                    win.timeOnFlip(earningsText, 'tStopRefresh')
                    earningsText.setAutoDraw(False)

            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break

            if continueRoutine:
                win.flip()

        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Line.started', Line.tStartRefresh)
        trials.addData('Line.stopped', Line.tStopRefresh)
        if choice.keys in ['', [], None]: 
            choice.keys = None
        trials.addData('choice.keys',choice.keys)
        if choice.keys != None: 
            trials.addData('choice.rt', choice.rt)
        trials.addData('choice.started', choice.tStartRefresh)
        trials.addData('choice.stopped', choice.tStopRefresh)
        trials.addData('GambleAmt.started', GambleAmt.tStartRefresh)
        trials.addData('GambleAmt.stopped', GambleAmt.tStopRefresh)
        trials.addData('SureAmt.started', SureAmt.tStartRefresh)
        trials.addData('SureAmt.stopped', SureAmt.tStopRefresh)
        trials.addData('GambleProb.started', GambleProb.tStartRefresh)
        trials.addData('GambleProb.stopped', GambleProb.tStopRefresh)
        trials.addData('SureProb.started', SureProb.tStartRefresh)
        trials.addData('SureProb.stopped', SureProb.tStopRefresh)

        if choice.keys == '1':
            chosenMoney = leftMoney
        if choice.keys == '2':
            chosenMoney = rightMoney
        if choice.keys != None:
            if subID%2==1:   #gambles are on left side of screen
               if choice.keys == '1' and WinLossCode== 1 :
                   print('gambled during win condition')
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)
                   if result == 1:   #win
                       feedbackVar = 1 #gambled during win and won
                       earnings = earnings + chosenMoney
                       print('Won money earnings:')
                       print(earnings)
                   if result == 0: #lose
                       feedbackVar = 3
                    #       earnings += 0

               if choice.keys == '1' and WinLossCode==0:
                   print('gambled during lose condition')
                  #gamProbability(gamProb)
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)
                   if result == 1: #lose
                      feedbackVar = 2 #gambled during loss and lost
                      earnings = earnings - chosenMoney
                      print('Lost Money earnings:')
                      print(earnings)
                   if result == 0: #win
                      feedbackVar = 3
                 #          earnings += 0

               if choice.keys == '2'and WinLossCode ==1:
                   print('did not gamble for win condition')
                   earnings = earnings + chosenMoney
                   feedbackVar = 1
                   print('Won sure money earnings:')
                   print(earnings)
               if choice.keys == '2' and WinLossCode == 0: #did not gamble for lose condition
                   earnings = earnings - chosenMoney
                   feedbackVar = 2
                   print('Lost sure Money earnings:')
                   print(earnings)


            if subID%2==0:  #gambles are on right side of screen
               if choice.keys == '2' and WinLossCode == 1:
                   print('gambled during win condition')
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)
                   if result == 1: #win
                       feedbackVar = 1
                       earnings = earnings + chosenMoney
                       print('won money earnings:')
                       print(earnings)
                   if result == 0: #lost
                       feedbackVar = 3
                #           earnings += 0


               if choice.keys == '2' and WinLossCode == 0:
                   print('gambled during lose condition')
                      #gamProbability(gamProb)
                   probs = int(gambleProb)
                   if probs == 65:
                       probability = SixtyGamble
                       print('65% gamble')
                   if probs == 35:
                       probability = ThirtyGamble
                       print('35% gamble')
                   if probs == 50:
                       probability = FiftyGamble
                       print('50% gamble')
                   result = random.choice(probability)
                   print('gamble result:')
                   print(result)
                   if result == 1: #lose
                       feedbackVar = 2
                       earnings = earnings - chosenMoney
                       print('Lost Money earnings:')
                       print(earnings)
                   if result == 0: #win
                       feedbackVar = 3
                 #          earnings += 0

               if choice.keys == '1' and WinLossCode == 1:
                   print('did not gamble during win condition')
                   earnings = earnings + chosenMoney
                   feedbackVar = 1
                   print('Won sure money earnings:')
                   print(earnings)
               if choice.keys == '1' and WinLossCode == 0:
                   print('did not gamble for loss condition')
                   feedbackVar = 2
                   earnings = earnings - chosenMoney
                   print('Lost sure Money earnings:')
                   print(earnings)
            earningsStr = "$" + '%.2f' % earnings
            earningsText.setText('$' + earningsStr)
        if choice.keys == None:
            feedbackVar = 4;

        GambleAmt.setColor('white')
        SureAmt.setColor('white')

        if (blank.status==FINISHED):
            GambleAmt.setAutoDraw(False)
            SureAmt.setAutoDraw(False)
            SureProb.setAutoDraw(False)
            GambleProb.setAutoDraw(False)
            Line.setAutoDraw(False)
            moneyBank.setAutoDraw(False)
        trials.addData('blank.started', blank.tStartRefresh)
        trials.addData('blank.stopped', blank.tStopRefresh)
        trials.addData('moneyBank.started', moneyBank.tStartRefresh)
        trials.addData('moneyBank.stopped', moneyBank.tStopRefresh)
        trials.addData('earningsText.started', earningsText.tStartRefresh)
        trials.addData('earningsText.stopped', earningsText.tStopRefresh)

        #begin isi
        isiFunc(2.000)
        
        # begin routine Feedback
        continueRoutine = True
        routineTimer.add(2.500000)
        text_3.setText('placeholder')
        chosenStr = "$" + '%.2f' % chosenMoney
        winVar = []
        if WinLossCode == 1:
            winVar = "won "
        if WinLossCode == 0:
            winVar = 'lost '
        if feedbackVar == 1:
            text_3.setText("You won " + chosenStr)
        if feedbackVar == 2:
            text_3.setText("You lost " + chosenStr)
        if feedbackVar == 3 and WinLossCode == 1:
            text_3.setText("You won $0.00")
        if feedbackVar == 3 and WinLossCode == 0:
            text_3.setText("You lost $0.00")
        if feedbackVar ==4 :
            text_3.setText("No response made")
        FeedbackComponents = [text_3]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)
        frameN = -1

        while continueRoutine and routineTimer.getTime() > 0:
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1

            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text_3.frameNStart = frameN
                text_3.tStart = t
                text_3.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(text_3, 'tStartRefresh')
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                if tThisFlipGlobal > text_3.tStartRefresh + 2.5-frameTolerance:
                    text_3.tStop = t
                    text_3.frameNStop = frameN
                    win.timeOnFlip(text_3, 'tStopRefresh')
                    text_3.setAutoDraw(False)

            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break

            if continueRoutine:
                win.flip()

        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_3.started', text_3.tStartRefresh)
        trials.addData('text_3.stopped', text_3.tStopRefresh)
        thisExp.nextEntry()

    thisExp.nextEntry()

isiFunc(15.00)

# begin Routine ThankYou
continueRoutine = True

if earnings <= 0.00:
    earningsStr = "$0.00"
tyText.setText("Thank you for playing!\n\nYour total earnings are " + earningsStr)
ThankYouComponents = [tyText]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankYouClock.reset(-_timeToFirstFrame) 
frameN = -1

while continueRoutine:
    t = ThankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1 

    if tyText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        tyText.frameNStart = frameN
        tyText.tStart = t
        tyText.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(tyText, 'tStartRefresh')
        tyText.setAutoDraw(True)

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine: 
        break
    continueRoutine = False
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

# end routine
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tyText.started', tyText.tStartRefresh)
thisExp.addData('tyText.stopped', tyText.tStopRefresh)
routineTimer.reset()
win.flip()

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
