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
from tkinter.filedialog import askopenfilename



smtp_server = 'smtp.gmail.com'

d = datetime.now().strftime("%I:%M %p")
port = 465
notification_password = 'RDMSSK6247!'
sender_email = 'notifications.webtrafik@gmail.com'
receiver_email = 'jiroxys101@gmail.com'

context = ssl.create_default_context()
print(d)
# os.chdir('C:\\Users\\Rijul Kumar\\PycharmProjects\\LinkedInAutomation')
os.chdir('C:\\Users\\Rijul Kumar\\Documents\\LinkedInAutomation')

is_int = True


# current
log_in = {"Rijul Kumar": ["rijulkumar.webtrafik@gmail.com", "Gocam2020", "/in/rijul-kumar/"],
          "Omotayo Ogunnusi": ["tayoogunnusi@outlook.com", "Temitope5", "/in/tayo-o/"],
          "Rijul K": ["rijulkumar7500@gmail.com", "nov192011", "/in/rijul-kumar-02a02586/"],
          "Prasad Pansare": ["prasadpansare2019@gmail.com", "Gocam2020", "/in/prasadpbiz/"],
          "Dieudonné Ndjebayi": ["rijul.kumar@construction.com", "Gocam2020", "/in/dieudonné-ndjebayi-seh/"],
          "Sushma Kumar": ["sush126.kumar@gmail.com", "Dmnd2017", ""],
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
        global url_var
        url_var = log_in.get(variable1.get(), "")[2]

        print("Name: ", name_var)
        print("E-Mail: ", email_var)
        print("Password: ", pw_var)

    master.quit()
    master.destroy()


button1 = Button(master, text="OK", command=ok)
button1.pack()

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
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument(f'user-agent={user_agent}')

if variable2.get() == "Run Script (Headless)":
    options.add_argument("--headless")

chrome_driver = "C:\Webdrivers\\chromedriver.exe"
filename = askopenfilename(title=str(email_var))

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
num = int(len(results))


def setup():
    driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
    print("VPN", end="")

    #start up VPN

    try:
        os.system('TASKKILL /F /IM CyberGhost.exe')
    except Exception:
        print('...', end="")
    finally:
        os.startfile('C:\\Program Files\\CyberGhost 7\\CyberGhost.exe')
        print(" Started! Waiting!")
        time.sleep(120)

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
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
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

    greetings1 = ["Hi ", "Hello "]
    greetings2 = ["Hi ", "Hello ", "Good Morning ", "Morning "]
    greetings3 = ["Hi ", "Hello ", "Good Afternoon ", "Afternoon "]
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

    hook2_list = [
        'Have you ever given any thought to utilizing your skills to develop a business outside of your career?',
        'Have you ever given any thought to utilizing your skills to develop a business outside of your job?',
        'Have you ever given any thought to utilizing your skills to develop a business outside of your profession?',
        'Do you ever think about using your skills to develop a business outside of your career?',
        'Do you ever think about using your skills to develop a business outside of your job?',
        'Do you ever think about using your skills to develop a business outside of your profession?',
        'Did you ever consider using your skills to develop a business outside of your career?',
        'Did you ever consider using your skills to develop a business outside of your job?',
        'Did you ever consider using your skills to develop a business outside of your profession?',
        'Have you ever thought about utilizing your skills to develop a business outside of your career?',
        'Have you ever thought about utilizing your skills to develop a business outside of your job?',
        'Have you ever thought about utilizing your skills to develop a business outside of your profession?',
        'Have you ever thought about using your skills to develop a business outside of your career?',
        'Have you ever thought about using your skills to develop a business outside of your job?',
        'Have you ever thought about using your skills to develop a business outside of your profession?'
]

    hook3_list = [
                  ' After taking a look at your profile, I wanted to ask: ',
                  ' After taking a look at your profile, I wanted to follow-up: ',
                  ' After taking a look at your profile, I want to ask: ',
                  ' After taking a look at your profile, I want to follow-up: '
]

    total_time = 0
    today_date = datetime.today().date().replace(day=1)
    interpersonal_skills_array = ['interpersonal', 'management', 'communication', 'leadership', ]
    wait = WebDriverWait(driver, 3600)
    url = ''
    while count1 < num:
        if count1 != 0:
            if count1 % 25 == 0:  # test
                driver.get('http://www.google.com')
                timey = random.randint(1800, 3600)
                wimey = int(round(timey/60, 0))
                print('Threshold met. Waiting at Google for ' + str(wimey) + ' minutes')

                try:
                    os.system('TASKKILL /F /IM CyberGhost.exe')
                except Exception:
                    print('...', end="")
                finally:
                    countdown(3600)
                    os.startfile('C:\\Program Files\\CyberGhost 7\\CyberGhost.exe')
                    print(" Started! Waiting!")
                    time.sleep(120)
            else:
                pass
        else:
            pass

        driver.get(results[count1])
        wait.until(lambda driver: driver.current_url != url)
        wait.until(lambda driver: '.com/in/' in driver.current_url)
        # driver.get(driver.current_url)
        time.sleep(1)
        source = str(driver.page_source)

        # find name
        start_pos = 0
        end_pos = len(source)
        name_bool = False
        name = ''
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
                name = name.split(' ', 1)[0]
        if name_bool:
            print('No Name Found.')
            driver.save_screenshot(str(name_var) + str(int(round(time.time(), 0))) + '.png')
            count1 += 1
            count2 += 1
            errors.append(results[count1])
            continue
        else:
            print(str(count1 + 1) + "| " + name, end=" | ")

        # check location area
        location_area = ''
        location_bool = False
        start_pos = 0
        end_pos = len(source)

        location_check = False  # check if within location area
        experience_check = False  # check if experience within range
        employed_check = False  # check if currently employed
        age_check = False  # check if age within range
        education_check = False  # check if currently student

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

        if any(sub in location_area for sub in area_list):
            location_check = True
        else:
            print("Outside Location", end=" | ")

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

        if end_check < positions:
            print("Employed", end=" | ")
            employed_check = True
        else:
            print("Not Currently Employed", end=" | ")

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
        else:
            k = skill_fragment.rfind(', ')
            if skill_fragment.count(', ') >= 3:
                skill_fragment = skill_fragment[:k] + ', and ' + skill_fragment[k + 1:]
            elif skill_fragment.count(', ') == 2:
                skill_fragment = skill_fragment[:-2]
                skill_fragment = skill_fragment.replace(",", " and")
            else:
                skill_fragment = skill_fragment.replace(",", "")
                print("Skill Match", end=" | ")
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
            education = int(max(education_array))
            print(str(education), end=" | ")
        else:
            age = 25
            x = 5
            education = 2002
        print(str(age) + " years old", end=" | ")

        if 22 < age < 37:
            age_check = True
        else:
            print("Outside Age Range", end=" | ")


        current_year = 2020
        # education check
        if current_year > education:
            print("Graduated", end=" | ")
            education_check = True
        else:
            print("Currently Student", end=" | ")

        checker = [location_check, age_check, employed_check, education_check]
        if not all(checker):
            print("Not Viable Prospect.")
            count1 += 1
            count2 = 0
            continue

        hour = datetime.now().hour
        if 5 <= int(hour) <= 11:
            greeting = random.choice(greetings1 + greetings2)
        elif 12 <= int(hour) <= 17:
            greeting = random.choice(greetings1 + greetings3)
        elif 18 <= int(hour) <= 22:
            greeting = random.choice(greetings1 + greetings4)
        else:
            greeting = random.choice(greetings1)

        message_script = greeting + name + "! " + str(random.choice(acknowledgements)) + str(random.choice(
            hook3_list)) + str(random.choice(hook2_list))
        message_script = message_script.replace("  ", " ")
        pyperclip.copy(message_script)
        count1 += 1
        url = driver.current_url
        is_int = True
        gogo = True

        while is_int:
            while True:
                try:  # see if their is an open message window
                    msg_close_element = WebDriverWait(driver, 2).until(
                        lambda driver: driver.find_element_by_xpath
                        ("//button[contains(@class, 'msg-close')]"))
                    print("Open Message Window. Closing...")
                    msg_close_element.click()
                except TimeoutException:
                    break

            try:
                message_button_element = WebDriverWait(driver, 15).until(
                    lambda driver: driver.find_element_by_xpath
                    ("//button[contains(@class, 'message')]"))
                driver.execute_script('arguments[0].click();', message_button_element)
            except TimeoutException:
                print("No Message Button. Skipping...")
            else:
                numpy = 0
                try:
                    array1 = WebDriverWait(driver, 3).until(
                        lambda driver: driver.find_elements_by_xpath
                        ("//div[contains(@class, 'msg-s-event-listitem')]"))
                except TimeoutException:
                    numpy = 0
                else:
                    for i in array1:
                        message = str(i.get_attribute('innerHTML')).lower()
                        if url_var in message:
                            numpy += 1
                            if '?"' in message:
                                numpy = 7
                if numpy <= 1:
                    print('Messaging', end=" | ")
                    try:
                        message_area_element = WebDriverWait(driver, 5).until(
                            lambda driver: driver.find_element_by_xpath(
                                "//ul[contains(@class,'msg-s-message-list-content')]"))
                    except TimeoutException:
                        pass
                    finally:
                        try:
                            text_area_element = WebDriverWait(driver, 3).until(
                                lambda driver: driver.find_element_by_xpath
                                ("//div[contains(@role, 'text')]"))
                        except TimeoutException:
                            pass
                        else:
                            try:
                                send_button_element = WebDriverWait(driver, 5).until(
                                    lambda driver: driver.find_element_by_xpath
                                    ("//button[contains(@class, 'send-button')]"))
                            except TimeoutException:
                                pass
                            else:
                                text_area_element.send_keys(str(message_script))
                                driver.execute_script('arguments[0].click();', send_button_element)
                                time.sleep(random.randint(2, 4))
                                try:
                                    WebDriverWait(driver, 5).until(
                                        lambda driver: driver.find_elements_by_xpath
                                        ("//div[contains(@class, 'msg-s-event-listitem')]"))
                                except TimeoutException:
                                    pass
                                # time.sleep(5)
                                count3 += 1
                                print(str(count3) + ' messages sent.')
                    driver.get('https://www.google.com')
                    is_int = False
                else:
                    print('Messaged. Skipping...')
                    driver.get('https://www.google.com')
                    is_int = False


def teardown(self):
    self.driver.quit()


setup()
