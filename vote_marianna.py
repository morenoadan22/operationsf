import time
import sys
import re
import logging
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from faker import Factory

logger = logging.getLogger('missiontrump')

hdlr = logging.FileHandler('votes.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

lines = []
with open('./proxy_servers.txt') as file:
    lines = file.read().splitlines()

PROXY = lines[randint(0, len(lines) - 1)] # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver', chrome_options=chrome_options)

driver.get('http://www.surveymonkey.com/r/RN2LPQX')

fake = Factory.create('en_US')

#input email and phone
email_field = "106663941"
phone_field = "106663942"

elem = driver.find_element_by_name(email_field)
elem.clear()
email = fake.free_email()
elem.send_keys(email)
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_name(phone_field)
elem.clear()
number = fake.phone_number()
if number.find('x') != -1:
	number = number[:number.index('x')]
number = re.sub("[^0-9]", "", number)
number = "760" + number[3:]
number = (number[:10]) if len(number) > 10 else number
elem.send_keys(number)
elem.send_keys(Keys.RETURN)

logger.info("Email: " + email + ", Phone: " + number + " Proxy: " + PROXY)

#user info page
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
nxt_btn.click()

#best food and drinks (part 1 of 3)
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click()

# #best food and drinks (part 2 of 3) 
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click()

# best food and drinks (part 3 of 3)
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click()

# beauty and fitness
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click()

# best goods and services (part 1 of 2)
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click()

# best goods and services (part 2 of 2)
# select marianne's state farm checkbox
vote_check = driver.find_element_by_xpath("//*[contains(text(), 'Marianne Valenzuela Fenley')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-30);", vote_check)
time.sleep(randint(1,3))
vote_check.click()
time.sleep(randint(1,3))
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click() 

# best health services
nxt_btn = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", nxt_btn)
time.sleep(randint(1,3))
nxt_btn.click()

# submit the survey
submit_btn = driver.find_element_by_css_selector(".survey-page-button.done-button")
driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", submit_btn)
time.sleep(randint(1,3))
submit_btn.click()
time.sleep(randint(1,3))


driver.quit()
	


