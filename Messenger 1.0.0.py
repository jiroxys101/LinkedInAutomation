import csv
import os
import time
import unittest
import random
from tkinter import *
import pyperclip
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import logging
import atexit
import smtplib
import ssl
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
import re
import pickle
from pynput.mouse import Listener

smtp_server = 'smtp.gmail.com'

d = datetime.now().strftime("%I:%M %p")
port = 465
notification_password = 'RDMSSK6247!'
sender_email = 'notifications.webtrafik@gmail.com'
receiver_email = 'jiroxys101@gmail.com'

context = ssl.create_default_context()
print(d)

# current
log_in = {"Rijul Kumar": ["rijulkumar.webtrafik@gmail.com", "Gocam2020"],
          "Omotayo Ogunnusi": ["tayoogunnusi@outlook.com", "Temitope5"],
          "Rijul K": ["rijulkumar7500@gmail.com", "nov192011"],
          "Prasad Pansare": ["prasadpansare2019@gmail.com", "Gocam2020"],
          "Dieudonné Ndjebayi": ["rijul.kumar@construction.com", "Gocam2020"],
          "Sushma Kumar": ["sush126.kumar@gmail.com", "Dmnd2017"],
          }

user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
]

master = Tk()

variable1 = StringVar(master)

variable1.set("")  # default value
w = OptionMenu(master, variable1, "Rijul Kumar", "Omotayo Ogunnusi", "Rijul K", "Prasad Pansare", "Dieudonné Ndjebayi",
               "Sushma Kumar")
w.pack()

name_var = ""
email_var = ""
pw_var = ""


def ok():
    if variable1.get() in log_in:
        global name_var
        name_var = variable1.get()
        if name_var == "Rijul K":
            name_var = "Rijul Kumar"
        global email_var
        email_var = log_in.get(variable1.get(), "")[0]
        global pw_var
        pw_var = log_in.get(variable1.get(), "")[1]
        print("Name: ", name_var)
        print("E-Mail: ", email_var)
        print("Password: ", pw_var)

    master.quit()
    master.destroy()


button1 = Button(master, text="OK", command=ok)
button1.pack()

mainloop()

results = []
errors = []

options = webdriver.ChromeOptions()
user_agent = random.choice(user_agent_list)

