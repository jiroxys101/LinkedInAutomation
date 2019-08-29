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
from bs4 import BeautifulSoup
import mitmproxy
from mitmproxy import ctx

is_int = True

d = datetime.now().strftime("%I:%M %p")
print(d)

log_in = \
    {"Rijul Kumar": ["rijulkumar.webtrafik@gmail.com", "Gocam2020"],
          "Omotayo Ogunnusi": ["tayoogunnusi@outlook.com", "Temitope5"],
          "Rijul K": ["rijulkumar7500@gmail.com", "nov192011"],
          "Prasad Pansare": ["prasadpansare2019@gmail.com", "Gocam2020"],
          "Dieudonné Ndjebayi": ["rijul.kumar@construction.com", "Gocam2020"],
          "Sushma Kumar": ["sush126.kumar@gmail.com", "Dmnd2017"]
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
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    ]

master = Tk()

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
        email_var = log_in.get(variable1.get(), "")[0]
        global pw_var
        pw_var = log_in.get(variable1.get(), "")[1]
        print("Name: ", name_var + " |", end = " ")
        print("E-Mail: ", email_var + " |", end = " ")
        print("Password: ", pw_var + " |", end = " ")

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

filename = askopenfilename(title = str(email_var), initialdir = r"C:\Users\jirox_000\Desktop\Business Scripts\First Degree Connections")
print(filename)

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
    print(" Starting!")

