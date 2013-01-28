#! /usr/bin/env python
#coding: utf8

'''
Created on Jan 22, 2013

Main class for the SeeTweets-application

@author: sailniir
'''
import sys
import os

path = os.path.join(os.path.dirname(__file__), "..")
print path
#sys.path.append(os.path.join(os.path.dirname(__file__), path))
sys.path.append("/home/sami/sami/code/seetweets/seetweets/main/")

from seetweets.main.Controller import Controller
from Tkinter import Tk
from seetweets.main.gui.TweetPopup import TweetPopup
from seetweets.main.Tweet import Tweet


controller = Controller()
controller.invoke()

#root = Tk()

#text = "testaan etta toimiiko taa mitenkaa jarkevastia sease aädasäsdä awddaw aägeägegäa easä gaä äs äafsä asäfasäf aes eas faes feas"
#text = "test"
#text = "Keskipitunen teksti, jossa suomalaisiakin aakkasia jonkin verran :-)"

#print len(text)

#tweet = Tweet(tid=124512, hashtag="lollero", time="16:25", author="Sami Niiranen", text=text)

#popup = TweetPopup(tweet)

#root.mainloop()

