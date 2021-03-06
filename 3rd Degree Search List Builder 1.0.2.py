import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
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
import re
import pickle

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
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    ]

master = Tk()

ID = str(round(time.time()))


d = datetime.now().strftime("%I:%M %p")
start_time = time.time()
print(d)
is_int = True

print('')

variable1 = StringVar(master)
variable1.set("")  # default value

w = OptionMenu(master, variable1, "Rijul Kumar", "Omotayo Ogunnusi", "Rijul K", "Prasad Pansare", "Dieudonné Ndjebayi", "Sushma Kumar")
w.pack()

name_var = ""
email_var = ""
pw_var = ""


def ok():

    if variable1.get() in log_in:
        global name_var
        name_var = variable1.get()
        global email_var
        email_var = log_in.get(variable1.get())[0]
        global pw_var
        pw_var = log_in.get(variable1.get())[1]
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

locations = {"Greater New York City Area": "3A70",
             "Greater Philadelphia Area": "3A77",
             "Washington D.C. Metro Area": "3A97",
             "Baltimore, Maryland Area": "3A7416",
             "Dover, Delaware Area": "3A219",
             "Miami/Fort Lauderdale Area": "3A56",
             "Columbus, Ohio": "3A184",
             "Toronto, Canada": "3A4876",
             }

location = Tk()
variable3 = StringVar(location)
variable3.set("")  # default value
location_options = OptionMenu(location, variable3, "Greater New York City Area", "Greater Philadelphia Area",
                              "Washington D.C. Metro Area", "Baltimore, Maryland Area", "Dover, Delaware Area",
                              "Miami/Fort Lauderdale Area", "Columbus, Ohio", "Toronto, Canada")
location_options.pack()


def ok3():
    global location_var
    location_var = str(variable3.get())
    print("Location: ", location_var)
    global encode
    encode = locations.get(variable3.get())
    print("Encode: ", encode)

    location.quit()
    location.destroy()


button3 = Button(location, text="OK", command=ok3)
button3.pack()

mainloop()

filename = askopenfilename(title=str(email_var),
                           filetypes=[("CSV files", "*.csv")])
print(filename)

exclusion_list = []

