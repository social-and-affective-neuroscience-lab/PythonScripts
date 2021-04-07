#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import pandas as pd
import sys  # to get file system encoding
import random
from psychopy.hardware import keyboard
from psychopy.tools.filetools import fromFile

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'FinanceSNS'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Self-Regulation-Psychopy-Files-master\\Self-Regulation-Psychopy-Files-master\\AcademicSelf-Regulation\\FinanceSNS\\FinanceSNS.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
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
    frameDur = 1.0 / 60.0  # could not measure, so guess

defaultKeyboard = keyboard.Keyboard()

InstructionsClock = core.Clock()
instructions1 = visual.TextStim(win=win, name='instruct',
    text='In this part of the study, you will be making choices to allocate 20 minutes between reading finance tips and watching youtube videos. \n\nBefore making these decisions, you will first be prompted to choose what type of videos and what type of finance tips you want to make these allocations between.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.4, ori=0,
    color='white');
space = keyboard.Keyboard()
instructions2 = visual.TextStim(win=win, name='instruct',
    text='Which type of video would you like to make decisions about? Please use the number keys 1, 2, and 3 to move to the video you would like, then press ENTER to continue.',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=1.4, ori=0,
    color='white');
enter = keyboard.Keyboard()
chooseGameClock = core.Clock()

comedyVids = visual.TextStim(win=win, text='Comedy Videos', pos = (-0.5,-0.08), height=0.05)
musicVids = visual.TextStim(win=win, text='Music Videos', pos = (0.5,-0.08), height=0.05)
gameVids = visual.TextStim(win=win, text='Gaming Videos', pos = (0,-0.08), height=0.05)

comedy = visual.ImageStim(win=win, image='comedy.PNG', pos=(-0.5, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)
music = visual.ImageStim(win=win, image='music.PNG', pos=(0.5, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)
game = visual.ImageStim(win=win, image='gaming.PNG', pos=(0, -0.25), size=(0.38, 0.27),
    color=[1,1,1], texRes=128.0, interpolate=True)

polygon = visual.Rect(win=win,size=(0.39, 0.28),
    ori=0.0, pos=(0, 0),lineWidth=8, lineColor='black', fillColor=None,interpolate=True)

instructions3 = visual.TextStim(win=win, name='instruct',
    text='Which type of finance tips would you like to make decisions about? Please use the number keys 1, 2, and 3 to move to the tips you would like, then press ENTER to continue.',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=1.4, ori=0,
    color='white');

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

instructions4 = visual.TextStim(win=win,
    text='When making your decisions, you will be cued with the name of a person OR a word. On the following screens, you will be instructed to type out the name of two different, independent people in your life.\n\nPress SPACE to continue.',
    pos=(0, 0), height=0.05, wrapWidth=1.4, color='white');
instructions5 = visual.TextStim(win=win,
    text="You will be completing 24 blocks of decisions, with each block consisting of 5 decisions.\n\nDuring each block of decisions, you will either see one of the words you typed, one of the names you typed, or the word 'Choice' in the center of the screen. \n\nPress SPACE to continue.",
    pos=(0, 0), height=0.05, wrapWidth=1.4, color='white');

inst5A = visual.TextStim(win=win, text='',pos=(0, 0.016), height=0.05, wrapWidth=1.4, color='white')
inst5B = visual.TextStim(win=win, text='', pos=(0, 0.015), height=0.05, wrapWidth=1.4, color='white')

instructions6 = visual.TextStim(win=win,
    text="Each decision will consist of making allocations of 20 minutes towards watching the videos you chose and reading the financial tips you chose. You will be presented with two different allocations - one on the left side of your screen and one on the right side of your screen. \n\nTo choose the allocation on the left side, press the 1 key. \nTo choose the allocation on the right side, press the 2 key.\nYou will have 6 seconds to make your choice before the trials move on. \n\nPress SPACE to continue.",
    pos=(0, 0), height=0.05, wrapWidth=1.4, color='white');

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
blank = visual.TextStim(win=win, text='', pos=(0,0), height=0.001, color='white')

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

bucket = ["a","b","c","d","e", "f", "g", "h", "i","j","k","l", "m","n","o","p","u","v","w", "x"]


selectedTips=[]
selectedVid=[]

keyResp = keyboard.Keyboard()
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

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
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + timeVar-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isi"-------
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)



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
# reset timers
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
        # keep track of start time/frame for later
        instructions1.frameNStart = frameN  # exact frame index
        instructions1.tStart = t  # local t and not account for scr refresh
        instructions1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1, 'tStartRefresh')  # time at next scr refresh
        instructions1.setAutoDraw(True)

    # *space* updates
    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.status = STARTED
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        _space_allKeys.extend(theseKeys)
        if len(_space_allKeys):
            space.keys = _space_allKeys[-1].name  # just the last key pressed
            space.rt = _space_allKeys[-1].rt
            continueRoutine = False

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
thisExp.nextEntry()
routineTimer.reset()

