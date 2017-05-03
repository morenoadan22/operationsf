import time
import sys
import re
import logging
import platform
from unidecode import unidecode
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from faker import Factory

survey_url = 'http://www.surveymonkey.com/r/BG3JM7R'
first_field = "109336225"
last_field = "109336226"
email_field = "109336227"
phone_field = "109336228"

def getChromedriverPath():
   return '/lib/python2.7/site-packages/selenium/webdriver/chrome/chromedriver' if platform.system() == 'Linux' else '/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver'

def findAndClickNext():
   nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
   driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
   time.sleep(randint(1,3))
   nxt_btn.click()

def generateFakeCredentials():
   global firstName
   global lastName
   global email
   global phone_number
   countryCode = 'en_US' if randint(0, 2) < 1 else 'es_MX'
   fake = Factory.create(countryCode)
   name = fake.name().split()
   firstName = name[0] if "." not in name[0] else ''
   lastName = name[1]   
   email = unidecode(fake.free_email())
   number = fake.phone_number()
   if number.find('x') != -1:
      number = number[:number.index('x')]
   number = re.sub("[^0-9]", "", number)
   number = "760" + number[3:]
   number = (number[:10]) if len(number) > 10 else number
   phone_number = number

def initLogger():
   global logger
   logger = logging.getLogger('missiontrump')
   hdlr = logging.FileHandler('votes.log')
   formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
   hdlr.setFormatter(formatter)
   logger.addHandler(hdlr)
   logger.setLevel(logging.INFO)

def setupChrome():
   global driver
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("-incognito")
   driver = webdriver.Chrome(executable_path=getChromedriverPath(), chrome_options=chrome_options)   

def fillInputWithName(fieldName, value):
   elem = driver.find_element_by_name(fieldName)
   elem.clear()
   elem.send_keys(value)
   elem.send_keys(Keys.RETURN)   

def startVotingProcess():   
   setupChrome()
   driver.get(survey_url)
   star_time = time.time()
   generateFakeCredentials() 

   fillInputWithName(first_field, firstName)
   fillInputWithName(last_field, lastName)
   fillInputWithName(email_field, email)
   fillInputWithName(phone_field, phone_number)

   for x in range(0, 6):
      findAndClickNext()
   
   # select marianne's state farm checkbox
   vote_check = driver.find_element_by_xpath("//*[contains(text(), 'Marianne Valenzuela Fenley')]")
   driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-30);", vote_check)
   time.sleep(randint(1,3))
   vote_check.click()
   time.sleep(randint(1,3))

   for x in range(0, 2):
      findAndClickNext()
   
   submit_btn = driver.find_element_by_css_selector(".survey-page-button.done-button")
   driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", submit_btn)
   time.sleep(randint(1,3))
   submit_btn.click()

   elapsed_time = time.time() - star_time
   logger.info("Name:" + lastName + ", " + firstName +" Email: " + email + " Phone: " + phone_number + " Time Spent: " + str(elapsed_time))
   time.sleep(randint(1,3))
   driver.quit()

def main():
   initLogger()      
   for x in range(0, int(sys.argv[1])):      
         startVotingProcess()
      

if __name__ == '__main__':
    main()
