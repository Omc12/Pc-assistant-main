#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pywhatkit
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser
import tkinter as tk
import ctypes
import color
import time
import requests
import os
import winshell
import warnings
import indic_transliteration
import flask_googletrans
import subprocess
import shutil
import json
import random
import operator
import numpy as np
import cv2
import win32com.client as wincl
from urllib.request import urlopen
from time import ctime
from color import color
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import wolframalpha
from tkinter import messagebox
from kivy.app import App
from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from googletrans import Translator

warnings.filterwarnings('ignore')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', NONE, webbrowser.BackgroundBrowser(chrome_path))

def talk(text):
    engine.say(text)
    #engine.runAndWait()
    engine.runAndWait()

def speak(self, output):
        # initiating the speech engine
        engine = pyttsx3.init()
        # speaking the desired output
        engine.say(output)
        #engine.runAndWait()
        engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'assistant' in command:
         run_assistant()

    except:
        pass
    return command

class run_assistant(App):
 def build(self):
    talk("How can i Help you")
    print("Assistant Running..!")
    talk("Please speak now")
    command = take_command()
    print(command)

    #if 'exit' in command:
        # talk('quiting')
         #run_assistant.quit(0)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        webbrowser.register('chrome', NONE, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome")
        webbrowser.open_new_tab("")
        pywhatkit.playonyt(song)

    #elif 'is+time' in command:
     #   istime = datetime.datetime.now().strftime('%I:%M %p')
      #  print(time)
       # talk('Current time is ' + time)

    elif "time" in command:
       listening = True
       talk(ctime())

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how' in command:
        person = command.replace('how', 'how')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what', 'what')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'where' in command:
        person = command.replace('where', 'where')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'info' in command:
        person = command.replace('information', 'info', 'information')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'can' in command:
        person = command.replace('can', 'can')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'help' in command:
        person = command.replace('help', 'help')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell' in command:
        person = command.replace('tell', 'tell')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'search' in command:
        person = command.replace("search", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'are you my personal assistant' in command:
        talk("Yes, I am your personal assistant")

    elif "change my name to" in command:
        command = command.replace("change my name to", "")
        name = command

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.get('chrome').open("youtube.com")

    elif 'open google' in command:
        talk("Here you go to google\n")
        webbrowser.get('chrome').open("google.com")

    elif 'open stack overflow' in command:
        talk("Here you go to stackoverflow\n")
        webbrowser.get('chrome').open("stackoverflow.com")

    elif 'open opera' in command:
        talk("Here you go to opera\n")
        webbrowser.get('chrome').open("opera.com")

    elif 'open gmail' in command:
        talk("Here you go to gmail\n")
        webbrowser.get('chrome').open("gmail.com")

    elif 'open email' in command:
        talk("Here you go to email\n")
        webbrowser.get('chrome').open("email.com")

    elif 'open amazon' in command:
        talk("Here you go to amazon.in\n")
        webbrowser.get('chrome').open("amazon.in")

    elif 'open fortnite dot com' in command:
        talk("Here you go to fortnite.com\n")
        webbrowser.get('chrome').open("fortnite.com")

    elif 'open topper' in command:
        talk("Here you go to topper\n")
        webbrowser.get('chrome').open("toppr.com")

    elif 'open top answer' in command:
        talk("Here you go to topper Answer\n")
        webbrowser.get('chrome').open("toppr.com/ask")

    elif 'open whatsapp' in command:
        talk("Here you go to whatsapp\n")
        webbrowser.get('chrome').open("web.whatsapp.com")

    elif "camera" in command or "take a photo" in command:
        ec.capture(0, " CamZ ", "img.jpg")

    #elif 'shutdown' in command:
        #talk("Hold On a Sec ! Your system is on its way to shut down")
       # os.system('shutdown /l')

    #elif "restart" in command:
        #os.system(["shutdown", "/r"]);

    #elif "hibernate" in command or "sleep" in command:
        #talk("Hibernating")
       # os.system("shutdown / s");

    #elif "log off" in command or "sign out" in command:
      #  talk("Make sure all the application are closed before sign-out")
     #   time.sleep(5)
    #    os.system(["shutdown", "/l"]);

    elif "good morning" in command:
        talk("A warm" + command)
        talk("How are you oom")

    elif "good afternoon" in command:
        talk("" + command)
        talk("How are you oom")

    elif "good evening" in command:
        talk("same to you")
        talk("How are you oom")

    elif "good night" in command:
        talk("good night")
        talk("How are you oom")

    elif "exit" in command:
        talk("are you sure")
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        root.title("CHROMA")
        root.geometry('200x80')

        button1 = tk.Button(frame, text="START", fg="white", command=run_assistant, bd=0, bg='black', padx='50px')
        button1.bind("button1")
        button1.pack(side=tk.LEFT)
        button2 = tk.Button(root, text=".QUIT.", fg="white", command=quit, bd=0, bg='black', padx='50px')
        button2.bind("button1")
        button2.pack(side=tk.LEFT)
        button2.place(x=15, y=50)
        button2.bind("button2")
        root.mainloop()
        talk('quiting')
    else:
        talk('Please say it again')

while True:
    run_assistant()