# ------Prepare to start Routine "GameChoice"-------
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
GameChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
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
        # keep track of start time/frame for later
        enter.frameNStart = frameN  # exact frame index
        enter.tStart = t  # local t and not account for scr refresh
        enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
        enter.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name  # just the last key pressed
            enter.rt = _enter_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    if keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp.frameNStart = frameN  # exact frame index
        keyResp.tStart = t  # local t and not account for scr refresh
        keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
        keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp.status == STARTED and not waitOnFlip:
        theseKeys = keyResp.getKeys(keyList=['1', '2', '3', 'return'], waitRelease=False)
        _keyResp_allKeys.extend(theseKeys)
        if len(_keyResp_allKeys):
            keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
            keyResp.rt = _keyResp_allKeys[-1].rt

    if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.tStart = t  # local t and not account for scr refresh
        instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2, 'tStartRefresh')  # time at next scr refresh
        instructions2.setAutoDraw(True)

    if comedy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        comedy.frameNStart = frameN  # exact frame index
        comedy.tStart = t  # local t and not account for scr refresh
        comedy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(comedy, 'tStartRefresh')  # time at next scr refresh
        comedy.setAutoDraw(True)

    if game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        game.frameNStart = frameN  # exact frame index
        game.tStart = t  # local t and not account for scr refresh
        game.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(game, 'tStartRefresh')  # time at next scr refresh
        game.setAutoDraw(True)

    if music.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        music.frameNStart = frameN  # exact frame index
        music.tStart = t  # local t and not account for scr refresh
        music.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(music, 'tStartRefresh')  # time at next scr refresh
        music.setAutoDraw(True)

    # *image_4* updates
    if comedyVids.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        comedyVids.frameNStart = frameN  # exact frame index
        comedyVids.tStart = t  # local t and not account for scr refresh
        comedyVids.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(comedyVids, 'tStartRefresh')  # time at next scr refresh
        comedyVids.setAutoDraw(True)

    if musicVids.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        musicVids.frameNStart = frameN  # exact frame index
        musicVids.tStart = t  # local t and not account for scr refresh
        musicVids.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(musicVids, 'tStartRefresh')  # time at next scr refresh
        musicVids.setAutoDraw(True)

    # *image_6* updates
    if gameVids.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gameVids.frameNStart = frameN  # exact frame index
        gameVids.tStart = t  # local t and not account for scr refresh
        gameVids.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gameVids, 'tStartRefresh')  # time at next scr refresh
        gameVids.setAutoDraw(True)
    # *polygon* updates
    if polygon.status == NOT_STARTED and asarray(keyResp.keys == '1' or keyResp.keys == '2' or keyResp.keys == '3'):
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:  # only update if drawing
        polygon.setPos((x, -0.25))
    if keyResp.keys == '1':
        x = -0.5
    if keyResp.keys == '2':
        x = 0
    if keyResp.keys == '3':
        x=0.5


    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GameChoiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GameChoiceComponents"-------
for thisComponent in GameChoiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if keyResp.keys in ['', [], None]:  # No response was made
    keyResp.keys = None
if keyResp.keys != None:  # we had a response
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
if enter.keys in ['', [], None]:  # No response was made
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
if enter.keys != None:  # we had a response
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
FinTipChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
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
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
    if polygon_2.status == NOT_STARTED and asarray(keyResp1.keys == '1' or keyResp1.keys == '2' or keyResp1.keys == '3'):
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:  # only update if drawing
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
        win.callOnFlip(enter1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter1.status == STARTED and not waitOnFlip:
        theseKeys = enter1.getKeys(keyList=['return'], waitRelease=False)
        _enter1_allKeys.extend(theseKeys)
        if len(_enter1_allKeys):
            enter1.keys = _enter1_allKeys[-1].name  # just the last key pressed
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

continueRoutine = True
space.keys = []
space.rt = []
_space_allKeys = []
Instructions2Components = [instructions4, space]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions2Clock = core.Clock()
Instructions2Clock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    t = Instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if instructions4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instructions4.frameNStart = frameN  # exact frame index
        instructions4.tStart = t  # local t and not account for scr refresh
        instructions4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions4, 'tStartRefresh')  # time at next scr refresh
        instructions4.setAutoDraw(True)

    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        space.frameNStart = frameN
        space.tStart = t 
        space.tStartRefresh = tThisFlipGlobal 
        win.timeOnFlip(space, 'tStartRefresh') 
        space.status = STARTED
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
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
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break 

    if continueRoutine:
        win.flip()

