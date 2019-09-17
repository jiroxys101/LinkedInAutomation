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
import datetime
from datetime import datetime
import requests
from browsermobproxy import Server
import traceback
import logging
import atexit
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.action_chains import ActionChains

server = Server("C:\\Users\\Rijul.Kumar\\PycharmProjects\\LinkedInAutomation\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy")
smtp_server = 'smtp.gmail.com'
server.start()
proxy = server.create_proxy()

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
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    ]

master = Tk()

variable1 = StringVar(master)

variable1.set("")  # default value
w = OptionMenu(master, variable1, "Rijul Kumar", "Omotayo Ogunnusi", "Rijul K", "Prasad Pansare", "Dieudonné Ndjebayi", "Sushma Kumar",
               "Utkarsh Manjrekar")
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

results = []
errors = []


chrome_options = webdriver.ChromeOptions()
user_agent = random.choice(user_agent_list)

if variable2.get() == "Run Script (Headless)":
    chrome_options.add_argument("--headless")

bunji = os.getenv("USERNAME")
# userProfile = "C:\\Users\\jirox_000\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
userProfile = "C:\\Users\\" + bunji + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])

chrome_options.add_argument("user-data-dir={}".format(userProfile))
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--proxy-server={host}:{port}'.format(host='localhost', port=proxy.port))
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')

chrome_driver = "C:\Webdrivers\\chromedriver.exe"

while is_int:
    pause_time = int(input("Enter how many seconds you would like to pause for:"))
    if isinstance(pause_time, int):
        is_int = False
    else:
        is_int = True
        print("Sorry.  That value is not an integer.", end=" ")

print("Pausing for " + str(pause_time) + " seconds")


def countdown(t):
    while t >= 0:
        sys.stdout.write('\r' + str(t) + ' seconds left')
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    print("Starting!")


countdown(pause_time)


def setup():
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
        driver.set_page_load_timeout(60)

        username = str(email_var)
        password = str(pw_var)
        email_field_id = "username"
        pass_field_id = "password"
        login_button_xpath = "//button[contains(@type,'submit')]"
        print("Logging in...", end=" ")
        print(user_agent)
        actions = ActionChains(driver)

        email_field_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(email_field_id))
        pass_field_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(pass_field_id))
        login_button_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
        (login_button_xpath))
        email_field_element.clear()
        email_field_element.send_keys(username)
        time.sleep(1)
        pass_field_element.clear()
        pass_field_element.send_keys(password)
        time.sleep(1)
        login_button_element.click()
        logo_x_path = "(//span[contains(@id, 'feed-tab-icon')])"
        WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(logo_x_path))
        print("Log in successful")
        # driver.get('https://www.linkedin.com/in/tony-olusoga-2b4555125/')
        driver.get('https://www.linkedin.com/in/oyafunmike-ogunlano-ba63a04a/')

        body = driver.find_element_by_css_selector('body')

        lenOfPage = driver.execute_script("var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        footer_xpath = '//p[contains(@id, "globalfooter-copyright")]'

        match = False
        while match is False:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            try:
                WebDriverWait(driver, 0.5).until(lambda driver: driver.find_elements_by_xpath(footer_xpath))
            except TimeoutException:
                pass
            else:
                match = True

        experience_see_more = "//button[contains(@class,'pv-experience-section')]"
        see_more_xpath = "//button[contains(@class,'additional-skills')]"

        try:
            experience_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(experience_see_more))
        except TimeoutException:
            pass
        else:
            actions.move_to_element(experience_button).perform()
            driver.execute_script('arguments[0].click();', experience_button)

        try:
            see_more_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(see_more_xpath))
        except TimeoutException:
            pass
        else:
            actions.move_to_element(see_more_element).perform()
            driver.execute_script('arguments[0].click();', see_more_element)

        years = WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath(
            "//span[contains(@class,'bullet-item-v2')]"))
        descriptions = WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath(
            "//h4[contains(@class,'date-range')]"))
        years_array = []
        present_array = []
        descriptions_array = []
        for e in years:
            years_array.append(e.get_attribute('innerText'))
        for e in descriptions:
            descriptions_array.append(e.get_attribute('innerText').lower())
        print(years_array)
        total_experience = 0
        loop_count = 0
        for e in years_array:
            experience = e.split()
            if "yrs" in experience:
                yrs_index = experience.index("yrs") - 1
                yrs = int(int(experience[yrs_index]) * 12)
            else:
                yrs = 0
            if "mos" in experience:
                mos_index = experience.index("mos") - 1
                mos = int(experience[mos_index])
            else:
                mos = 0
            experience_time = yrs + mos
            if 'present' in descriptions_array[loop_count]:
                present_array.append(experience_time)
            else:
                total_experience += experience_time
            loop_count += 1
        total_experience = round(total_experience/12, 2) + round(max(present_array)/12, 2)
        print(str(total_experience) + " years experience")

        education_x_path = "(//time)"
        education_years = []
        try:
            education_times = WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath(education_x_path))
        except TimeoutException:
            print("No Education Years Present")
            if total_experience >= 16:
                print("Above Maximum Experience")
            elif total_experience < 2:
                print("Below Minimum Experience")
            else:
                print("Within Experience Demographic!")
        else:
            for e in education_times:
                if re.search('[a-zA-Z]', e.get_attribute("innerText")):
                    education_years.append(e.get_attribute("innerText").lower())
                else:
                    education_years.append(int(e.get_attribute("innerText")))

            if 'present' in education_years:
                print("Currently Student")
            elif min(education_years) < 2003:
                print("Above Maximum Age")
            elif max(education_years) > 2017:
                print("Below Minimum Age")
            else:
                if total_experience >= 16:
                    print("Above Minimum Experience")
                elif total_experience < 2:
                    print("Below Minimum Experience")
                else:
                    print("Within Age & Experience Demographic!")
    except TimeoutException:
        logging.error(traceback.print_exc())
        message = str(os.path.basename(__file__)) + ' experience an unhandled TimeoutException.' + '\n' + '\n' + str(traceback.format_exc())
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