bunji = os.getenv("USERNAME")
# userProfile = "C:\\Users\\jirox_000\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
# userProfile = "C:\\Users\\" + bunji + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
options.add_experimental_option("excludeSwitches",
                                ["ignore-certificate-errors", "safebrowsing-disable-download-protection",
                                 "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
# options.add_argument("user-data-dir={}".format(userProfile))
options.add_argument('--disable-extensions')
# options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920x1080")
options.add_argument(f'user-agent={user_agent}')
chrome_driver = "C:\Webdrivers\\chromedriver.exe"


def setup():
    driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
    driver.get('https://www.google.com')
    driver.set_page_load_timeout(600)

    actions = ActionChains(driver)

    username = str(email_var)
    password = str(pw_var)
    email_field_id = "username"
    pass_field_id = "password"
    login_button_xpath = "//button[contains(@type,'submit')]"
    agent = driver.execute_script("return navigator.userAgent")
    print(str(agent))
    print("Logging in...", end=" | ")
    driver.save_screenshot('screenie.png')

    cookies = pickle.load(open(str(email_var) + ".pkl", "rb"))
    for cookie in cookies:
        if 'expiry' in cookie:
            cookie.pop('expiry')  # cookie['expires'] = cookie.pop('expiry')
        driver.add_cookie(cookie)
    driver.get('https://www.linkedin.com/feed/')
    logo_x_path = "(//span[contains(@id, 'feed-tab-icon')])"
    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(logo_x_path))
    print("Log in successful")

    # time.sleep(60)
    count1 = 0  # counter to loop through array of links
    count2 = 0  # error counter
    count3 = 0  # sent counter

    greetings1 = ["Hi ", "Hello "]
    greetings2 = ["Hi ", "Hello ", "Good Morning ", "Morning "]
    greetings3 = ["Hi ", "Hello ", "Good Afternoon ", "Afternoon"]
    greetings4 = ["Hi ", "Hello ", "Good Evening ", "Evening "]

    acknowledgements = ["It is a pleasure to add you to my network!", "Pleasure to add you to my network!",
                        "I am happy to add you to my network!", "It's a pleasure to add you to my network!",
                        "I'm happy to add you to my network!", "It is a pleasure to e-meet you!",
                        "It is nice to e-meet you!",
                        "Pleasure to e-meet you!", "I am happy to e-meet you!", "It's a pleasure to e-meet you!",
                        "It's nice to e-meet you!", "I'm happy to e-meet you!",
                        "It is a pleasure to make your acquaintance!",
                        "It is nice to make your acquaintance!", "Pleasure to make your acquaintance!",
                        "I am happy to make your acquaintance!", "It's a pleasure to make your acquaintance!",
                        "It's nice to make your acquaintance!", "I'm happy to make your acquaintance!",
                        "It is a pleasure to be connected with you!", "Pleasure to be connected with you!",
                        "I am happy to be connected with you!", "It's a pleasure to be connected with you!",
                        "I'm happy to be connected with you!", "It is a pleasure to connect with you!",
                        "It is nice to connect with you!",
                        "Pleasure to connect with you!", "I am happy to connect with you!",
                        "It's a pleasure to connect with you!",
                        "It's nice to connect with you!", "I'm happy to connect with you!",
                        "It is a pleasure to have made your acquaintance!",
                        "It is nice to have made your acquaintance!",
                        "Pleasure to have made your acquaintance!", "I am happy to have made your acquaintance!",
                        "It's a pleasure to have made your acquaintance!", "It's nice to have made your acquaintance!",
                        "I'm happy to have made your acquaintance!", "It is a pleasure to have connected with you!",
                        "It is nice to have connected with you!", "Pleasure to have connected with you!",
                        "I am happy to have connected with you!", "It's a pleasure to have connected with you!",
                        "It's nice to have connected with you!", "I'm happy to have connected with you!"]

    hook1_list = ["I wanted to ask if you had read the note attached to my connection request?",
                  "I would like to know whether you read the note attached to my connection request?",
                  "I was going to ask if you read the note attached to my connection request?",
                  "I was going to ask if you read the note attached to my contact request?",
                  "Did you accept my connection request because you had read the message I attached to it?",
                  "Did you accept my invitation after reading the message I had added to it?",
                  "Was it after reading the message I attached to it that you decided accept my connection request?",
                  "Did you accept my invitation because you had read the message I attached to it?",
                  "I wanted to ensure that you accepted my invitation because you do have an interest in developing your own business based on the message attached?",
                  "I wanted to make sure you accepted my invitation because you're interested in developing your own business based on the message attached?",
                  "I wanted to make sure you accepted my invitation because you have an interest in developing your own business based on the message attached?",
                  "I wanted to ensure that you accepted my invitation because you do have an interest in developing your own business based on the note attached?",
                  "I wanted to make sure you accepted my invitation because you're interested in developing your own business based on the note attached?",
                  "I wanted to make sure you accepted my invitation because you have an interest in developing your own business based on the note attached?",
                  "Is owning your owning business what drove you to accept my invitation, based on the message attached?",
                  "Was running your own business what prompted you to accept my invitation, based on the message attached to it?",
                  "Was running your own business what prompted you to accept my connection request, based on the message attached to it?",
                  "Was running your own business what prompted you to accept my connection request, based on the note attached to it?",
                  "Was running your own business what prompted you to accept my invitation, based on the message attached?",
                  "Was running your own business what prompted you to accept my connection request, based on the message attached?",
                  "Was running your own business what prompted you to accept my connection request, based on the note attached?",
                  "Was owning your own business what prompted you to accept my invitation, based on the message attached to it?",
                  "Was owning your own business what prompted you to accept my connection request, based on the message attached to it?",
                  "Was owning your own business what prompted you to accept my connection request, based on the note attached to it?",
                  "Was owning your own business what prompted you to accept my invitation, based on the message attached?",
                  "Was owning your own business what prompted you to accept my connection request, based on the message attached?",
                  "Was owning your own business what prompted you to accept my connection request, based on the note attached?",
                  "Is owning your own business what led you to accept my invitation, based on the message attached to it?",
                  "Is running your own business what led you to accept my invitation, based on the message attached to it?",
                  "Is owning your own business what led you to accept my connection request, based on the message attached to it?",
                  "Is owning your own business what led you to accept my invitation, based on the message attached?",
                  "Is running your own business what led you to accept my connection request, based on the message attached to it?",
                  "Is running your own business what led you to accept my connection request, based on the note attached to it?",
                  "Is running your own business what led you to accept my connection request, based on the note attached to it?",
                  "Is owning your own business what led you to accept my connection request, based on the note attached?",
                  "Was it after reading the note I attached to it that you decided accept my connection request?",
                  "Was it after reading the note I attached to it that you decided accept my invitation?",
                  "Was it after reading the message I attached to it that you decided accept my invitation?",
                  "Did you get a chance to read the message I had sent you?",
                  "Have you had a chance to read the message I sent you?",
                  "Have you had a chance to read the message that I sent to you?",
                  "Did you receive the message I had sent to you?",
                  "Did you get a chance to go through my last message?",
                  "Did you have a chance to go through my last message?",
                  "Did you have a chance to read the message I had sent you?"]

    total_time = 0
    today_date = datetime.today().date().replace(day=1)
    interpersonal_skills_array = ['interpersonal', 'management', 'communication', 'leadership', ]
    wait = WebDriverWait(driver, 600)
    url = ''
    try:
        while True:
            wait.until(lambda driver: driver.current_url != url)
            wait.until(lambda driver: '.com/in/' in driver.current_url)

            source = str(driver.page_source)

            # find name
            start_pos = 0
            end_pos = len(source)
            name_bool = False
            try:
                current_position = source.index('"multiLocaleFirstName":{"en_US":"', start_pos,
                                                end_pos)
            except ValueError:
                name_bool = True
            else:
                start_pos = current_position + 33
                try:
                    current_position = source.index('"', start_pos, end_pos)
                except ValueError:
                    name_bool = True
                else:
                    end_pos = current_position
                    name = str(source[start_pos:end_pos]).title()
            if name_bool:
                print('No Name Found.')
                count1 += 1
                count2 += 1
                errors.append(results[count1])
                continue
            else:
                print(str(count1 + 1) + name, end=" | ")



            url = driver.current_url
    except TimeoutException:
        logging.error(traceback.print_exc())
        message = str(os.path.basename(__file__)) + ' experienced an unhandled TimeoutException.' + '\n' + '\n' + str(
            traceback.format_exc())
        print(message)
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, notification_password)
            server.sendmail(sender_email, receiver_email, message)
        sys.exit()

    except Exception as p:
        logging.error(traceback.print_exc())
        message = str(os.path.basename(__file__)) + ' has failed.' + '\n' + '\n' + str(traceback.format_exc())
        print(message)
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, notification_password)
            server.sendmail(sender_email, receiver_email, message)
        sys.exit()
    else:
        message = str(os.path.basename(__file__)) + ' has terminated successfully.'
        print(message)
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, notification_password)
            server.sendmail(sender_email, receiver_email, message)


def teardown(self):
    self.driver.quit()


setup()
