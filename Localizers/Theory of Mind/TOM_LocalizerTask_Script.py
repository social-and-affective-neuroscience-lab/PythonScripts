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
from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '2021.1.2'
expName = 'TOM_LocalizerTask'
expInfo = {'Participant ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant ID'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Certainty Study\\TOM_Localizer\\TOM_LocalizerTask.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
endExpNow = False
frameTolerance = 0.001

win = visual.Window(size=(1024, 768), fullscr=True, screen=0,winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

# Initialize vars
IntroClock = core.Clock()
VignetteRoutineClock = core.Clock()
ISIClock = core.Clock()
AnswerRoutineClock = core.Clock()
ITIClock = core.Clock()
endScreenClock = core.Clock()

spaceKey = keyboard.Keyboard()
Response = keyboard.Keyboard()

Instructions = visual.TextStim(win=win,text='', wrapWidth=1.2,pos=(0, 0), height=0.06, color='white');
VigText = visual.TextStim(win=win, text='', pos=(0, 0), height=0.06, wrapWidth=1.35, color='white');
isi_text = visual.TextStim(win=win, text='',pos=(0, 0), height=0.07, color='white', colorSpace='rgb');
blank = visual.TextStim(win=win, text='',pos=(0, 0), height=0.1);
Qtext = visual.TextStim(win=win, text='',pos=(0, 0.15), height=0.06, wrapWidth=1.5, color='white');
TrueText = visual.TextStim(win=win, text='True', pos=[0,0], height=0.055, color='white');
FalseText = visual.TextStim(win=win, text='False',pos=(0.5, -0.1), height=0.055, color='white');
ITI_text = visual.TextStim(win=win, text='+', pos=(0, 0), height=0.07, color='white');
endText = visual.TextStim(win=win, text='Thank you, you have completed this part of the study! ', pos=(0, 0), height=0.06, wrapWidth=1.4,color='white');

globalClock = core.Clock()
routineTimer = core.CountdownTimer()

#begin Intro routine
def introFunc(text):
    continueRoutine = True
    spaceKey.keys = []
    spaceKey.rt = []
    IntroComponents = [Instructions, spaceKey]
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    while continueRoutine:
        if Instructions.status == NOT_STARTED:
            Instructions.setText(text)
            Instructions.setAutoDraw(True)
        waitOnFlip = False
        if spaceKey.status == NOT_STARTED:
            spaceKey.status = STARTED
        if spaceKey.status == STARTED:
            theseKeys = spaceKey.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                spaceKey.keys = theseKeys[-1].name
                spaceKey.rt = theseKeys[-1].rt
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in IntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if spaceKey.keys != None:
        thisExp.addData('spaceKey.rt', spaceKey.rt)
    thisExp.nextEntry()
    routineTimer.reset()

textArray=["In this part of the study, you will be reading short vignettes and responding to one true or false statement following each vignette.\n\n You will have 10 seconds to read each vignette, and 6 seconds to respond. \n\n Press SPACE for more instructions.", \
    "To respond 'true' to the statement, press the \'1\' key. \n\n To respond 'false' to the statement, press the \'2\' key.\n\n When you are ready to begin, press SPACE!"]
for i in textArray:
    introFunc(i)


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


isiFunc(3.00)

trials = data.TrialHandler(nReps=1.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TOM_Stimuli.csv'),
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
    continueRoutine = True
    routineTimer.add(10.000000)
    VigText.setText(Vignette)
    VignetteRoutineComponents = [VigText]
    for thisComponent in VignetteRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VignetteRoutineClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine and routineTimer.getTime() > 0:
        t = VignetteRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VignetteRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if VigText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            VigText.frameNStart = frameN
            VigText.tStart = t
            VigText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(VigText, 'tStartRefresh')
            VigText.setAutoDraw(True)
        if VigText.status == STARTED:
            if tThisFlipGlobal > VigText.tStartRefresh + 10.0-frameTolerance:
                VigText.tStop = t
                VigText.frameNStop = frameN
                win.timeOnFlip(VigText, 'tStopRefresh')
                VigText.setAutoDraw(False)

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in VignetteRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()
    for thisComponent in VignetteRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('VigText.started', VigText.tStartRefresh)
    trials.addData('VigText.stopped', VigText.tStopRefresh)

    #begin routine ISI
    isiFunc(3.00)

    #begin routine AnswerRoutine
    continueRoutine = True
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    Qtext.setText(Question)
    TrueText.setPos((-0.5, -0.1))
    if Response.keys == '1':
        blank.status = STARTED
        TrueText.setColor("blue")
    if Response.keys =='2':
        blank.status=STARTED
        FalseText.setColor("blue")
    AnswerRoutineComponents = [Response, blank, Qtext, TrueText, FalseText]
    for thisComponent in AnswerRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AnswerRoutineClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine:
        t = AnswerRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AnswerRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            Response.frameNStart = frameN
            Response.tStart = t
            Response.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(Response, 'tStartRefresh')
            Response.status = STARTED
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)
            win.callOnFlip(Response.clearEvents, eventType='keyboard')
        if Response.status == STARTED:
            if tThisFlipGlobal > Response.tStartRefresh + 7.0-frameTolerance:
                Response.tStop = t
                Response.frameNStop = frameN
                win.timeOnFlip(Response, 'tStopRefresh')
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['1', '2'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name
                Response.rt = _Response_allKeys[-1].rt

        if blank.status == NOT_STARTED and asarray(len(Response.keys) > 0):
            blank.frameNStart = frameN
            blank.tStart = t
            blank.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(blank, 'tStartRefresh')
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            if tThisFlipGlobal > blank.tStartRefresh + 1.5:
                blank.tStop = t
                blank.frameNStop = frameN
                win.timeOnFlip(blank, 'tStopRefresh')
                blank.setAutoDraw(False)

        if Qtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            Qtext.frameNStart = frameN
            Qtext.tStart = t
            Qtext.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(Qtext, 'tStartRefresh')
            Qtext.setAutoDraw(True)
        if Qtext.status == STARTED:
            if tThisFlipGlobal > Qtext.tStartRefresh + 7.0-frameTolerance:
                Qtext.tStop = t
                Qtext.frameNStop = frameN
                win.timeOnFlip(Qtext, 'tStopRefresh')
                Qtext.setAutoDraw(False)

        if TrueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            TrueText.frameNStart = frameN
            TrueText.tStart = t
            TrueText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(TrueText, 'tStartRefresh')
            TrueText.setAutoDraw(True)
        if TrueText.status == STARTED:
            if tThisFlipGlobal > TrueText.tStartRefresh + 7.0-frameTolerance:
                TrueText.tStop = t
                TrueText.frameNStop = frameN
                win.timeOnFlip(TrueText, 'tStopRefresh')
                TrueText.setAutoDraw(False)

        if FalseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            FalseText.frameNStart = frameN
            FalseText.tStart = t
            FalseText.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(FalseText, 'tStartRefresh')
            FalseText.setAutoDraw(True)
        if FalseText.status == STARTED:
            if tThisFlipGlobal > FalseText.tStartRefresh + 7.0-frameTolerance:
                FalseText.tStop = t
                FalseText.frameNStop = frameN
                win.timeOnFlip(FalseText, 'tStopRefresh')
                FalseText.setAutoDraw(False)
        if Response.keys == '1':
            TrueText.setColor("blue")
        if Response.keys =='2':
            FalseText.setColor("blue")

        if Response.keys == '1' or Response.keys =='2':
            Response.status=FINISHED
        if t>=7.5:
            continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in AnswerRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win.flip()

    for thisComponent in AnswerRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if Response.keys in ['', [], None]:
        Response.keys = None
    trials.addData('Response.keys',Response.keys)
    if Response.keys != None:
        trials.addData('Response.rt', Response.rt)

    TrueText.setColor("white")
    FalseText.setColor("white")
    
    routineTimer.reset()

    #begin routine ITI
    isiFunc(5.00)
    thisExp.nextEntry()

isiFunc(15.000)

#begin routine endScreen
continueRoutine = True
routineTimer.add(6.000000)
endScreenComponents = [endText]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine and routineTimer.getTime() > 0:
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        endText.frameNStart = frameN
        endText.tStart = t
        endText.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(endText, 'tStartRefresh')
        endText.setAutoDraw(True)
    if endText.status == STARTED:

        if tThisFlipGlobal > endText.tStartRefresh + 6.0-frameTolerance:
            endText.tStop = t
            endText.frameNStop = frameN
            win.timeOnFlip(endText, 'tStopRefresh')
            endText.setAutoDraw(False)

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()

for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.flip()

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