# -------Ending Routine 
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if space.keys in ['', [], None]:
    space.keys = None
thisExp.addData('space.keys',space.keys)
thisExp.nextEntry()
routineTimer.reset()

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
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name  # just the last key pressed
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

    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in typeFinNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

# -------Ending Routine "typeFinName"-------
for thisComponent in typeFinNameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:  # No response was made
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
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name  # just the last key pressed
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

    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in typefriendNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

for thisComponent in typefriendNameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:  # No response was made
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
thisExp.addData('Friend Name', friendName.text)
friendName = friendName.text
friendNameStr = str(friendName)
print("friend name: ", friendNameStr)
thisExp.nextEntry()
routineTimer.reset()


Instruction2AComponents = []
continueRoutine = True
space.keys = []
space.rt = []
_space_allKeys = []
Instruction2AComponents = [instructions4, space]
for thisComponent in Instruction2AComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions2AClock = core.Clock()
Instructions2AClock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    t = Instructions2AClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2AClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if instructions4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instructions4.setText("On the following screens, you will be instructed to write down two different words (not names). \n\nPress SPACE to continue.")
        instructions4.setAutoDraw(True)

    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        space.status = STARTED
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        _space_allKeys.extend(theseKeys)
        if len(_space_allKeys):
            space.keys = _space_allKeys[-1].name  # just the last key pressed
            space.rt = _space_allKeys[-1].rt
            continueRoutine = False

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    for thisComponent in Instruction2AComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

for thisComponent in Instruction2AComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if space.keys in ['', [], None]:
    space.keys = None
thisExp.addData('space.keys',space.keys)
thisExp.nextEntry()
routineTimer.reset()

#Begin typing for finance words
typefinWordClock=core.Clock()
event.clearEvents('keyboard')
_enter_allKeys_ = []
modify = False
finWord = visual.TextStim(win=win, text='default text', height=0.1, color='white', pos=[0,-0.05], wrapWidth=1.2)
finWord.text = ""

typefinWordComponents = [enter, nameInstructions, finWord]
nameInstructions.setText("Think of a word that reminds you of financial success.\n\nPlease type that word below, then press ENTER to continue:")
for thisComponent in typefinWordComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
typefinWordClock.reset(-_timeToFirstFrame)
frameN = -1

continueRoutine = True
while continueRoutine:
    t = typefinWordClock.getTime()
    frameN = frameN + 1
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name  # just the last key pressed
            enter.rt = _enter_allKeys[-1].rt
            continueRoutine = False
    if nameInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        nameInstructions.setAutoDraw(True) 
    if t >= 0.0 and finWord.status == NOT_STARTED:
        finWord.tStart = t
        finWord.frameNStart = frameN
        finWord.setAutoDraw(True)

    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            finWord.text = finWord.text + ' '
        elif 'backspace' in keys:
            finWord.text = finWord.text[:-1]
        elif 'apostrophe' in keys:
            finWord.text = finWord.text + "'"
        elif 'lshift' in keys or 'rshift'  in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                finWord.text = finWord.text + keys[0].upper()
                modify = False
            else:
                finWord.text = finWord.text + keys[0]
                
    if finWord.text == '' and enter.keys != None:
        continueRoutine = True
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in typefinWordComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in typefinWordComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    if continueRoutine:
        win.flip()

for thisComponent in typefinWordComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
thisExp.addData('Finance Word', finWord.text)
finWord = finWord.text
finWordStr = str(finWord)
print("Finance Word: ", finWordStr)
thisExp.nextEntry()
routineTimer.reset()


#BEgin typing for friend word
typefriendWordClock=core.Clock()
event.clearEvents('keyboard')
_enter_allKeys_ = []
modify = False
friendWord = visual.TextStim(win=win, text='default text', height=0.1, color='white', pos=[0,-0.05], wrapWidth=1.2)
friendWord.text = ""

