#! /usr/bin/env python

'''
Created on Jan 22, 2013

Main class for the SeeTweets-application

@author: sailniir
'''
from seetweets.main.Controller import Controller
from Tkinter import Tk
from seetweets.main.gui.TweetPopup import TweetPopup
from seetweets.main.Tweet import Tweet

controller = Controller()
controller.invoke()

#root = Tk()

#tweet = Tweet(tid=124512, hashtag="lollero", time="16:25", author="Sami Niiranen", text="Hehehe mitas tassa nyt vois testata etta toimiiko taahahahahah")

#popup = TweetPopup(tweet)

#root.mainloop()

