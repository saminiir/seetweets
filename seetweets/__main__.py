#! /usr/bin/env python
#coding: utf8

'''
Created on Jan 22, 2013

Main class for the SeeTweets-application. Serves only as an entry point for the software -
Invokes the SeeTweets-Controller

@author: sailniir
'''
import sys
import os
import logging

#This is kind of a hack and isn't really the preferred way to set up the python interpreter
path = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(os.path.join(os.path.dirname(__file__), path))

from main.Controller import Controller

logging.basicConfig(level=logging.DEBUG)

controller = Controller()
controller.invoke()