typefriendWordComponents = [enter, nameInstructions, friendWord]
nameInstructions.setText("Think of a word that reminds you of hanging out socially.\n\nPlease type that word below, then press ENTER to continue:")
for thisComponent in typefriendWordComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
typefriendWordClock.reset(-_timeToFirstFrame)
frameN = -1

continueRoutine = True
while continueRoutine:
    t = typefinWordClock.getTime()
    frameN = frameN + 1
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name  # just the last key pressed
            enter.rt = _enter_allKeys[-1].rt
            continueRoutine = False
    if nameInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        nameInstructions.setAutoDraw(True) 
    if t >= 0.0 and friendWord.status == NOT_STARTED:
        friendWord.tStart = t
        friendWord.frameNStart = frameN
        friendWord.setAutoDraw(True)

    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            friendWord.text = friendWord.text + ' '
        elif 'backspace' in keys:
            friendWord.text = friendWord.text[:-1]
        elif 'apostrophe' in keys:
            friendWord.text = friendWord.text + "'"
        elif 'lshift' in keys or 'rshift'  in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                friendWord.text = friendWord.text + keys[0].upper()
                modify = False
            else:
                friendWord.text = friendWord.text + keys[0]
                
    if friendWord.text == '' and enter.keys != None:
        continueRoutine = True
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in typefriendWordComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine: 
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in typefriendWordComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "typefriend word"-------
for thisComponent in typefriendWordComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if enter.keys in ['', [], None]:
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
thisExp.addData('Friend Word', friendWord.text)
friendWord = friendWord.text
friendWordStr = str(friendWord)
print("Friend Word: ", friendWordStr)
thisExp.nextEntry()
routineTimer.reset()
regCueStr = []
def getRandomFromBucket():
    randomIndex = random.choice(bucket)
    print("random index from bucket = ", randomIndex)
    if randomIndex == "a" or randomIndex =="b" or randomIndex =="c" or randomIndex =="d":
        regCue.setText(finNameStr)

    if randomIndex == "i" or randomIndex == "j" or randomIndex == "k" or randomIndex == "l":
        regCue.setText(friendNameStr)

    if randomIndex == "e" or randomIndex =="f"or randomIndex =="g"or randomIndex =="h":
        regCue.setText(finWordStr)

    if randomIndex == "m" or randomIndex == "n" or randomIndex == "o" or randomIndex == "p":
        regCue.setText(friendWordStr)

    if randomIndex == "u" or randomIndex == "v" or randomIndex == "w" or randomIndex == "w" :
        regCue.setText("Choice")

    bucket.remove(randomIndex)
    return regCueStr
    print(regCueStr)
    print(bucket)

continueRoutine = True
space.keys = []
space.rt = []
_space_allKeys = []
Instructions3Components = [instructions5, space]
for thisComponent in Instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions3Clock = core.Clock()
Instructions3Clock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    t = Instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if instructions5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instructions5.setText("You will be completing 24 blocks of decisions, with each block consisting of 5 decisions.\n\nDuring each block of decisions, you will either see one of the words you typed, one of the names you typed, or the word 'Choice' in the center of the screen. \n\nPress SPACE to continue.")
        instructions5.setAutoDraw(True)

    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in Instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()

#end routine 
for thisComponent in Instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if space.keys in ['', [], None]:
    space.keys = None
thisExp.addData('space.keys',space.keys)
thisExp.nextEntry()
routineTimer.reset()

#instructions loops
instTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Insttext.csv'),
    seed=None)
thisExp.addLoop(instTrials)
thisTrial = instTrials.trialList[0]
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in instTrials:
    currentLoop = instTrials
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
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
    # reset timers
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
            inst5A.setText(ImagineText)
            inst5A.setColor(ColorText)
        if inst5B.status == NOT_STARTED:
            inst5B.setAutoDraw(True)
            inst5B.setText(PrimeText)
        waitOnFlip = False
        if space.status == NOT_STARTED:
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
Instructions4Clock=core.Clock()
Instructions4Components = [instructions6, space]
for thisComponent in Instructions4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions4Clock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    t = Instructions4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if instructions6.status == NOT_STARTED:
        win.timeOnFlip(instructions6, 'tStartRefresh')  # time at next scr refresh
        instructions6.setAutoDraw(True)
    waitOnFlip = False
    if space.status == NOT_STARTED:
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
    for thisComponent in Instructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()
