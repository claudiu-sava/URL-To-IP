from selenium import webdriver
from time import sleep
from urllib.parse import urlparse
import socket

# chromedriver file options
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# the chromedriver file should be placed inside /content folder
# chromedriver options are linked to options argumend (see above)
driver = webdriver.Chrome("chromedriver/chromedriver.exe", options=options) 
driver.get("https://www.python.org") # the chromedriver opens a page (random set)

link = driver.current_url # link = browser url
x = 1
while True: # always
    if link == driver.current_url:
        while x == 1: 
            print(driver.current_url + " || " + socket.gethostbyname(urlparse(driver.current_url).netloc)) # prints the url + ip
            x = x + 1 # changes the x value, so that the message is displayed only one time the user visits the page
    else:
        print(driver.current_url + " || " + socket.gethostbyname(urlparse(driver.current_url).netloc)) # prints the url + ip
        link = driver.current_url # update the link variable with the new url the user has visited
        x = 1 # changes the x value, so that the if function can print the text again
    sleep(1) # one second of skip before the program rund the while function again
