#CardTask

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys
from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.2.0'
expName = 'Experiment1'
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
    originPath='C:\\Users\\Jojo\\Downloads\\Helion Lab\\Experiment Files\\CardTask\\CardTaskFinal1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001


win = visual.Window(size=(1024, 768), fullscr=True, screen=0, winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True)
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

InstructionsClock = core.Clock()
Instructions = visual.TextStim(win=win, text='', font='Arial', pos=(0, 0), height=0.1, wrapWidth=1.25, color='white');
spaceKey = keyboard.Keyboard()

firstITIClock = core.Clock()
firstTrialITI = visual.TextStim(win=win,text='+',font='Arial',pos=(0, 0), height=0.15, color='white');

code_2Clock = core.Clock()
nRepsblock1=0
nRepsblock2=0

Reward_TrialClock = core.Clock()
polygon = visual.Rect(win=win,width=(0.6, 1)[0], height=(0.85, 1.3)[1],
    ori=0, pos=(0, 0),lineWidth=9, lineColor=[1,1,1], lineColorSpace='rgb',fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win,text='?',font='Arial', pos=(0, 0), height=0.18, color='white');
response2 = keyboard.Keyboard()
ISI = visual.TextStim(win=win,text='+',font='Arial',pos=(0, 0), height=0.15, color='white');

RewardOutcomeClock = core.Clock()
polygon2_2 = visual.Rect(win=win,width=(0.6, 1)[0], height=(0.85, 1.3)[1],
    ori=0, pos=(0, 0),lineWidth=9, lineColor=[1,1,1], lineColorSpace='rgb',fillColor=[0,0,0], fillColorSpace='rgb', opacity=1, depth=0.0, interpolate=True)
feedback1_2 = visual.TextStim(win=win, text='default', font='Arial',pos=(0, 0), height=0.16, color='white');
arrow1_2 = visual.TextStim(win=win, text='default',font='Arial', pos=(0, 0), height=0.16, wrapWidth=None, ori=0, color='white');
ITI_2 = visual.TextStim(win=win, text='+',font='Arial',pos=(0, 0), height=0.15, color='white');

Punishment_trialClock = core.Clock()
rectangle = visual.Rect(win=win, width=(0.6, 1)[0], height=(0.85, 1.3)[1], ori=0, pos=(0, 0),lineWidth=9, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb', opacity=1, depth=0.0, interpolate=True)
text1 = visual.TextStim(win=win, text='?',font='Arial', pos=(0, 0), height=0.18, color='white');
response3 = keyboard.Keyboard()
ISI2 = visual.TextStim(win=win,text='+',font='Arial', pos=(0, 0), height=0.15, color='white');

PunishmentOutcomeClock = core.Clock()
rectangle2_2 = visual.Rect(win=win, width=(0.6, 1)[0], height=(0.85, 1.3)[1], ori=0, pos=(0, 0), lineWidth=9, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], opacity=1, depth=0.0, interpolate=True)
feedback2_2 = visual.TextStim(win=win,text='default',font='Arial', pos=(0, 0), height=0.16, color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1);
arrow2_2 = visual.TextStim(win=win,text='default', font='Arial', units='norm', pos=(-0.02, 0), height=0.16, wrapWidth=0.2, color='white', colorSpace='rgb', opacity=1);
ITI2_2 = visual.TextStim(win=win, text='+', font='Arial', pos=(0, 0), height=0.15, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, depth=-3.0);

EndTextClock = core.Clock()
Finished = visual.TextStim(win=win,text='Thank you for playing, you earned $4.00!',
    font='Arial', pos=(0, 0), height=0.14, wrapWidth=None, color='white');
key_resp_2 = keyboard.Keyboard()

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