#end routine
for thisComponent in Instructions4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if space.keys in ['', [], None]:
    space.keys = None
thisExp.nextEntry()
routineTimer.reset()

thisExp.addData('instructions6.started', instructions6.tStartRefresh)
thisExp.addData('instructions6.stopped', instructions6.tStopRefresh)

choiceResp = keyboard.Keyboard()
CueClock = core.Clock()
blank.setText("")


trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Rows.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "isi"-------
    continueRoutine = True
    isiFunc(3.000)
    if not bucket:
        trials.finished=True
        trials_2.finished=True
    getRandomFromBucket()
    print(bucket)
    print("regcue string=", regCue.text)
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TimeDivisions.csv', selection=Rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))

       
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        ChoiceClock=core.Clock()
        randomString=[]
        selectedVidStr = str(selectedVid)
        selectedTipStr = str(selectedTips)
        choiceSelection.keys = []
        choiceSelection.rt = []
        _choiceSelection_allKeys = []
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

        trialComponents = [andSignLeft, andSignRight, regCue, selectedVidImgLeft, selectedVidImgRight, selectedTipImgLeft, selectedTipImgRight, topLeftText, topLeftTime, topRightText, topRightTime, botLeftText, botLeftTime, botRightText, botRightTime, choiceSelection, blank]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            t = ChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  

            if regCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                regCue.frameNStart = frameN  # exact frame index
                regCue.tStart = t  # local t and not account for scr refresh
                regCue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(regCue, 'tStartRefresh')  # time at next scr refresh
                regCue.setAutoDraw(True)
            if regCue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > regCue.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    regCue.tStop = t  # not accounting for scr refresh
                    regCue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(regCue, 'tStopRefresh')  # time at next scr refresh
                    regCue.setAutoDraw(False)
            # *botLeftTime* updates
            if botLeftTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                botLeftTime.frameNStart = frameN  # exact frame index
                botLeftTime.tStart = t  # local t and not account for scr refresh
                botLeftTime.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(botLeftTime, 'tStartRefresh')  # time at next scr refresh
                botLeftTime.setAutoDraw(True)
            if botLeftTime.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > botLeftTime.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    botLeftTime.tStop = t  # not accounting for scr refresh
                    botLeftTime.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(botLeftTime, 'tStopRefresh')  # time at next scr refresh
                    botLeftTime.setAutoDraw(False)
            
            # *botRightTime* updates
            if botRightTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                botRightTime.frameNStart = frameN  # exact frame index
                botRightTime.tStart = t  # local t and not account for scr refresh
                botRightTime.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(botRightTime, 'tStartRefresh')  # time at next scr refresh
                botRightTime.setAutoDraw(True)
            if botRightTime.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > botRightTime.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    botRightTime.tStop = t  # not accounting for scr refresh
                    botRightTime.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(botRightTime, 'tStopRefresh')  # time at next scr refresh
                    botRightTime.setAutoDraw(False)
            
            # *topRightTime* updates
            if topRightTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                topRightTime.frameNStart = frameN  # exact frame index
                topRightTime.tStart = t  # local t and not account for scr refresh
                topRightTime.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(topRightTime, 'tStartRefresh')  # time at next scr refresh
                topRightTime.setAutoDraw(True)
            if topRightTime.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > topRightTime.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    topRightTime.tStop = t  # not accounting for scr refresh
                    topRightTime.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(topRightTime, 'tStopRefresh')  # time at next scr refresh
                    topRightTime.setAutoDraw(False)
            
            # *topLeftText* updates
            if topLeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                topLeftText.frameNStart = frameN  # exact frame index
                topLeftText.tStart = t  # local t and not account for scr refresh
                topLeftText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(topLeftText, 'tStartRefresh')  # time at next scr refresh
                topLeftText.setAutoDraw(True)
            if topLeftText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > topLeftText.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    topLeftText.tStop = t  # not accounting for scr refresh
                    topLeftText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(topLeftText, 'tStopRefresh')  # time at next scr refresh
                    topLeftText.setAutoDraw(False)
            
            # *topRightText* updates
            if topRightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                topRightText.frameNStart = frameN  # exact frame index
                topRightText.tStart = t  # local t and not account for scr refresh
                topRightText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(topRightText, 'tStartRefresh')  # time at next scr refresh
                topRightText.setAutoDraw(True)
            if topRightText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > topRightText.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    topRightText.tStop = t  # not accounting for scr refresh
                    topRightText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(topRightText, 'tStopRefresh')  # time at next scr refresh
                    topRightText.setAutoDraw(False)
            
            # *botLeftText* updates
            if botLeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                botLeftText.frameNStart = frameN  # exact frame index
                botLeftText.tStart = t  # local t and not account for scr refresh
                botLeftText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(botLeftText, 'tStartRefresh')  # time at next scr refresh
                botLeftText.setAutoDraw(True)
            if botLeftText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > botLeftText.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    botLeftText.tStop = t  # not accounting for scr refresh
                    botLeftText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(botLeftText, 'tStopRefresh')  # time at next scr refresh
                    botLeftText.setAutoDraw(False)
            
            # *botRightText* updates
            if botRightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                botRightText.frameNStart = frameN  # exact frame index
                botRightText.tStart = t  # local t and not account for scr refresh
                botRightText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(botRightText, 'tStartRefresh')  # time at next scr refresh
                botRightText.setAutoDraw(True)
            if botRightText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > botRightText.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    botRightText.tStop = t  # not accounting for scr refresh
                    botRightText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(botRightText, 'tStopRefresh')  # time at next scr refresh
                    botRightText.setAutoDraw(False)
            
            # *topLeftTime* updates
            if topLeftTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                topLeftTime.frameNStart = frameN  # exact frame index
                topLeftTime.tStart = t  # local t and not account for scr refresh
                topLeftTime.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(topLeftTime, 'tStartRefresh')  # time at next scr refresh
                topLeftTime.setAutoDraw(True)
            if topLeftTime.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > topLeftTime.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    topLeftTime.tStop = t  # not accounting for scr refresh
                    topLeftTime.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(topLeftTime, 'tStopRefresh')  # time at next scr refresh
                    topLeftTime.setAutoDraw(False)
                    


            # *SelectedVidLeft* updates
            if selectedVidImgLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                selectedVidImgLeft.frameNStart = frameN  # exact frame index
                selectedVidImgLeft.tStart = t  # local t and not account for scr refresh
                selectedVidImgLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(selectedVidImgLeft, 'tStartRefresh')  # time at next scr refresh
                selectedVidImgLeft.setAutoDraw(True)
            if selectedVidImgLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > selectedVidImgLeft.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    selectedVidImgLeft.tStop = t  # not accounting for scr refresh
                    selectedVidImgLeft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(selectedVidImgLeft, 'tStopRefresh')  # time at next scr refresh
                    selectedVidImgLeft.setAutoDraw(False)
            
            # *SelectedVidRight* updates
            if selectedVidImgRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                selectedVidImgRight.frameNStart = frameN  # exact frame index
                selectedVidImgRight.tStart = t  # local t and not account for scr refresh
                selectedVidImgRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(selectedVidImgRight, 'tStartRefresh')  # time at next scr refresh
                selectedVidImgRight.setAutoDraw(True)
            if selectedVidImgRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > selectedVidImgRight.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    selectedVidImgRight.tStop = t  # not accounting for scr refresh
                    selectedVidImgRight.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(selectedVidImgRight, 'tStopRefresh')  # time at next scr refresh
                    selectedVidImgRight.setAutoDraw(False)
            
            # *SelectedTipLeft* updates
            if selectedTipImgLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                selectedTipImgLeft.frameNStart = frameN  # exact frame index
                selectedTipImgLeft.tStart = t  # local t and not account for scr refresh
                selectedTipImgLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(selectedTipImgLeft, 'tStartRefresh')  # time at next scr refresh
                selectedTipImgLeft.setAutoDraw(True)
            if selectedTipImgLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > selectedTipImgLeft.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    selectedTipImgLeft.tStop = t  # not accounting for scr refresh
                    selectedTipImgLeft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(selectedTipImgLeft, 'tStopRefresh')  # time at next scr refresh
                    selectedTipImgLeft.setAutoDraw(False)
            
            # *SelectedTipRight* updates
            if selectedTipImgRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                selectedTipImgRight.frameNStart = frameN  # exact frame index
                selectedTipImgRight.tStart = t  # local t and not account for scr refresh
                selectedTipImgRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(selectedTipImgRight, 'tStartRefresh')  # time at next scr refresh
                selectedTipImgRight.setAutoDraw(True)
            if selectedTipImgRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > selectedTipImgRight.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    selectedTipImgRight.tStop = t  # not accounting for scr refresh
                    selectedTipImgRight.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(selectedTipImgRight, 'tStopRefresh')  # time at next scr refresh
                    selectedTipImgRight.setAutoDraw(False)
            
            # *choiceSelection* updates
            waitOnFlip = False
            if choiceSelection.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceSelection.frameNStart = frameN  # exact frame index
                choiceSelection.tStart = t  # local t and not account for scr refresh
                choiceSelection.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceSelection, 'tStartRefresh')  # time at next scr refresh
                choiceSelection.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choiceSelection.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choiceSelection.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choiceSelection.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > choiceSelection.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    choiceSelection.tStop = t  # not accounting for scr refresh
                    choiceSelection.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(choiceSelection, 'tStopRefresh')  # time at next scr refresh
                    choiceSelection.status = FINISHED
            if choiceSelection.status == STARTED and not waitOnFlip:
                theseKeys = choiceSelection.getKeys(keyList=['1', '2'], waitRelease=False)
                _choiceSelection_allKeys.extend(theseKeys)
                if len(_choiceSelection_allKeys):
                    choiceSelection.keys = _choiceSelection_allKeys[-1].name  # just the last key pressed
                    choiceSelection.rt = _choiceSelection_allKeys[-1].rt
            
            # *andSignLeft* updates
            if andSignLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                andSignLeft.frameNStart = frameN  # exact frame index
                andSignLeft.tStart = t  # local t and not account for scr refresh
                andSignLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(andSignLeft, 'tStartRefresh')  # time at next scr refresh
                andSignLeft.setAutoDraw(True)
            if andSignLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > andSignLeft.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    andSignLeft.tStop = t  # not accounting for scr refresh
                    andSignLeft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(andSignLeft, 'tStopRefresh')  # time at next scr refresh
                    andSignLeft.setAutoDraw(False)
            
            # *andSignRight* updates
            if andSignRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                andSignRight.frameNStart = frameN  # exact frame index
                andSignRight.tStart = t  # local t and not account for scr refresh
                andSignRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(andSignRight, 'tStartRefresh')  # time at next scr refresh
                andSignRight.setAutoDraw(True)
            if andSignRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > andSignRight.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    andSignRight.tStop = t  # not accounting for scr refresh
                    andSignRight.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(andSignRight, 'tStopRefresh')  # time at next scr refresh
                    andSignRight.setAutoDraw(False)
            
            # *blank* updates
            if blank.status == NOT_STARTED and asarray(choiceSelection.status == FINISHED):
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                    blank.setAutoDraw(False)
            if andSignLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                andSignLeft.frameNStart = frameN  # exact frame index
                andSignLeft.tStart = t  # local t and not account for scr refresh
                andSignLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(andSignLeft, 'tStartRefresh')  # time at next scr refresh
                andSignLeft.setAutoDraw(True)
            if andSignLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > andSignLeft.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    andSignLeft.tStop = t  # not accounting for scr refresh
                    andSignLeft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(andSignLeft, 'tStopRefresh')  # time at next scr refresh
                    andSignLeft.setAutoDraw(False)
            if andSignRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                andSignRight.frameNStart = frameN  # exact frame index
                andSignRight.tStart = t  # local t and not account for scr refresh
                andSignRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(andSignRight, 'tStartRefresh')  # time at next scr refresh
                andSignRight.setAutoDraw(True)
            if andSignRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > andSignRight.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    andSignRight.tStop = t  # not accounting for scr refresh
                    andSignRight.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(andSignRight, 'tStopRefresh')  # time at next scr refresh
                    andSignRight.setAutoDraw(False)

            if choiceSelection.keys == '1':
                randomString = "favoredTips"
            if choiceSelection.keys == '2':
                randomString  = "favoredVideo"
            
            if choiceSelection.keys == '1':
                topLeftText.setColor('green')
                topLeftTime.setColor('green')
                botLeftText.setColor('green')
                botLeftTime.setColor('green')
                andSignLeft.setColor("green")
                choiceSelection.status = FINISHED
            
            if choiceSelection.keys == '2':
                topRightText.setColor('green')
                topRightTime.setColor('green')
                botRightText.setColor('green')
                botRightTime.setColor('green')
                andSignRight.setColor("green")
                choiceSelection.status = FINISHED
            if choiceSelection.keys == '2' or choiceSelection.keys == '1':
                choiceSelection.status = FINISHED
            if blank.status == FINISHED:
                continueRoutine = False

            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('regCue', regCue.text)
