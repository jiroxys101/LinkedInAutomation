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

smtp_server = 'smtp.gmail.com'

d = datetime.now().strftime("%I:%M %p")
port = 465
notification_password = 'RDMSSK6247!'
sender_email = 'notifications.webtrafik@gmail.com'
receiver_email = 'jiroxys101@gmail.com'

context = ssl.create_default_context()
print(d)

is_int = True

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


button = Button(master, text="OK", command=ok)
button.pack()

mainloop()

script_mode = Tk()

variable2 = StringVar(script_mode)

variable2.set("")  # default value
mode = OptionMenu(script_mode, variable2, "Run Script (Headless)", "Run Test (Non-headless)")
mode.pack()


def ok2():
    print("mode is", variable2.get())
    script_mode.quit()
    script_mode.destroy()


button2 = Button(script_mode, text="OK", command=ok2)
button2.pack()

mainloop()

from tkinter.filedialog import askopenfilename

filename = askopenfilename(title=str(email_var),
                           initialdir=r"C:\Users\jirox_000\Desktop\Business Scripts\Second Degree Connections")
print(filename)

results = []
errors = []

options = webdriver.ChromeOptions()
user_agent = random.choice(user_agent_list)

if variable2.get() == "Run Script (Headless)":
    options.add_argument("--headless")

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

while is_int:
    pause_time = int(input("Enter how many seconds you would like to pause for:"))
    if isinstance(pause_time, int):
        is_int = False
    else:
        is_int = True
        print("Sorry.  That value is not an integer.", end=" | ")

print("Pausing for " + str(pause_time) + " seconds")


def countdown(t):
    while t >= 0:
        sys.stdout.write('\r' + str(t) + ' seconds left')
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    print(" Starting!")


