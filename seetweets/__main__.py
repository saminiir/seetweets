#! /usr/bin/env python
#coding: utf8

'''
Created on Jan 22, 2013

Main class for the SeeTweets-application

@author: sailniir
'''
# boilerplate to allow running as script directly
#if __name__ == "__main__" and __package__ is None:
#    import sys, os
    # The following assumes the script is in the top level of the package
    # directory.  We use dirname() to help get the parent directory to add to
    # sys.path, so that we can import the current package.  This is necessary 
    # since when invoked directly, the 'current' package is not automatically
    # imported.
#    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    sys.path.insert(0, parent_dir)
#    __package__ = str("main")
#    del sys, os

import sys
import os


path = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(os.path.join(os.path.dirname(__file__), path))

from main.Controller import Controller
from Tkinter import Tk, Frame
from main.Tweet import Tweet
from main.gui.TweetPopup import TweetPopup


#controller = Controller()
#controller.invoke()

root = Tk()
#text = "Keskipitunen teksti, jossa suomalaisiakin aakkasia jonkin verran :-)"
text = "Testailen tätä TweetPopuppia sikapitkillälauseillajotkavoisivatrikkoaxxxxxxxxxxxxxxxxx toiminnallisuuden"

frame = Frame(root)
#print len(text)

tweet = Tweet(tid=124512, hashtag="lollero", time="16:25", author="Sami Niiranen", text=text)

popup = TweetPopup(tweet)

root.mainloop()