print('Reading CSV file...', end=" ")
with open(filename, "rt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        exclusion_list.append(row[0].lower())
dir_path = os.path.dirname(os.path.realpath(__file__))
csvfile.close()
print('File Read! | ' + str(len(exclusion_list)))
print('')

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


chrome_options = webdriver.ChromeOptions()
user_agent = random.choice(user_agent_list)

if variable2.get() == "Run Script (Headless)":
    chrome_options.add_argument("--headless")

bunji = os.getenv("USERNAME")
# userProfile = "C:\\Users\\jirox_000\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
# userProfile = "C:\\Users\\" + bunji + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])

# chrome_options.add_argument("user-data-dir={}".format(userProfile))
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

recruiter_keyword = str(input("Enter Keyword you want to use: ")).strip()
recruiter_filename = str(re.sub(r'\W+', '', recruiter_keyword.title()))
recruiter_keyword = recruiter_keyword.replace(' ', '%20')
recruiter_keyword = recruiter_keyword.replace('"', '%22')



file_name = str("3rd - " + name_var + " - " + recruiter_filename + " - " + location_var + " - " + ID + '.csv')
file_name = file_name.replace("/", "-")
print(file_name)

print(user_agent)


def set_up():
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
    driver.set_page_load_timeout(600)
    num = 1
    page = str(num)
    recruiter_URL = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%' + encode + '%22%5D' + \
                    '&facetIndustry=%5B%2296%22%2C%22124%22%2C%224%22%2C%2257%22%2C%2280%22%2C%2298%22%2C%2211%22%2C%22118' \
                    '%22%2C%2251%22%2C%2253ejt%22%2C%2254%22%2C%226%22%2C%2284%22%2C%2291%22%2C%221%22%2C%22102%22%2C%22112' \
                    '%22%2C%22114%22%2C%22116%22%2C%22117%22%2C%22119%22%2C%2212%22%2C%22123%22%2C%22134%22%2C%22135%22%' \
                    '2C%22137%22%2C%22138%22%2C%22143%22%2C%22144%22%2C%22146%22%2C%22147%22%2C%2217%22%2C%2219%22%2C%' \
                    '2220%22%2C%223%22%2C%2231%22%2C%2240%22%2C%2241%22%2C%2247%22%2C%2249%22%2C%225%22%2C%2252%22%2C%' \
                    '2255%22%2C%2256%22%2C%2261%22%2C%2262%22%2C%227%22%2C%228%22%2C%2282%22%2C%2283%22%2C%2286%22%2C%' \
                    '2287%22%2C%2297%22%5D' \
                    '&facetNetwork=%5B%22O%22%5D&keywords=' + recruiter_keyword + \
                    '&origin=FACETED_SEARCH&page=' + page + \
                    '&title=NOT%20(' \
                    '%22CEO%22%20OR%20%22Founder%22%20OR%20%22' \
                    'President%22%20OR%20%22Chief%22%20OR%20%22Director%22%20OR%20%22Owner%22)'

    alt_url = 'https://www.linkedin.com/search/results/people/?authorCompany=%5B%5D&authorIndustry=%5B%5D&contactInterest=%5B%5D&facetCity=%5B%5D&facetCompany=%5B%5D&facetConnectionOf=%5B%5D&facetCurrentCompany=%5B%5D&facetCurrentFunction=%5B%5D&facetGeoRegion=%5B%22us%' + encode + '%22%5D&facetGeoUrn=%5B%5D&facetGroup=%5B%5D&facetGuides=%5B%5D&facetIndustry=%5B%2296%22%2C%22124%22%2C%224%22%2C%2257%22%2C%2280%22%2C%2298%22%2C%2211%22%2C%22118%22%2C%2251%22%2C%2253ejt%22%2C%2254%22%2C%226%22%2C%2284%22%2C%2291%22%2C%221%22%2C%22102%22%2C%22112%22%2C%22114%22%2C%22116%22%2C%22117%22%2C%22119%22%2C%2212%22%2C%22123%22%2C%22134%22%2C%22135%22%2C%22137%22%2C%22138%22%2C%22143%22%2C%22144%22%2C%22146%22%2C%22147%22%2C%2217%22%2C%2219%22%2C%2220%22%2C%223%22%2C%2231%22%2C%2240%22%2C%2241%22%2C%2247%22%2C%2249%22%2C%225%22%2C%2252%22%2C%2255%22%2C%2256%22%2C%2261%22%2C%2262%22%2C%227%22%2C%228%22%2C%2282%22%2C%2283%22%2C%2286%22%2C%2287%22%2C%2297%22%5D&facetNetwork=%5B%22O%22%5D&facetNonprofitInterest=%5B%5D&facetPastCompany=%5B%5D&facetProfessionalEvent=%5B%5D&facetProfileLanguage=%5B%5D&facetRegion=%5B%5D&facetSchool=%5B%5D&facetSeniority=%5B%5D&facetServiceCategory=%5B%5D&facetState=%5B%5D&groups=%5B%5D&keywords=' + recruiter_keyword + '&origin=GLOBAL_SEARCH_HEADER&page=1&refresh=false&skillExplicit=%5B%5D&title=NOT%20(%22CEO%22%20OR%20%22Founder%22%20OR%20%22President%22%20OR%20%22Chief%22%20OR%20%22Director%22%20OR%20%22Owner%22)&topic=%5B%5D'

    actions = ActionChains(driver)

    username = str(email_var)
    password = str(pw_var)
    email_field_id = "username"
    pass_field_id = "password"
    login_button_xpath = "//button[contains(@type,'submit')]"
    print("Logging in", end="...")
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

    if pause_time > 0:
        driver.get('http://www.google.com')
        countdown(pause_time)

    agent = driver.execute_script("return navigator.userAgent")
    print('')
    loopy = 0

    driver.get(recruiter_URL)
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
    errors = 0
    while loopy < iterations:
        if errors < 6:
            link_list = []
            link_count = 0
            county_boi = 0
            results_found_elem = ''
            try:
                results_found_elem = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath(
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
                    if not link_list:
                        loopy += 1
                        errors += 1
                        continue
                    profile_wrapper_to_link_count = 0
                    for e in profile_wrappers:
                        result_text = str(e.get_attribute('innerHTML')).lower()
                        if any(sub in result_text for sub in exclusion_list):
                            profile_wrapper_to_link_count += 1
                        else:
                            try:
                                profile_list.append(link_list[profile_wrapper_to_link_count])
                            except IndexError:
                                profile_list.append(0)
                            finally:
                                profile_wrapper_to_link_count += 1
            loopy += 1
            driver.get('http://www.google.com')
            time.sleep(10)
            page = str(loopy + 1)
            recruiter_URL = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%' + encode + '%22%5D' + \
                            '&facetIndustry=%5B%2296%22%2C%22124%22%2C%224%22%2C%2257%22%2C%2280%22%2C%2298%22%2C%2211%22%2C%22118' \
                            '%22%2C%2251%22%2C%2253ejt%22%2C%2254%22%2C%226%22%2C%2284%22%2C%2291%22%2C%221%22%2C%22102%22%2C%22112' \
                            '%22%2C%22114%22%2C%22116%22%2C%22117%22%2C%22119%22%2C%2212%22%2C%22123%22%2C%22134%22%2C%22135%22%' \
                            '2C%22137%22%2C%22138%22%2C%22143%22%2C%22144%22%2C%22146%22%2C%22147%22%2C%2217%22%2C%2219%22%2C%' \
                            '2220%22%2C%223%22%2C%2231%22%2C%2240%22%2C%2241%22%2C%2247%22%2C%2249%22%2C%225%22%2C%2252%22%2C%' \
                            '2255%22%2C%2256%22%2C%2261%22%2C%2262%22%2C%227%22%2C%228%22%2C%2282%22%2C%2283%22%2C%2286%22%2C%' \
                            '2287%22%2C%2297%22%5D' \
                            '&facetNetwork=%5B%22O%22%5D&keywords=' + recruiter_keyword + \
                            '&origin=FACETED_SEARCH&page=' + page + \
                            '&title=NOT%20(' \
                            '%22CEO%22%20OR%20%22Founder%22%20OR%20%22' \
                            'President%22%20OR%20%22Chief%22%20OR%20%22Director%22%20OR%20%22Owner%22)'

            driver.get(recruiter_URL)
            print(".", end="")
    driver.quit()
    profiles = len(profile_list)

    with open(file_name, 'a+', newline='') as my_file:
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