with open(filename, "rt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        results.append(row[0])
csvfile.close()
print(results[0])
print(os.getcwd())


def setup():
    driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
    driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
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

    email_field_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(email_field_id))
    pass_field_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(pass_field_id))
    login_button_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
    (login_button_xpath))
    email_field_element.clear()
    email_field_element.send_keys(username)
    pass_field_element.clear()
    pass_field_element.send_keys(password)
    login_button_element.click()
    logo_x_path = "(//span[contains(@id, 'feed-tab-icon')])"
    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(logo_x_path))
    print("Log in successful")

    if pause_time > 0:
        driver.get('http://www.google.com')
        countdown(pause_time)

    # time.sleep(60)
    count1 = 0  # counter to loop through array of links
    count2 = 0  # error counter
    count3 = 0  # sent counter

    if len(results) < 150:
        num = len(results)
        print(str(num) + " profiles left")

    else:
        num = random.randint(150, 190)  # set to 5 for testing
        print(str(num) + " profiles")

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
    try:
        while count1 < num:
            if count2 < 5:  # test
                if count1 != 0:
                    if count1 % 25 == 0:  # test
                        driver.get('http://www.google.com')
                        print('Threshold met. Waiting at Google')
                        countdown(random.randint(2700, 4500))
                        print(str(count1 + 1), end=" | ")
                    else:
                        print(str(count1 + 1), end=" || ")
                else:
                    print(str(count1 + 1), end=" | ")

                start_time = time.time()
                current_time = int(datetime.now().hour)

                try:
                    driver.get(results[count1])
                except TimeoutException:
                    print('Page Timeout.')
                    count1 += 1
                    errors.append(results[count1])
                    continue
                except IndexError:
                    print("End of list reached")
                    break
                else:
                    source = str(driver.page_source)

                    start_pos = 0
                    end_pos = len(source)
                    time.sleep(1)
                    # find name
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
                        print(name, end=" | ")

                # pyperclip.copy(source)
                # print("Source Obtained")
                # check location area
                location_bool = False
                start_pos = 0
                end_pos = len(source)
                # print('Bajinga') change to something else
                try:
                    # print('Looking for location')  change to something else
                    current_position = source.index('defaultLocalizedNameWithoutCountryName":"', start_pos,
                                                    end_pos)
                except ValueError:
                    # print("benghazi")  change to something else
                    location_bool = False
                else:
                    start_pos = current_position + 41
                    try:
                        # print('Still looking for location')  change to something else
                        current_position = source.index('"', start_pos, end_pos)
                    except ValueError:
                        # print("bonobo")  change to something else
                        location_bool = False
                    else:
                        end_pos = current_position
                        location_area = str(source[start_pos:end_pos]).lower()
                if location_bool:
                    count1 += 1
                    count2 += 1
                    errors.append(results[count1])
                    continue

                print(location_area.title(), end=" | ")
                area_list = ["new york", "new jersey", "toronto", "mississauga", "brampton", "scarborough",
                             "philadelphia",
                             "maryland", "washington d.c.", "delaware", "washington, district of columbia",
                             "virginia", "pennsylvania", "ontario", "united states", "florida", "miami", "lauderdale",
                             "ohio",
                             "washington dc", "washington, dc", "montreal", "washington d.c"]

                start_pos = 0
                position_array = []
                # search for all work positions listed
                while True:
                    end_pos = len(source)
                    try:
                        current_position = source.index('"dateRange":{"start":{"month":', start_pos, end_pos)
                    except ValueError:
                        break
                    else:
                        start_pos = current_position

                    try:
                        current_position = source.index(
                            '"$type":"com.linkedin.common.DateRange"},"multiLocaleCompanyName":{"en_US":"', start_pos,
                            end_pos)
                    except ValueError:
                        break
                    else:
                        end_pos = current_position
                        position_array.append(source[start_pos:end_pos])
                        start_pos = end_pos
                if position_array:
                    position_array = list(dict.fromkeys(position_array))
                    positions = len(position_array)
                    end_check = sum(',"end":{' in s for s in position_array)
                else:
                    print("No Positions Found.")
                    count1 += 1
                    count2 += 1
                    errors.append(results[count1])
                    continue
                experience = 0
                present_array = []
                # print(len(position_array), end=" | ")
                test1 = []
                test2 = []
                for e in position_array:
                    sp = 0
                    ep = len(e)
                    # print(e, end=" ||| ")
                    month_index = int(e.index('start":{"month":', sp, ep) + 16)
                    comma_index = int(e.index(',', month_index, ep))
                    start_month = int(e[month_index:comma_index])
                    year_index = int(e.index('"year":', comma_index, ep) + 7)
                    start_year = int(e[year_index:(year_index + 4)])
                    start_date = datetime(year=start_year, month=start_month, day=1)
                    if 'end' in e:
                        if 'end":{"month":' in e:
                            month_index = int(e.index('end":{"month":', year_index, ep) + 14)
                            comma_index = int(e.index(',', month_index, ep))
                            end_month = int(e[month_index:comma_index])
                        else:
                            end_month = start_month
                        year_index = int(e.index('"year":', comma_index, ep) + 7)
                        end_year = int(e[year_index:(year_index + 4)])
                        end_date = datetime(year=end_year, month=end_month, day=1)
                        days = abs(end_date - start_date)
                        years = int(days.days) / 365
                        test1.append(round(years, 2))
                        experience += round(years, 2)
                    else:
                        end_date = datetime(year=int(today_date.year), month=int(today_date.month), day=1)
                        days = abs(end_date - start_date)
                        years = int(days.days) / 365
                        test2.append(round(years, 2))
                        present_array.append(round(years, 2))

                if present_array:
                    experience += max(present_array)
                experience = round(experience, 2)
                print(str(experience) + " years experience", end=" | ")

                start_pos = 0
                temp_array_1 = []
                # search for all skills
                while True:
                    end_pos = len(source)
                    try:
                        current_position = source.index(
                            '"entityUrn":"urn:li:fsd_skill:'
                            , start_pos, end_pos)
                    except ValueError:
                        break
                    else:
                        start_pos = current_position
                    try:
                        current_position = source.index('multiLocaleName', start_pos, end_pos)
                    except ValueError:
                        break
                    else:
                        end_pos = current_position
                        temp_array_1.append(source[start_pos:end_pos])
                        start_pos = end_pos

                skill_array = []
                # build skill array
                for e in temp_array_1:
                    sp = 0
                    ep = len(e)
                    skill_index = int(e.index(',"name":"', sp, ep) + 9)
                    comma_index = int(e.index('","', skill_index, ep))
                    skill_array.append(e[skill_index:comma_index].lower())
                skill_fragment = ""
                # check for skill match
                for i in interpersonal_skills_array:
                    if i in skill_array:
                        skill_fragment += (str(i) + ", ")
                # Skill Check
                if not skill_fragment:
                    print('No skill match', end=" | ")
                    sentence = "I was looking at your profile and couldn't help but notice your " + str(int(round(
                        experience, 0))) + " years of experience and your strong " + random.choice(interpersonal_skills_array) + " skills. "
                else:
                    k = skill_fragment.rfind(', ')
                    if skill_fragment.count(', ') >= 3:
                        skill_fragment = skill_fragment[:k] + ', and ' + skill_fragment[k + 1:]
                    elif skill_fragment.count(', ') == 2:
                        skill_fragment = skill_fragment[:-2]
                        skill_fragment = skill_fragment.replace(",", " and")
                    else:
                        skill_fragment = skill_fragment.replace(",", "")
                    sentence = "I was looking at your profile and couldn't help but notice that you've been endorsed for your strong "\
                               + skill_fragment + ' skills. '
                # print(sentence)
                start_pos = 0
                education_array = []
                # search for education years listed
                x = 1  # variable will change to 5 if there is no education
                while True:
                    end_pos = len(source)
                    try:
                        current_position = source.index('{"dateRange":{"start":{"year":', start_pos, end_pos)
                    except ValueError:
                        break
                    else:
                        start_pos = current_position
                        education_array.append(int(re.sub('[^0-9]', "", source[start_pos + 30:start_pos + 34])))
                    try:
                        current_position = source.index(
                            ',"end":{"year":', start_pos,
                            end_pos)
                    except ValueError:
                        break
                    else:
                        end_pos = current_position
                        education_array.append(int(re.sub('[^0-9]', "", source[end_pos + 15:end_pos + 19])))
                        start_pos = end_pos
                if education_array:
                    age = (2019 - min(education_array)) + 18
                else:
                    age = 25
                    x = 5
                print("Approximately " + str(age) + " years old", end=" | ")
                # 4 below must be true to continue
                location_check = False  # check if within location area
                experience_check = False  # check if experience within range
                employed_check = False  # check if currently employed
                age_check = False  # check if age within range
                # check for matches with interpersonal skill array; industry instead of skills if false
                skill_check = False

                # location check
                if any(sub in location_area for sub in area_list):
                    location_check = True
                else:
                    print("Outside Location Area", end=" | ")

                # employed check
                if end_check < positions:
                    employed_check = True
                else:
                    print("Not Currently Employed", end=" | ")

                # Age check
                if 22 < age < 37:
                    age_check = True
                else:
                    print("Outside Age Range", end=" | ")

                # Experience check
                if x < experience < 16:
                    experience_check = True
                elif age_check:
                    if (end_check - positions) <= 3:
                        print("", end="|")
                        experience_check = True
                else:
                    print("Outside Age & Experience Range", end=" | ")

                checker = [location_check, age_check, experience_check, employed_check]
                if not all(checker):
                    print("Not Viable Prospect.")
                    count1 += 1
                    continue
                connect_bool = True
                try:
                    connect_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(
                        "//button[contains(@class, '--connect')]"))
                except TimeoutException:
                    print("", end="|")
                else:
                    for e in range(10):
                        try:
                            connect_button.click()
                        except WebDriverException:
                            time.sleep(1)
                            continue
                        else:
                            connect_bool = False
                            break
                if connect_bool:
                    try:
                        dropdown = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(
                            "//artdeco-dropdown-content[contains(@class, 'overflow-dropdown')]"))
                    except TimeoutException:
                        print("Cant Access Dropdown")
                        count1 += 1
                        count2 += 1
                        errors.append(results[count1])
                        continue
                    else:
                        driver.execute_script(
                            "arguments[0].style.visibility = 'visible'; arguments[0].style.opacity = 1",
                            dropdown)
                    try:
                        connect_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(
                            "//artdeco-dropdown-item[contains(@class, '--connect')]"))
                    except TimeoutException:
                        print("No Connect buttons found.")
                        count1 += 1
                        count2 += 1
                        errors.append(results[count1])
                        continue
                    else:
                        for e in range(10):
                            try:
                                connect_button.click()
                            except WebDriverException:
                                time.sleep(1)
                                continue
                            else:
                                connect_bool = False
                                break
                if connect_bool:
                    print('No Connection Button Found')
                    count1 += 1
                    count2 += 1
                    errors.append(results[count1])
                    continue
                else:
                    try:
                        note_element = WebDriverWait(driver, 5).until(
                            lambda driver: driver.find_element_by_xpath("//button[contains(.,'Add a note')]"))
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        count2 += 1
                        print("No Add Note Button detected")
                        continue
                    else:
                        driver.execute_script('arguments[0].click();', note_element)

                    try:
                        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_css_selector('textarea'))
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        count2 += 1
                        print("No Message Area detected")
                        continue
                    else:
                        textbox_element = WebDriverWait(driver, 5).until(
                            lambda driver: driver.find_element_by_css_selector('textarea'))

                        hour = datetime.now().hour
                        if 5 <= int(hour) <= 11:
                            greeting = random.choice(greetings1 + greetings2)
                        elif 12 <= int(hour) <= 17:
                            greeting = random.choice(greetings1 + greetings3)
                        elif 18 <= int(hour) <= 22:
                            greeting = random.choice(greetings1 + greetings4)
                        else:
                            greeting = random.choice(greetings1)

                        message_script = greeting + name + "! " + sentence + "I'm always looking to network with strong professionals. Hope we can add value to each other!"
                        message_script = message_script.replace("  ", " ")
                        textbox_element.send_keys(message_script)
                    try:
                        send_element = WebDriverWait(driver, 5).until(
                            lambda driver: driver.find_element_by_xpath("//button[contains(.,'Send ')]"))
                        driver.execute_script('arguments[0].click();', send_element)
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        count2 += 1
                        print("No send button detected")
                        continue
                    try:
                        success = WebDriverWait(driver, 15).until(
                            lambda driver: driver.find_element_by_xpath("//h3[contains(@class,'t-18 ')]"))
                    except TimeoutException:
                        if driver.current_url != driver.get(results[count1]):
                            pass
                        else:
                            count1 += 1
                            count2 += 1
                            print("Unsuccessful")
                            continue

                end_time = time.time()
                print(round(end_time - start_time, 2), end=" | ")
                count1 += 1
                count3 += 1
                count2 = 0
                print(count3)
                # time.sleep(600)
            else:
                break

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