textArray=["In this part of the study, you will be playing a simple card-guessing game in which you will have the chance to earn some money.\n\nPress SPACE for more instructions.", "Your job is to guess if a card shown on screen will have a value of less than five (1, 2, 3, 4) or greater than five (6, 7, 8, 9).\n\n When you see a rectangle with a question mark in it, make your guess! \n\n Press SPACE for more instructions.", \
    "You will only have 4 seconds to make your guess once you see the question mark appear on the screen. \nYou can press the \'1\' key to guess that a card will have a value less than five, or press the \'2\' key to guess a value greater than five.\n\nPress SPACE to continue.", \
    "After making your guess, the value of the card will be revealed.\n\nIf your guess was correct, you will win $0.50. \nIf your guess was incorrect, you will lose $0.25. \n\nThe money you earn in this task is real money and will be used as a bonus in a later task.\n\nPress SPACE to continue. ",\
    "Again, you can press the \'1\' key for a guess of less than five, or the \'2\' key for a guess of greater than five.\n\nWhen you are ready to begin the task, press SPACE!"]
for i in textArray:
    introFunc(i)



def isiFunc(time):
    routineTimer.add(time)
    firstITIComponents = [firstTrialITI]
    for thisComponent in firstITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firstITIClock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True

    while continueRoutine and routineTimer.getTime() > 0:
        t = firstITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firstITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if firstTrialITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            firstTrialITI.frameNStart = frameN
            firstTrialITI.tStart = t
            firstTrialITI.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(firstTrialITI, 'tStartRefresh')
            firstTrialITI.setAutoDraw(True)
        if firstTrialITI.status == STARTED:
            if tThisFlipGlobal > firstTrialITI.tStartRefresh + time-frameTolerance:
                firstTrialITI.tStop = t 
                firstTrialITI.frameNStop = frameN
                win.timeOnFlip(firstTrialITI, 'tStopRefresh')
                firstTrialITI.setAutoDraw(False)
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in firstITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
                
        if continueRoutine:
            win.flip()

    for thisComponent in firstITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


isiFunc(6.000)

alltrials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('spreadsheet5.xlsx'),
    seed=None, name='alltrials')
thisExp.addLoop(alltrials)
thisAlltrial = alltrials.trialList[0]
if thisAlltrial != None:
    for paramName in thisAlltrial:
        exec('{} = thisAlltrial[paramName]'.format(paramName))

