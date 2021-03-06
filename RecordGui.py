#!/usr/bin/python

##############################################################################
##
## File: RecordGui.py
## Authors: James Kuczynski <jkuczyns@cs.uml.edu>
##          Joshua Rodriguez <jrodrig1@cs.uml.edu>
## File Description: This file is the frontend which allows the user to
##                   train the AI with audio input.
##
## Created: 11/10/2016 by J.K.
## Last Modified: 11/10/2016 by J.K.
##
##############################################################################

import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import PitchDetection
import threading


class RecordGui(QWidget):
    def __init__(self):
        super(RecordGui, self).__init__()
        self.initUi()
        self.scale = []

    """
    " Set up the UI elements.
    """
    def initUi(self):

        # internal representation of the layout is in grid format.
        self.outerLayout = QGridLayout()

        self.heardInput = QLineEdit()

        # create the buttons
        self.recordBtn = QPushButton("Record")
        self.stopBtn = QPushButton("Stop")
        self.playbackBtn = QPushButton("Playback")
        self.saveBtn = QPushButton("Save")
        self.rejectBtn = QPushButton("Reject")

        # connect the buttons with their callback functions
        self.recordBtn.clicked.connect(self.recordBtnSlot)
        self.stopBtn.clicked.connect(self.stopBtnSlot)
        self.playbackBtn.clicked.connect(self.playbackBtnSlot)
        self.saveBtn.clicked.connect(self.saveBtnSlot)
        self.rejectBtn.clicked.connect(self.rejectBtnSlot)

        # add the elements to the layout
        self.outerLayout.addWidget(self.heardInput, 0, 0, 1, 2, Qt.AlignCenter)
        self.outerLayout.addWidget(self.recordBtn, 1, 0)
        self.outerLayout.addWidget(self.stopBtn, 1, 1)
        self.outerLayout.addWidget(self.playbackBtn, 2, 0, 1, 2)
        self.outerLayout.addWidget(self.saveBtn, 3, 0)
        self.outerLayout.addWidget(self.rejectBtn, 3, 1)

        # add the layout to the outermost widget
        self.setLayout(self.outerLayout)


    """
    " Triggered when the Record button is pressed.  Starts recording.
    " @#see recordBtn
    """
    def recordBtnSlot(self):
        print "recordBtn was clicked"

        if len(self.scale) < 7:
            self.listen()
        else:
            print "7 notes have been recorded -- Xavier is sticking his fingers in his ears now"

    def listen(self):
        detector = PitchDetection.PitchDetection(self)

        #for i in range(7):
        note = detector.detect()
        self.appendNoteToUi(note + " ")
        self.scale.append(note)



    def appendNoteToUi(self, text):
        self.heardInput.setText(self.heardInput.text() + text)


    """
    " Triggered when the Stop button is pressed.  Stops recording.
    "
    """
    def stopBtnSlot(self):
        print "stop recording"


    """
    " Triggered when the Playback button is pressed.  Plays the current
    " scale to the user.
    """
    def playbackBtnSlot(self):
        print "playback"


    """
    " Triggered when the Save button is pressed.  Saves the current
    " note analyzed
    """
    def saveBtnSlot(self):
        print "save note/scale"


    """
    " Triggered when the Reject button is pressed.  Deletes the current
    " note analyzed and prepares to re-record it.
    """
    def rejectBtnSlot(self):
        print "reject note"
        self.scale = []
        self.heardInput.setText("")