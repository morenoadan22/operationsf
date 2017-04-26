import time
import sys
import re
import logging
import platform
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from faker import Factory


def getChromedriverPath():
   return '/lib/python2.7/site-packages/selenium/webdriver/chrome/chromedriver' if platform.system() == 'Linux' else '/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver'


def findAndClickNext():
   nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
   driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
   time.sleep(randint(1,3))
   nxt_btn.click()

def generateFakeCredentials():
   global email
   global phone_number
   fake = Factory.create('en_US')
   email = fake.free_email()
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


def main():
   initLogger()
   setupChrome()
   driver.get('http://www.surveymonkey.com/r/RN2LPQX')
   star_time = time.time()
   generateFakeCredentials()
   # input email and phone
   email_field = "106663941"
   phone_field = "106663942"

   elem = driver.find_element_by_name(email_field)
   elem.clear()
   elem.send_keys(email)
   elem.send_keys(Keys.RETURN)

   elem = driver.find_element_by_name(phone_field)
   elem.clear()
   elem.send_keys(phone_number)
   elem.send_keys(Keys.RETURN)

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
   logger.info("Email: " + email + ", Phone: " + phone_number + " Time Spent: " + str(elapsed_time))
   time.sleep(randint(1,3))
   driver.quit()




if __name__ == '__main__':
    main()