#        trials.addData('botLeftTime.started', botLeftTime.tStartRefresh)
#        trials.addData('botLeftTime.stopped', botLeftTime.tStopRefresh)
#        trials.addData('botRightTime.started', botRightTime.tStartRefresh)
#        trials.addData('botRightTime.stopped', botRightTime.tStopRefresh)
#        trials.addData('topRightTime.started', topRightTime.tStartRefresh)
#        trials.addData('topRightTime.stopped', topRightTime.tStopRefresh)
#        trials.addData('topLeftText.started', topLeftText.tStartRefresh)
#        trials.addData('topLeftText.stopped', topLeftText.tStopRefresh)
#        trials.addData('topRightText.started', topRightText.tStartRefresh)
#        trials.addData('topRightText.stopped', topRightText.tStopRefresh)
#        trials.addData('botLeftText.started', botLeftText.tStartRefresh)
#        trials.addData('botLeftText.stopped', botLeftText.tStopRefresh)
#        trials.addData('botRightText.started', botRightText.tStartRefresh)
#        trials.addData('botRightText.stopped', botRightText.tStopRefresh)
#        trials.addData('topLeftTime.started', topLeftTime.tStartRefresh)
#        trials.addData('topLeftTime.stopped', topLeftTime.tStopRefresh)
#        trials.addData('SelectedVidLeft.started', selectedVidImgLeft.tStartRefresh)
#        trials.addData('SelectedVidLeft.stopped', selectedVidImgLeft.tStopRefresh)
#        trials.addData('SelectedVidRight.started', selectedVidImgRight.tStartRefresh)
#        trials.addData('SelectedVidRight.stopped', selectedVidImgRight.tStopRefresh)
#        trials.addData('SelectedTipLeft.started', selectedTipImgLeft.tStartRefresh)
#        trials.addData('SelectedTipLeft.stopped', selectedTipImgLeft.tStopRefresh)
#        trials.addData('SelectedTipRight.started', selectedTipImgRight.tStartRefresh)
#        trials.addData('SelectedTipRight.stopped', selectedTipImgRight.tStopRefresh)
#        trials.addData("Counter Code", counterCode)
        trials.addData("Random String", randomString)
        # check responses
        if choiceSelection.keys in ['', [], None]:  # No response was made
            choiceSelection.keys = None
        trials.addData('choiceSelection.keys',choiceSelection.keys)
        if choiceSelection.keys != None:  # we had a response
            trials.addData('choiceSelection.rt', choiceSelection.rt)
