import csv
import os
import time
import random
from tkinter import *
import pyperclip
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from tkinter.filedialog import askopenfilename
import datetime
from datetime import datetime
import sys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import Request, urlopen
from random import choice

greetings1 = ["Hi ", "Hello "]
greetings2 = ["Hi ", "Hello ", "Good Morning ", "Morning "]
greetings3 = ["Hi ", "Hello ", "Good Afternoon ", "Afternoon"]
greetings4 = ["Hi ", "Hello ", "Good Evening ", "Evening "]

hour = datetime.now().hour

if 5 <= int(hour) <= 11:
    print(random.choice(greetings1 + greetings2))
elif 12 <= int(hour) <= 17:
    print(random.choice(greetings1 + greetings3))
elif 18 <= int(hour) <= 22:
    print(random.choice(greetings1 + greetings4))
else:
    print(random.choice(greetings1))

