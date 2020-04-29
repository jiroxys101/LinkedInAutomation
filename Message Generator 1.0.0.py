import pyperclip
import random
from datetime import datetime
import os
import time
from requests import get

greetings1 = ["Hi", "Hello"]
greetings2 = ["Hi", "Hello", "Good Morning", "Morning"]
greetings3 = ["Hi", "Hello", "Good Afternoon", "Afternoon"]
greetings4 = ["Hi", "Hello", "Good Evening", "Evening"]

interpersonal_skills_array = ['interpersonal', 'management', 'communication', 'leadership', 'teamwork']

is_int = True

while is_int:
    try:
        vpn = int(input("1 for VPN, 2 for None: "))
    except ValueError:
        print("Sorry. That value is not an integer.", end=" ")
        pass
    else:
        if isinstance(vpn, int):
            if vpn == 1:
                try:
                    os.system(
                        'tasklist | find /i "CyberGhost.exe" && taskkill /im "CyberGhost.exe" /F || echo VPN not running')
                except Exception:
                    print('...', end="")
                finally:
                    is_int = False
                    ip1 = str(get('https://api.ipify.org').text)
                    print(ip1, end="")
                    os.startfile('C:\\Program Files\\CyberGhost 7\\CyberGhost.exe')
                    ip2 = ip1
                    while True:
                        try:
                            ip2 = str(get('https://api.ipify.org').text)
                        except Exception:
                            pass
                        else:
                            if ip2 != ip1:
                                ip = str(get('https://api.ipify.org').text)
                                print(ip)
                                break
                            else:
                                print('.', end="")
                                time.sleep(1)
            elif vpn == 2:
                is_int = False
                break
            else:
                print("Invalid Entry", end=" | ")
        else:
            is_int = True
            print("Sorry. That value is not an integer.", end=" ")

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

line_1 = ['Hope you are doing well during this time with everything that has been going on. ',
              'Hope you are staying safe with everything that has been going on. ',
              'Hope you are staying healthy with everything that has been going on. ',
              'Hope you are staying safe during this time with everything that has been going on. ',
              'Hope you are staying healthy during this time with everything that has been going on. ',
              'Hope you are staying safe and healthy with everything that has been going on. ',
              'Hope you are staying safe and healthy during this time. ',
              'Hope you and yours are doing well with everything that has been going on. ',
              'Wish you safety and good health during this time with everything that has been going on. ',
              'Hope you and yours are staying safe with everything that has been going on. ',
              'Hope you and yours are staying healthy with everything that has been going on. ',
              'Hope you and yours are staying safe and healthy during this time with everything that has been going on. '
         ]

line_2 = 'I understand that there is a lot of uncertainty in the air today. '

line_3 = [
    'As an organization, we are looking to assemble a team to help us develop a larger market presence. ',
    'My organization is looking to assemble a team to help us develop a larger market presence. '
]

line_4 = "I was going through your profile and couldn't" \
         " help but notice that you have been endorsed for a variety of skills, including "

line_5 = [
    'After looking at your profile, I wanted to ask. ',
    'After looking at your profile, I wanted to follow-up. ',
    'After taking a look at your profile, I want to ask. ',
    'After taking a look at your profile, I want to follow-up. '
]

line_6 = [
    'Have you ever given any thought to utilizing your skills to develop a business outside of your career, ',
    'Have you ever given any thought to utilizing your skills to develop a business outside of your job, ',
    'Have you ever given any thought to utilizing your skills to develop a business outside of your profession, ',
    'Do you ever think about using your skills to develop a business outside of your career, ',
    'Do you ever think about using your skills to develop a business outside of your job, ',
    'Do you ever think about using your skills to develop a business outside of your profession, ',
    'Did you ever consider using your skills to develop a business outside of your career, ',
    'Did you ever consider using your skills to develop a business outside of your job, ',
    'Did you ever consider using your skills to develop a business outside of your profession, ',
    'Have you ever thought about utilizing your skills to develop a business outside of your career, ',
    'Have you ever thought about utilizing your skills to develop a business outside of your job, ',
    'Have you ever thought about utilizing your skills to develop a business outside of your profession, ',
    'Have you ever thought about using your skills to develop a business outside of your career, ',
    'Have you ever thought about using your skills to develop a business outside of your job, ',
    'Have you ever thought about using your skills to develop a business outside of your profession, ',
    'Do you have an interest in working for yourself on the side, ',
    'Have you ever thought about working for yourself on the side, '
]