#        trials.addData('choiceSelection.started', choiceSelection.tStartRefresh)
#        trials.addData('choiceSelection.stopped', choiceSelection.tStopRefresh)
        if randomString == "favoredTips":
            selectedTipTime.append(MoreQuestionAmt1)
            selectedVidTime.append(LessGameAmt1)
            print("selected tip time:", selectedTipTime)
        if randomString == "favoredVideo":
            selectedTipTime.append(LessQuestionAmt1)
            print("selected tip time:", selectedTipTime)
            selectedVidTime.append(MoreGameAmt1)
#        trials.addData('andSignLeft.started', andSignLeft.tStartRefresh)
#        trials.addData('andSignLeft.stopped', andSignLeft.tStopRefresh)
#        trials.addData('andSignRight.started', andSignRight.tStartRefresh)
#        trials.addData('andSignRight.stopped', andSignRight.tStopRefresh)
#        trials.addData('blank.started', blank.tStartRefresh)
#        trials.addData('blank.stopped', blank.tStopRefresh)
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
        routineTimer.reset()
        
        # ------Prepare to start Routine "isi"-------
        continueRoutine = True
        isiFunc(2.000)
        thisExp.nextEntry()
        
#        if not bucket:
#            trials.finished=True
#            trials_2.finished=True
    # completed 1.0 repeats of 'trials'
    if not bucket:
        trials.finished=True
        trials_2.finished=True
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'



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
# reset timers
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
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')
        endText.setAutoDraw(True)
        endText.setText("Thank you for participating! \n\n One trial was selected at random, and in that trial you chose to allot the 20 minutes as: \n\n" + randomVidTimeStr + " minutes watching the videos, and \n\n" + randomTipTimeStr + " minutes reading financial tips.\n\n You will be reminded of this allotment at the end of the study, when you will be prompted to complete these activities. For now, please press ENTER to continue with the study." )
    waitOnFlip = False
    if enter.status == NOT_STARTED:
        enter.status = STARTED
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
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
