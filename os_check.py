import platform

chromedriver_path = '/lib/python2.7/site-packages/selenium/webdriver/chrome/chromedriver' if platform.system() == 'Linux' else '/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver'

print "System is " + platform.system() + ", therefore this is the path: " + chromedriver_path