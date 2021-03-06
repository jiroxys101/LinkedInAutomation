import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import bs4
from bs4 import BeautifulSoup
import random
import pyperclip
import unittest
import csv
import time
import os
from tkinter import *
from selenium.webdriver.common.action_chains import ActionChains
import re
from datetime import datetime
from tkinter.filedialog import askopenfilename
from collections import OrderedDict
import math


log_in = {"Rijul Kumar": ["rijulkumar.webtrafik@gmail.com", "Gocam2020"],

          "Omotayo Ogunnusi": ["tayoogunnusi@outlook.com", "Temitope5"],

          "Rijul K": ["rijulkumar7500@gmail.com", "nov192011"],

          "Devansh Kumar": ["devanshk64@gmail.com", "Dk081899"],

          "Sushma Kumar": ["sush126.kumar@gmail.com", "Dmnd2017"],

          }

user_agent_list = \
    [
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
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    ]

master = Tk()

ID = str(round(time.time()))


d = datetime.now().strftime("%I:%M %p")
start_time = time.time()
print(d)
print('')

variable1 = StringVar(master)
variable1.set("")  # default value

w = OptionMenu(master, variable1, "Rijul Kumar", "Omotayo Ogunnusi", "Rijul K", "Devansh Kumar",
               "Sushma Kumar")
w.pack()

name_var = ""
email_var = ""
pw_var = ""


def ok():

    if variable1.get() in log_in:
        global name_var
        name_var = variable1.get()
        global email_var
        email_var = log_in.get(variable1.get(), "")[0]
        global pw_var
        pw_var = log_in.get(variable1.get(), "")[1]
        print("Name: ", name_var)
        print("E-Mail: ", email_var)
        print("Password: ", pw_var)
        print('')

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

filename = askopenfilename(title=str(email_var),
                           initialdir=r"C:\Users\jirox_000\Desktop\Business Scripts\First Degree Connections",
                           filetypes=[("CSV files", "*.csv")])
print(filename)

exclusion_list = []

print('Reading CSV file...', end=" ")
with open(filename, "rt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        exclusion_list.append(row[0].lower())
csvfile.close()
print('File Read! | ' + str(len(exclusion_list)))
print('')

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
chrome_driver = "C:\Webdrivers\\chromedriver.exe"


def countdown(t):
    while t >= 0:
        sys.stdout.write('\r' + str(t) + ' seconds left')
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    print(" | Starting!", end="|")


is_URL = True

recruiter_keyword = str(input("Enter Keyword you want to use: ")).title().strip()

file_name = str("2nd - " + name_var + " - " + recruiter_keyword + " - " + ID + '.csv')
print(file_name)

recruiter_URL = \
    'https://www.linkedin.com/search/results/people/?facetGeoRegion=' \
    '%5B%22us%3A70%22%2C%22us%3A97%22%2C%22us%3A7416%22%2C%22us%3A77%22%5D&facetNetwork=' \
    '%5B%22S%22%5D&facetProfileLanguage=%5B%22en%22%5D&keywords=%22'\
    + recruiter_keyword + '%22&origin=FACETED_SEARCH&page='


def set_up():

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
    driver.set_page_load_timeout(60)

    actions = ActionChains(driver)

    username = str(email_var)
    password = str(pw_var)
    email_field_id = "username"
    pass_field_id = "password"
    login_button_xpath = "//button[contains(@type,'submit')]"
    print("Logging in", end="")
    driver.save_screenshot('screenie.png')

    email_field_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(email_field_id))
    pass_field_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(pass_field_id))
    login_button_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath(
        login_button_xpath))
    print(".", end="")
    email_field_element.clear()
    email_field_element.send_keys(username)
    pass_field_element.clear()
    pass_field_element.send_keys(password)
    print(".", end="")
    login_button_element.click()
    print(".", end="")
    logo_x_path = "(//span[contains(@id, 'feed-tab-icon')])"
    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(logo_x_path))
    print("Log in successful")

    agent = driver.execute_script("return navigator.userAgent")
    print('')
    loopy = 0

    driver.get(recruiter_URL + str(loopy+1))
    driver.save_screenshot('screenie2.png')

    results_xpath = "(//h3[contains(@class, 'search-results')])"
    results_elem = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath(results_xpath))
    num = results_elem.text
    first = int(num.find(' '))
    last = int(num.rfind(' '))
    num = num[first:last].strip('').replace(',', '')
    num = int(num)
    if num <= 1000:
        iterations = math.floor(num / 10) + 1
    else:
        iterations = 100
    print(str(num) + " Profiles | " + str(iterations) + " Pages")

    profile_list = []

    while loopy < iterations:
        link_list = []
        link_count = 0
        county_boi = 0
        results_found_elem = ''
        try:
            results_found_elem = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(
                "//h1[contains(@class, 't-normal')]")).get_attribute('innerText')
        except TimeoutException:
            if "No Results Found" in results_found_elem:
                print("No Results Found. Closing Script.")
                break
            else:
                print(loopy + 1, end="")
                try:
                    WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath(
                        "//div[contains(@class, 'search-filters-bar')]"))
                except TimeoutException:
                    print("Script Failure")
                    time_stamp = str(round(time.time()))
                    driver.save_screenshot('screenie' + time_stamp + '.png')
                    print('screenie' + time_stamp + '.png')
                    loopy += 1
                    driver.get(recruiter_URL + str(loopy + 1))
                    continue
                else:
                    print(".", end="")
                while link_count < 10 and county_boi < 5:
                    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
                    try:
                        profile_wrappers = WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath(
                            "//div[contains(@class, 'info')]"))
                    except TimeoutException:
                        print("Script Failure")
                        time_stamp = str(round(time.time()))
                        driver.save_screenshot('screenie' + time_stamp + '.png')
                        loopy += 1
                        driver.get(recruiter_URL + str(loopy + 1))
                        continue
                    else:
                        link_count = len(profile_wrappers)
                        county_boi += 1
                print(".", end="")
                try:
                    link_elements = WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath(
                        "//a[contains(@class, 'result-link')]"))
                except TimeoutException:
                    print("Script Failure")
                    time_stamp = str(round(time.time()))
                    driver.save_screenshot('screenie' + time_stamp + '.png')
                    print('screenie' + time_stamp + '.png')
                    loopy += 1
                    driver.get(recruiter_URL + str(loopy + 1))
                    continue
                else:
                    for e in link_elements:
                        link_list.append(e.get_attribute('href'))
                link_list = list(dict.fromkeys(link_list))
                profile_wrapper_to_link_count = 0
                for e in profile_wrappers:
                    result_text = str(e.get_attribute('innerHTML')).lower()
                    if any(sub in result_text for sub in exclusion_list):
                        profile_wrapper_to_link_count += 1
                    else:
                        profile_list.append(link_list[profile_wrapper_to_link_count])
                        profile_wrapper_to_link_count += 1
        loopy += 1
        driver.get(recruiter_URL + str(loopy + 1))
        print(".", end="")
    driver.quit()
    profiles = len(profile_list)

    with open(file_name, 'a', newline='') as my_file:
        wr = csv.writer(my_file, dialect='excel', quoting=csv.QUOTE_ALL)
        for x in range(0, profiles):
            wr.writerow([profile_list[x]])
    print('')
    print(str(profiles) + " profiles found", end=' | ')
    end_time = time.time() - start_time
    print("Search Complete | " + str(round(end_time, 2)) + " seconds")
    print('')
    print(file_name)


set_up()
