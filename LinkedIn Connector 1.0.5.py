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
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import logging
import atexit
import smtplib
import ssl
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


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
filename = askopenfilename(title = str(email_var), initialdir = r"C:\Users\jirox_000\Desktop\Business Scripts\Second Degree Connections")
print(filename)

results = []
errors = []


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
# chrome_options.add_argument('--profile-directory=Default')
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
        print("Sorry.  That value is not an integer.", end=" | ")

print("Pausing for " + str(pause_time) + " seconds")


def countdown(t):
    while t >= 0:
        sys.stdout.write('\r' + str(t) + ' seconds left')
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    print(" Starting!")


countdown(pause_time)


with open(filename, "rt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        results.append(row[0])
csvfile.close()
print(results[0])
print(os.getcwd())


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
    print("Logging in...", end=" | ")
    driver.save_screenshot('screenie.png')
    agent = driver.execute_script("return navigator.userAgent")
    print(str(agent))

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
    # time.sleep(60)
    count1 = 0  # counter to loop through array of links
    count2 = 0  # counter to check for recurring instances of NoSuchElement Exceptions
    count3 = 0  # counter to keep track of successful sent invitations

    if len(results) < 150:
        num = len(results)
        print(str(num) + " profiles left")

    else:
        num = random.randint(100, 200)  # set to 5 for testing
        print(str(num) + " profiles")

    total_time = 0                             
    try:
        while count3 < num:
                if count2 < 5:  # test
                    if count1 != 0:
                        if count1 % 25 == 0:  # test
                            driver.get('http://www.google.com')
                            print('Threshold met. Waiting at Google')
                            countdown(random.randint(1800, 5000))
                            print(str(count1 + 1), end=" | ")
                        else:
                            print(str(count1 + 1), end=" | ")
                    else:
                        print(str(count1 + 1), end=" | ")

                    start_time = time.time()

                    #  refresh page if it takes longer than 10 seconds to load

                    try:
                        driver.get(results[count1])
                    except TimeoutException:
                        continue
                    except IndexError:
                        print("End of list reached")
                        break

                    # check for name

                    lenOfPage = driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);"
                        "var lenOfPage=document.body.scrollHeight;return lenOfPage;")

                    footer_xpath = '//p[contains(@id, "globalfooter-copyright")]'
                    body = driver.find_element_by_css_selector('body')
                    experience_see_more = "//button[contains(@class,'see-more-inline')]"
                    see_more_xpath = "//button[contains(@class,'additional-skills')]"

                    match = False
                    while match is False:
                        lastCount = lenOfPage
                        time.sleep(2)
                        lenOfPage = driver.execute_script(
                            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                        if lastCount == lenOfPage:
                            match = True
                    time.sleep(1)
                    scroll = 0
                    while scroll < 1:
                        scroll += 0.02
                        body.send_keys(Keys.ARROW_UP)
                        time.sleep(0.05)
                    time.sleep(1)

                    try:
                        see_more_element = WebDriverWait(driver, 7).until(
                            lambda driver: driver.find_element_by_xpath(see_more_xpath))
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        count2 += 1
                        print("No Skills listed. Skipping...")
                        time.sleep(random.randint(1, 6))
                        continue
                    else:
                        driver.execute_script('arguments[0].click();', see_more_element)

                    elems = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_xpath(
                        "//span[contains(@class, 'pv-skill-category-entity')]"))

                    skill_list = []
                    skill_variable = 'interpersonal'

                    try:
                        descriptions = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_xpath(
                            "//h4[contains(@class,'date-range')]"))
                    except TimeoutException:
                        print("No descriptions found", end=' | ')
                    else:
                        last_element = int(len(descriptions) - 1)
                        driver.execute_script('arguments[0].scrollIntoView(true);', descriptions[last_element])

                    try:
                        experience_button = WebDriverWait(driver, 5).until(
                            lambda driver: driver.find_element_by_xpath(experience_see_more))
                    except TimeoutException:
                        print("No Experience Button Found", end=" | ")
                    else:
                        driver.execute_script('arguments[0].scrollIntoView(true);', experience_button)
                        driver.execute_script('arguments[0].click();', experience_button)
                    try:
                        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(experience_see_more))
                    except TimeoutException:
                        print("No Experience Button Found", end=" | ")

                    try:
                        descriptions = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_xpath(
                            "//h4[contains(@class,'date-range')]"))
                    except TimeoutException:
                        print("No descriptions found")
                        count1 += 1
                        continue
                    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
                    try:
                        years = WebDriverWait(driver, 7).until(lambda driver: driver.find_elements_by_xpath(
                            "//span[contains(@class,'bullet-item-v2')]"))
                    except TimeoutException:
                        print("No years found")
                        count1 += 1
                        continue
                    else:
                        driver.execute_script('arguments[0].scrollIntoView(true);', years[len(years)-1])
                    time.sleep(5)

                    years_array = []
                    present_array = []
                    descriptions_array = []

                    try:
                        years = WebDriverWait(driver, 7).until(lambda driver: driver.find_elements_by_xpath(
                            "//span[contains(@class,'bullet-item-v2')]"))
                    except TimeoutException:
                        print("No years found")
                        count1 += 1
                        continue

                    # print(len(years), end=" | ") # comment out when code is confirmed to work
                    # print(len(descriptions), end=" | ")

                    for e in years:
                        if 'yrs' in e.get_attribute('innerText'):
                            years_array.append(e.get_attribute('innerText'))
                        elif 'mos' in e.get_attribute('innerText'):
                            years_array.append(e.get_attribute('innerText'))

                    try:
                        descriptions = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_xpath(
                            "//h4[contains(@class,'date-range')]"))
                    except TimeoutException:
                        print("No descriptions found")
                        count1 += 1
                        continue
                    else:
                        driver.execute_script('arguments[0].scrollIntoView(true);', descriptions[len(descriptions)-1])

                    for e in descriptions:
                        descriptions_array.append(e.get_attribute('innerText').lower())
                    print(str(years_array).strip('[]'), end=" | ")
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
                            present_array.append(0)
                        loop_count += 1
                    total_experience = round(total_experience / 12, 2) + round(max(present_array) / 12, 2)
                    print(str(total_experience) + " years experience", end=" | ")

                    education_x_path = "(//time)"
                    education_years = []
                    try:
                        education_times = WebDriverWait(driver, 7).until(
                            lambda driver: driver.find_elements_by_xpath(education_x_path))
                    except TimeoutException:
                        print("No Education Years Present | ", end=" | ")
                        if total_experience >= 18:
                            print("Above Maximum Experience")
                            errors.append(results[count1] + " - outside experience range")
                            count1 += 1
                            continue
                        elif total_experience < 1:
                            print("Below Minimum Experience")
                            errors.append(results[count1] + " - outside experience range")
                            count1 += 1
                            continue
                        else:
                            print("Within Experience Demographic", end=" | ")
                    else:
                        for e in education_times:
                            if re.search('[a-zA-Z]', e.get_attribute("innerText")):
                                education_years.append(e.get_attribute("innerText").lower())
                            else:
                                education_years.append(int(e.get_attribute("innerText")))
                        age = (2019 - min(education_years)) + 18
                        print('~' + str(age) + ' years old', end=" | ")
                        if min(education_years) < 2001:
                            print("Above Maximum Age")
                            errors.append(results[count1] + " - outside age range")
                            count1 += 1
                            continue
                        elif max(education_years) > 2019:
                            print("Below Minimum Age")
                            errors.append(results[count1] + " - currently student")
                            count1 += 1
                            continue
                        else:
                            if total_experience >= 18:
                                print("Above Maximum Experience")
                                errors.append(results[count1] + " - outside experience range")
                                count1 += 1
                                continue
                            elif total_experience < 1:
                                print("Below Minimum Experience")
                                errors.append(results[count1] + " - outside experience range")
                                count1 += 1
                                continue
                            else:
                                print("Within Age & Experience Demographic | ", end=" | ")

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

                    name_xpath = "//li[contains(@class,'t-24')]"

                    try:
                        name_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(name_xpath))
                        full_name = name_element.get_attribute('innerText')
                        full_name = str(full_name.title())
                        full_name = full_name.strip()
                        first_name = full_name.split(" ", 1)[0]
                    except TimeoutException:
                        print("Name not found. Skipping...")
                        driver.save_screenshot('screenie.png')
                        errors.append(results[count1])
                        count1 += 1
                        count2 += 1
                        time.sleep(random.randint(1, 6))
                        continue

                    area_list = ["new york", "new jersey", "toronto", "mississauga", "brampton", "scarborough", "philadelphia",
                                  "maryland", "washington d.c.", "delaware", "washington, district of columbia",
                                 "virginia", "pennsylvania", "ontario", "united states", "florida", "miami", "lauderdale", "ohio",
                                 "washington dc", "washington, dc", "montreal"]
                    location_xpath = "//li[contains(@class,'t-16 t-black t-normal inline-block')]"
                    try:
                        location_element = WebDriverWait(driver, 7).until(lambda driver: driver.find_element_by_xpath
                        (location_xpath))
                        location = str(location_element.get_attribute('innerText')).lower()
                        print(location.title() + " | ", end=" | ")
                        if any(sub in location for sub in area_list):
                            print("|", end=" | ")
                        else:
                            errors.append(results[count1] + " - outside location area - " + location)
                            count1 += 1
                            print("Invalid location. Skipping...")
                            time.sleep(random.randint(1, 6))
                            continue
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        print("Error: No location area detected")
                        time.sleep(random.randint(1, 6))
                        continue

                    #check for position

                    current_position_xpath = "//h4[contains(@class,'date-range')]"
                    try:
                        current_position_element = WebDriverWait(driver, 7).until(lambda driver: driver.find_element_by_xpath
                        (current_position_xpath))
                        position = str(current_position_element.get_attribute('innerHTML')).lower()
                        if "present" in position:
                            print("Employed" + " | ", end=" | ")
                        else:
                            errors.append(results[count1] + " - Not Currently Employed")
                            count1 += 1
                            print("Not Currently Employed")
                            time.sleep(random.randint(1, 6))
                            continue
                    except TimeoutException:
                        errors.append(results[count1] + " - No current position")
                        count1 += 1
                        count2 += 1
                        print("No current position")
                        time.sleep(random.randint(1, 6))
                        continue
                    message_script = "Hi " + first_name + ". I was impressed with your profile;" \
                                     " particularly your endorsements for your " + skill_variable + " skills." \
                                     " I represent a business development organization looking to expand its partnerships." \
                                     " Have you thought about using your skills to develop a business outside of what you do?"

                    try:
                        connectButtonElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//button[contains(@class, 'connect')]"))
                        elem_class = str(connectButtonElement.get_attribute("class")).lower()
                        if "disabled" not in elem_class:
                            driver.execute_script('arguments[0].click();', connectButtonElement)
                        else:
                            count1 += 1
                            print("Invite pending. Skipping...")
                            time.sleep(random.randint(1, 6))
                            continue
                    except TimeoutException:
                        body.send_keys(Keys.HOME)
                        time.sleep(3)
                        print(' | Checking DropDown |', end=" | ")
                        try:
                            moreElement = WebDriverWait(driver, 5).until(
                                lambda driver: driver.find_element_by_xpath("//button[contains(@class,'overflow-toggle')]"))
                            time.sleep(1)
                            moreElement.click()
                        except TimeoutException:
                            errors.append(results[count1])
                            count1 += 1
                            print("Error: No More Button detected")
                            time.sleep(random.randint(1, 6))
                            continue

                        try:
                            connectListElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//artdeco-dropdown-item[contains(@class, 'connect')]"))
                        except TimeoutException:
                            errors.append(results[count1])
                            count1 += 1
                            print("Connect Button Timeout. Skipping...")
                            continue
                        else:
                            print(' | Dropdown Connect Found |', end=" | ")
                            time.sleep(3)
                            if 'remove' in connectListElement.get_attribute('innerHTML').lower():
                                print('Connection already added')
                                count1 += 1
                                continue
                            else:
                                driver.execute_script('arguments[0].click();', connectListElement)
                                print(' | Click 1 |', end=" | ")
                            time.sleep(3)
                    print(' | Checking for Add a Note |', end=" | ")
                    try:
                        addNoteElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//button[contains(.,'Add a note')]"))
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        print("Error: No Add Note Button detected")
                        time.sleep(random.randint(1, 6))
                        continue
                    else:
                        time.sleep(1)
                        driver.execute_script('arguments[0].click();', addNoteElement)
                    time.sleep(1)
                    try:
                        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_css_selector('textarea'))
                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        print("Error: No Message Area detected")
                        time.sleep(random.randint(1, 6))
                        continue
                    else:
                        textAreaElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_css_selector('textarea'))
                        textAreaElement.send_keys(message_script)
                    time.sleep(2.5)
                    try:
                        sendButtonElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//button[contains(.,'Send ')]"))
                        driver.execute_script('arguments[0].click();', sendButtonElement)
                        time.sleep(random.randint(1, 6))
                        end_time = time.time() - start_time
                        total_time += end_time

                        print(str(count3 + 1) + " - " + str(round(end_time, 2)) + " seconds")
                        count1 += 1
                        count3 += 1
                        count2 = 0

                    except TimeoutException:
                        errors.append(results[count1])
                        count1 += 1
                        print("Error: No send button detected")
                        time.sleep(random.randint(1, 6))
                        continue
                else:
                    driver.quit()
                    break
    except TimeoutException:
        logging.error(traceback.print_exc())
        message = str(os.path.basename(__file__)) + ' experienced an unhandled TimeoutException.' + '\n' + '\n' + str(traceback.format_exc())
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

    time.sleep(3)

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


    print("Invitations Sent. Last Profile Messaged: " + str(full_name))
    if count3 != 0:
        avg_time = total_time / count3
    else:
        avg_time = total_time / 3
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