line_7 = ['without impacting your existing commitments?',
          'without having any impact on the current obligations?',
          'without affecting your current commitments?',
          'without affecting your current obligations?',
          'without affecting your existing commitments?'
          ]

rep_1 = ["The reason I ask is that I work with a business development group that partners with several online retailers and other service providers, helping them expand their market base. ",
         "The reason I ask is that my organization collaborates with various online merchants, assisting them in growing and retaining their market base. ",
         "I work with a business development group that partners with several online retailers and other service providers, helping them expand their market base. ",
         "My organization collaborates with various online merchants, assisting them in growing and retaining their market base. "
         ]

rep_2 = ["We are looking for a few individuals with an interest in business ownership to bring on, whom we will train and educate. ",
         "We are looking to select someone with the right mindset to partner up in an entrepreneurial initiative. ",
         "We are looking for a couple of partners to work with us in business development initiatives. ",
         "We are looking for a couple of business partners who can help us strategize and implement business expansion plans; someone who is accountable and has a keen interest in business ownership. ",
         "We are looking to select someone who is accountable, has a deep desire for an opportunity so that we can potentially open doors to our mentorship and partnership to do business together. "
]

rep_3 = ["Your profile gave me the impression that you may be a good fit. ",
         "Your profile gave me the impression that that would be a good fit for you. "
         ]

rep_4 = ["If that piques your interest, I would be happy to set up a time to discuss further",
         "I would be happy to set up a time to discuss further if that piques your interest",
]

is_int = True

while is_int:
    hour = datetime.now().hour
    if 5 <= int(hour) <= 11:
        greeting = random.choice(greetings1 + greetings2)
    elif 12 <= int(hour) <= 17:
        greeting = random.choice(greetings1 + greetings3)
    elif 18 <= int(hour) <= 22:
        greeting = random.choice(greetings1 + greetings4)
    else:
        greeting = random.choice(greetings1)

    try:
        num = int(input("1 for DTM, 2 for Follow-Up, 3 to reset, 4 to cancel: "))
    except ValueError:
        print("Sorry. That value is not an integer.", end=" ")
        pass
    else:
        if isinstance(num, int):
            if num == 1:
                message_script = str(greeting + " ! " + random.choice(acknowledgements) + " " + random.choice(line_1) + line_2
                                     + random.choice(line_3) + line_4 +
                                     random.choice(interpersonal_skills_array) + ". " + random.choice(line_5) +
                                     random.choice(line_6) + random.choice(line_7)
                                     )
                pyperclip.copy(message_script)
            elif num == 2:
                message_script = str(random.choice(rep_1) + random.choice(rep_2) + random.choice(rep_3) +
                                     random.choice(rep_4)
                                     )
                pyperclip.copy(message_script)
            elif num == 3:
                print("Resetting!")
                try:
                    os.system(
                        'tasklist | find /i "CyberGhost.exe" && taskkill /im "CyberGhost.exe" /F || echo VPN not running')
                except Exception:
                    print('...', end="")
                else:
                    ip1 = str(get('https://api.ipify.org').text)
                    print(ip1, end="")
                    os.startfile('C:\\Program Files\\CyberGhost 7\\CyberGhost.exe')
                    ip2 = ip1
                    while True:
                        try:
                            ip2 = str(get('https://api.ipify.org').text)
                        except Exception:
                            pass
                        else:
                            if ip2 != ip1:
                                ip = str(get('https://api.ipify.org').text)
                                print(ip)
                                break
                            else:
                                print('.', end="")
                                time.sleep(1)
            elif num == 4:
                is_int = False
                print("Closing!")
                os.system(
                    'tasklist | find /i "CyberGhost.exe" && taskkill /im "CyberGhost.exe" /F || echo VPN not running')
            else:
                print("Invalid Entry", end=" | ")
        else:
            is_int = True
            print("Sorry. That value is not an integer.", end=" ")