for thisAlltrial in alltrials:
    currentLoop = alltrials
    if thisAlltrial != None:
        for paramName in thisAlltrial:
            exec('{} = thisAlltrial[paramName]'.format(paramName))
    
    if selectBlock==1:
     nRepsblock1=1
     nRepsblock2=0
    elif selectBlock==2:
     nRepsblock1=0
     nRepsblock2=1
    code_2Components = []
    for thisComponent in code_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    code_2Clock.reset(-_timeToFirstFrame)
    frameN = -1
    continueRoutine = True
    
    while continueRoutine:
        t = code_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=code_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in code_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    for thisComponent in code_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    routineTimer.reset()
    
    Reward = data.TrialHandler(nReps=nRepsblock1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Reward')
    thisExp.addLoop(Reward)
    thisReward = Reward.trialList[0]
    if thisReward != None:
        for paramName in thisReward:
            exec('{} = thisReward[paramName]'.format(paramName))
    
    for thisReward in Reward:
        currentLoop = Reward
        if thisReward != None:
            for paramName in thisReward:
                exec('{} = thisReward[paramName]'.format(paramName))
        
        routineTimer.add(4.000000)
        response2.keys = []
        response2.rt = []
        Reward_TrialComponents = [polygon, text, response2, ISI]
        for thisComponent in Reward_TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Reward_TrialClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = Reward_TrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Reward_TrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                polygon.frameNStart = frameN
                polygon.tStart = t
                polygon.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(polygon, 'tStartRefresh')
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                if tThisFlipGlobal > polygon.tStartRefresh + 2.0-frameTolerance:
                    polygon.tStop = t
                    polygon.frameNStop = frameN
                    win.timeOnFlip(polygon, 'tStopRefresh')
                    polygon.setAutoDraw(False)
            
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text.frameNStart = frameN
                text.tStart = t 
                text.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(text, 'tStartRefresh')
                text.setAutoDraw(True)
            if text.status == STARTED:
                if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                    text.tStop = t
                    text.frameNStop = frameN
                    win.timeOnFlip(text, 'tStopRefresh')
                    text.setAutoDraw(False)
            
            waitOnFlip = False
            if response2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                response2.frameNStart = frameN
                response2.tStart = t
                response2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(response2, 'tStartRefresh')
                response2.status = STARTED
                waitOnFlip = True
                win.callOnFlip(response2.clock.reset)
                win.callOnFlip(response2.clearEvents, eventType='keyboard')
            if response2.status == STARTED:
                if tThisFlipGlobal > response2.tStartRefresh + 2.0-frameTolerance:
                    response2.tStop = t
                    response2.frameNStop = frameN
                    win.timeOnFlip(response2, 'tStopRefresh')
                    response2.status = FINISHED
            if response2.status == STARTED and not waitOnFlip:
                theseKeys = response2.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]
                    
                    if "escape" == theseKeys:
                        endExpNow = True
                    response2.keys = theseKeys.name
                    response2.rt = theseKeys.rt
            
            if ISI.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                ISI.frameNStart = frameN
                ISI.tStart = t
                ISI.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(ISI, 'tStartRefresh')
                ISI.setAutoDraw(True)
            if ISI.status == STARTED:
                if tThisFlipGlobal > ISI.tStartRefresh + 2.0-frameTolerance:
                    ISI.tStop = t
                    ISI.frameNStop = frameN
                    win.timeOnFlip(ISI, 'tStopRefresh')
                    ISI.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in Reward_TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in Reward_TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        if response2.keys in ['', [], None]:
            response2.keys = None
        Reward.addData('response2.keys',response2.keys)
        if response2.keys != None:
            Reward.addData('response2.rt', response2.rt)

        outcome = []
        if response2.keys == '1':
            outcome = np.random.randint(1,4);
        elif response2.keys == '2':
            outcome = np.random.randint(6,9);
        else:
            outcome = "No Response";
        
        money = []
        color = []
        if response2.keys == '1':
            money = '+$0.50';
            color = [-1.0,1.0,-1.0];
        elif response2.keys == '2':
            money = '+$0.50';
            color = [-1.0,1.0,-1.0];
        else:
            money = '#';
            color = [1.0,1.0,1.0];

        
        routineTimer.add(4.000000)
        arrow1_2.setColor(color, colorSpace='rgb')
        arrow1_2.setText(money)
        RewardOutcomeComponents = [polygon2_2, feedback1_2, arrow1_2, ITI_2]
        for thisComponent in RewardOutcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RewardOutcomeClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = RewardOutcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RewardOutcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if polygon2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                polygon2_2.frameNStart = frameN
                polygon2_2.tStart = t
                polygon2_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(polygon2_2, 'tStartRefresh')
                polygon2_2.setAutoDraw(True)
            if polygon2_2.status == STARTED:
                if tThisFlipGlobal > polygon2_2.tStartRefresh + 2-frameTolerance:
                    polygon2_2.tStop = t
                    polygon2_2.frameNStop = frameN
                    win.timeOnFlip(polygon2_2, 'tStopRefresh')
                    polygon2_2.setAutoDraw(False)
            
            if feedback1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                feedback1_2.frameNStart = frameN
                feedback1_2.tStart = t
                feedback1_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(feedback1_2, 'tStartRefresh')
                feedback1_2.setAutoDraw(True)
            if feedback1_2.status == STARTED:
                if tThisFlipGlobal > feedback1_2.tStartRefresh + 1-frameTolerance:
                    feedback1_2.tStop = t
                    feedback1_2.frameNStop = frameN
                    win.timeOnFlip(feedback1_2, 'tStopRefresh')
                    feedback1_2.setAutoDraw(False)
            if feedback1_2.status == STARTED:
                feedback1_2.setText(outcome, log=False)
            
            if arrow1_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                arrow1_2.frameNStart = frameN
                arrow1_2.tStart = t
                arrow1_2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(arrow1_2, 'tStartRefresh')
                arrow1_2.setAutoDraw(True)
            if arrow1_2.status == STARTED:
                if tThisFlipGlobal > arrow1_2.tStartRefresh + 1.0-frameTolerance:
                    arrow1_2.tStop = t
                    arrow1_2.frameNStop = frameN
                    win.timeOnFlip(arrow1_2, 'tStopRefresh')
                    arrow1_2.setAutoDraw(False)
            
            if ITI_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                ITI_2.frameNStart = frameN
                ITI_2.tStart = t
                ITI_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(ITI_2, 'tStartRefresh')
                ITI_2.setAutoDraw(True)
            if ITI_2.status == STARTED:
                if tThisFlipGlobal > ITI_2.tStartRefresh + 2.0-frameTolerance:
                    ITI_2.tStop = t
                    ITI_2.frameNStop = frameN
                    win.timeOnFlip(ITI_2, 'tStopRefresh')
                    ITI_2.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in RewardOutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break 
                    
            if continueRoutine:
                win.flip()
        
        for thisComponent in RewardOutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        

    Loss = data.TrialHandler(nReps=nRepsblock2, method='random', extraInfo=expInfo, originPath=-1, trialList=[None], seed=None, name='Loss')
    thisExp.addLoop(Loss)
    thisLos = Loss.trialList[0]
    if thisLos != None:
        for paramName in thisLos:
            exec('{} = thisLos[paramName]'.format(paramName))
    
    for thisLos in Loss:
        currentLoop = Loss
        if thisLos != None:
            for paramName in thisLos:
                exec('{} = thisLos[paramName]'.format(paramName))
        
        routineTimer.add(4.000000)
        response3.keys = []
        response3.rt = []
        Punishment_trialComponents = [rectangle, text1, response3, ISI2]
        for thisComponent in Punishment_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Punishment_trialClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = Punishment_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Punishment_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1 

            if rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                rectangle.frameNStart = frameN
                rectangle.tStart = t
                rectangle.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rectangle, 'tStartRefresh')
                rectangle.setAutoDraw(True)
            if rectangle.status == STARTED:
                if tThisFlipGlobal > rectangle.tStartRefresh + 2-frameTolerance:
                    rectangle.tStop = t
                    rectangle.frameNStop = frameN
                    win.timeOnFlip(rectangle, 'tStopRefresh')
                    rectangle.setAutoDraw(False)
            
            if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text1.frameNStart = frameN
                text1.tStart = t
                text1.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(text1, 'tStartRefresh')
                text1.setAutoDraw(True)
            if text1.status == STARTED:
                if tThisFlipGlobal > text1.tStartRefresh + 2.0-frameTolerance:
                    text1.tStop = t
                    text1.frameNStop = frameN
                    win.timeOnFlip(text1, 'tStopRefresh')
                    text1.setAutoDraw(False)
            
            waitOnFlip = False
            if response3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                response3.frameNStart = frameN
                response3.tStart = t
                response3.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(response3, 'tStartRefresh')
                response3.status = STARTED
                waitOnFlip = True
                win.callOnFlip(response3.clock.reset)
                win.callOnFlip(response3.clearEvents, eventType='keyboard')
            if response3.status == STARTED:
                if tThisFlipGlobal > response3.tStartRefresh + 2-frameTolerance:
                    response3.tStop = t
                    response3.frameNStop = frameN
                    win.timeOnFlip(response3, 'tStopRefresh')
                    response3.status = FINISHED
            if response3.status == STARTED and not waitOnFlip:
                theseKeys = response3.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]
                    
                    if "escape" == theseKeys:
                        endExpNow = True
                    response3.keys = theseKeys.name
                    response3.rt = theseKeys.rt
            
            if ISI2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                ISI2.frameNStart = frameN
                ISI2.tStart = t
                ISI2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(ISI2, 'tStartRefresh')
                ISI2.setAutoDraw(True)
            if ISI2.status == STARTED:
                if tThisFlipGlobal > ISI2.tStartRefresh + 2-frameTolerance:
                    ISI2.tStop = t
                    ISI2.frameNStop = frameN
                    win.timeOnFlip(ISI2, 'tStopRefresh') 
                    ISI2.setAutoDraw(False)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in Punishment_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            if continueRoutine:
                win.flip()
        
        for thisComponent in Punishment_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        if response3.keys in ['', [], None]:
            response3.keys = None
        Loss.addData('response3.keys',response3.keys)
        if response3.keys != None:
            Loss.addData('response3.rt', response3.rt)
        outcome = []
        if response3.keys == '1':
            outcome = np.random.randint(6,9);
        elif response3.keys == '2':
            outcome = np.random.randint(1,4);
        else:
            outcome = "No Response";
        
        money = []
        color = []
        if response3.keys == '1':
            money = '-$0.25';
            color = [1.0,-1.0,-1.0];
        elif response3.keys == '2':
            money = '-$0.25';
            color = [1.0,-1.0,-1.0];
        else:
            money = '#';
            color = [1.0,1.0,1.0];
        
        routineTimer.add(4.000000)
        feedback2_2.setText(outcome)
        arrow2_2.setColor(color, colorSpace='rgb')
        arrow2_2.setText(money)
        PunishmentOutcomeComponents = [rectangle2_2, feedback2_2, arrow2_2, ITI2_2]
        for thisComponent in PunishmentOutcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PunishmentOutcomeClock.reset(-_timeToFirstFrame)
        frameN = -1
        continueRoutine = True
        
        while continueRoutine and routineTimer.getTime() > 0:
            t = PunishmentOutcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PunishmentOutcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            
            if rectangle2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                rectangle2_2.frameNStart = frameN 
                rectangle2_2.tStart = t
                rectangle2_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rectangle2_2, 'tStartRefresh') 
                rectangle2_2.setAutoDraw(True)
            if rectangle2_2.status == STARTED:
                if tThisFlipGlobal > rectangle2_2.tStartRefresh + 2-frameTolerance:
                    rectangle2_2.tStop = t  
                    rectangle2_2.frameNStop = frameN 
                    win.timeOnFlip(rectangle2_2, 'tStopRefresh') 
                    rectangle2_2.setAutoDraw(False)
            
            if feedback2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                feedback2_2.frameNStart = frameN 
                feedback2_2.tStart = t  
                feedback2_2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(feedback2_2, 'tStartRefresh') 
                feedback2_2.setAutoDraw(True)
            if feedback2_2.status == STARTED:
                if tThisFlipGlobal > feedback2_2.tStartRefresh + 1.0-frameTolerance:
                    feedback2_2.tStop = t 
                    feedback2_2.frameNStop = frameN 
                    win.timeOnFlip(feedback2_2, 'tStopRefresh')
                    feedback2_2.setAutoDraw(False)
            
            if arrow2_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                arrow2_2.frameNStart = frameN
                arrow2_2.tStart = t  
                arrow2_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(arrow2_2, 'tStartRefresh')
                arrow2_2.setAutoDraw(True)
            if arrow2_2.status == STARTED:
                if tThisFlipGlobal > arrow2_2.tStartRefresh + 1.0-frameTolerance:
                    arrow2_2.tStop = t 
                    arrow2_2.frameNStop = frameN
                    win.timeOnFlip(arrow2_2, 'tStopRefresh')
                    arrow2_2.setAutoDraw(False)
            
            if ITI2_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                ITI2_2.frameNStart = frameN
                ITI2_2.tStart = t 
                ITI2_2.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(ITI2_2, 'tStartRefresh')
                ITI2_2.setAutoDraw(True)
            if ITI2_2.status == STARTED:
                if tThisFlipGlobal > ITI2_2.tStartRefresh + 2.0-frameTolerance:
                    ITI2_2.tStop = t
                    ITI2_2.frameNStop = frameN
                    win.timeOnFlip(ITI2_2, 'tStopRefresh')
                    ITI2_2.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in PunishmentOutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            
            if continueRoutine:
                win.flip()
        
        for thisComponent in PunishmentOutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
   
    thisExp.nextEntry()

isiFunc(15.000)

key_resp_2.keys = []
key_resp_2.rt = []
EndTextComponents = [Finished, key_resp_2]
for thisComponent in EndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndTextClock.reset(-_timeToFirstFrame)
frameN = -1
continueRoutine = True

while continueRoutine:
    t = EndTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1 
    
    if Finished.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        Finished.frameNStart = frameN
        Finished.tStart = t
        Finished.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(Finished, 'tStartRefresh')
        Finished.setAutoDraw(True)
    
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]
            
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name
            key_resp_2.rt = theseKeys.rt
            continueRoutine = False
    
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

if key_resp_2.keys in ['', [], None]:
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
routineTimer.reset()

win.flip()
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