countdown(pause_time)
print('Reading CSV file...')
with open(filename, "rt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        results.append(row[0])
csvfile.close()
print('File Read! | ' + results[0] + " | "+ os.getcwd())


def setup():
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
    driver.set_page_load_timeout(60)

    actions = ActionChains(driver)

    username = str(email_var)
    password = str(pw_var)
    email_field_id = "username"
    pass_field_id = "password"
    login_button_xpath = "//button[contains(@type,'submit')]"
    print("Logging in...", end = " ")

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
    print(user_agent)
    driver.save_screenshot('screenie.png')
    logo_x_path = "(//span[contains(@id, 'feed-tab-icon')])"
    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(logo_x_path))
    print("Log in successful")

    agent = driver.execute_script("return navigator.userAgent")
    print(str(agent))

    count1 = 0  # counter to loop through array of links
    count2 = 0  # counter to check for recurring instances of NoSuchElement Exceptions
    count3 = 0  # counter to keep track of successful sent invitations
    county_boi = 0

    if len(results) < 25:
        num = len(results)
    else:
        num = random.randint(15, 35)  # testing, set to 5
    total_time = 0
    print(str(num) + " profiles")
    while county_boi < (num - count2):
        if count2 < 3:
            start_time = time.time()

            #  refresh page if it takes longer than 10 seconds to load

            while True:
                try:
                    driver.get(results[count1])
                except TimeoutException:
                    continue
                else:
                    break
            # check for name

            # page_source = str(driver.page_source)
            # start_pos = page_source.find('industryName')
            # end_pos = page_source.find(',', start_pos)
            # industry_name = page_source[start_pos + 15:end_pos - 1]
            # industry_name = str(industry_name.replace(' &amp; ', ' & '))

            name_xpath = "//li[contains(@class,'t-24')]"

            try:
                name_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(name_xpath))
                full_name = name_element.get_attribute('innerText')
                full_name = str(full_name.title())
                full_name = full_name.strip()
                first_name = full_name.split(" ", 1)[0]
            except TimeoutException:
                print("Name not found. Skipping...")
                errors.append(results[count1])
                count1 += 1
                count2 += 1
                driver.save_screenshot('screenie.png')
                time.sleep(random.randint(5, 15))
                continue
            time.sleep(random.randint(1, 3))  # test

            area_list = ["new york", "new jersey", "toronto", "mississauga", "brampton", "scarborough", "philadelphia",
                         "connecticut", "maryland", "washington d.c.", "delaware", "washington, district of columbia",
                         "virginia", "pennsylvania", "ontario" , "united states"]
            location_xpath = "//li[contains(@class,'t-16 t-black t-normal inline-block')]"
            try:
                location_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
                                                                       (location_xpath))
                location = str(location_element.get_attribute('innerText')).lower()
                print(str(count1 + 1) + " | " + location.title() + " | ", end = " ")
                if any(sub in location for sub in area_list):
                    print("|", end = " ")
                else:
                    errors.append(results[count1] + " - outside location area - " + location)
                    count1 += 1
                    print("Invalid location. Skipping...")
                    time.sleep(random.randint(2, 18))
                    continue
            except TimeoutException:
                errors.append(results[count1])
                count1 += 1
                print("Error: No location area detected")
                time.sleep(random.randint(5, 15))
                continue

            lenOfPage = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
                "var lenOfPage=document.body.scrollHeight;return lenOfPage;")

            match = False
            while match is False:
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                    "var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount == lenOfPage:
                    match = True
            time.sleep(1)

            see_more_xpath = "//button[contains(@class,'additional-skills')]"
            body = driver.find_element_by_css_selector('body')
            scroll = 0

            while scroll < 1:
                scroll += 0.1
                body.send_keys(Keys.PAGE_UP)
                time.sleep(1)
            time.sleep(1)

            see_more_xpath = "//button[contains(@class,'additional-skills')]"
            try:
                see_more_element = WebDriverWait(driver, 15).until(
                    lambda driver: driver.find_element_by_xpath(see_more_xpath))
            except TimeoutException:
                errors.append(results[count1])
                count1 += 1
                # count2 += 1
                print("No Skills listed. Skipping...")
                time.sleep(random.randint(5, 15))
                continue
            else:
                driver.execute_script('arguments[0].click();', see_more_element)

            elems = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_xpath(
                "//span[contains(@class, 'pv-skill-category-entity')]"))

            skill_list = []
            skill_variable = 'interpersonal'

            for elem in elems:
                skill = str(elem.text.lower())
                skill_list.append(skill)

            if any('leader' in s for s in skill_list):
                skill_variable = "leadership"
            else:
                if any('management' in s for s in skill_list):
                    skill_variable = "management"
                else:
                    skill_variable = "interpersonal"

            message = "Hi " + first_name + \
                      ". I was going through your profile and I couldn't help but " \
                      "notice that you've been endorsed for possessing a variety of skills, including " + \
                      skill_variable +\
                      ". Have you considered utilizing your skills and working for yourself on the side," \
                      " without impacting your existing work commitments?"

            while True:
                try:  # see if their is an open message window
                    msg_close_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath
                                                                        ("//button[contains(@class, 'msg-close')]"))
                    print("Open Message Window. Closing...")
                    msg_close_element.click()
                    time.sleep(random.randint(3, 7))
                except TimeoutException:
                    break
            # check for message button
            current_position_xpath = "//h4[contains(@class,'date-range')]"
            try:
                current_position_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
                                                                       (current_position_xpath))
                position = str(current_position_element.get_attribute('innerHTML')).lower()
                if "present" in position:
                    print("Employed" + " | ", end = " ")
                else:
                    errors.append(results[count1] + " - Not Currently Employed")
                    count1 += 1
                    print("Not Currently Employed")
                    time.sleep(random.randint(2, 18))
                    continue
            except TimeoutException:
                errors.append(results[count1] + " - No current position")
                count1 += 1
                count2 += 1
                print("No current position")
                time.sleep(random.randint(2, 18))
                continue

            try:
                message_button_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath
                                                                        ("//button[contains(@class, 'message')]"))
                # actions.move_to_element(message_button_element).perform()
                driver.execute_script('arguments[0].click();', message_button_element)

            except TimeoutException:
                errors.append(results[count1])
                count1 += 1
                count2 += 1
                print("No Message Button. Skipping...")
                time.sleep(random.randint(5, 15))
                continue

            script = message

            # check for previously sent
            try:
                message_area_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(
                    "//ul[contains(@class,'msg-s-message-list-content')]"))
                time.sleep(5)
                if "couldn't help but notice" in str(message_area_element.get_attribute(
                        'innerHTML')):
                    errors.append(results[count1] + " - already messaged")
                    count1 += 1
                    print("Previously messaged. Skipping...")
                    time.sleep(random.randint(2, 18))
                    continue
                else:
                    pass
            except TimeoutException:
                pass
            finally:
                print(first_name + " | ", end=" ")  # Success - no previous message detected

            # check for text area
            try:
                text_area_element = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
                                                                    ("//div[contains(@role, 'text')]"))
            except TimeoutException:
                errors.append(results[count1])
                count1 += 1
                print("Error: No text area detected")
                time.sleep(random.randint(5, 15))
                continue

            try:
                send_button_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath
                                                                     ("//button[contains(@class, 'send-button')]"))
            except TimeoutException:
                errors.append(results[count1])
                count1 += 1
                count2 += 1
                print("Error: No Send button detected")
                time.sleep(random.randint(5, 15))
                continue
            else:
                text_area_element.send_keys(script)
                time.sleep(5)
                driver.execute_script('arguments[0].click();', send_button_element)
                time.sleep(random.randint(1, 15))

                end_time = time.time() - start_time
                total_time += end_time

                count1 += 1
                count3 += 1
                county_boi += 1
                count2 = 0
                print(str(round(end_time, 2)) + " seconds | " + str(count3))

        else:
            driver.quit()
            break

    time.sleep(random.randint(1, 3))

    if count2 != 3:
        for x in range(0, count1):
            results.pop(0)
        fop = open(filename, "w+")
        fop.close()

        with open(filename, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in results:
                writer.writerow([val])

    print("done")


    if count3 != 0:
        avg_time = total_time / count3
    else:
        avg_time = total_time / 3

    print("Invitations Sent. Last Profile Messaged: " + str(full_name))
    print("Average Time Per Profile: " + str(round(avg_time, 2)) + " seconds")
    print(str(round(total_time, 2)) + " seconds")
    count4 = 0
    while count4 < len(errors):
        print(errors[count4])
        count4 += 1

    from datetime import datetime
    f = datetime.now().strftime("%I:%M %p")
    print("Start: " + d + " | " + "End: " + f)
    print("Successful Number of Invitations Sent: " + str(count3))


def teardown(self):
    self.driver.quit()


setup()
