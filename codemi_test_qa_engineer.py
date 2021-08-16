from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import random
import os

url = "https://twitter.com/login"
number = str(random.random())

email           = ["makisekurisu993", "kurisuchanneler99@gmail.com"]
password        = "Codemi2021"
text_to_tweet   = "Codemi Test - QA Engineer [Code : " + number + "]"

# Open Firefox and redirect to Twitter
driver = webdriver.Firefox()
driver.get(url)

# Test Case 1 : Login
# Bot Handler
try:
    elem = driver.find_element(by=By.XPATH, value="//input[@name='session[username_or_email]']")
    elem.is_displayed()
    pass
except NoSuchElementException:
    driver.implicitly_wait(10)
    inputemail = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    inputemail.send_keys(email[1])
    loginbtn = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
    loginbtn.click()

    driver.implicitly_wait(10)
    inputpassword = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input")
    inputpassword.send_keys(password)
    loginbtn = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
    loginbtn.click()
except NoSuchElementException:
    driver.implicitly_wait(10)
    inputemail = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    inputemail.send_keys(email[0])
    loginbtn = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
    loginbtn.click()

    driver.implicitly_wait(10)
    inputpassword = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input")
    inputpassword.send_keys(password)
    loginbtn = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
    loginbtn.click()
    pass

# Login using email and password
driver.implicitly_wait(10)
inputemail = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
inputemail.send_keys(email[0])
inputpassword = driver.find_element_by_xpath("//input[@name='session[password]']")
inputpassword.send_keys(password)
loginbtn = driver.find_element_by_xpath("//div[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
loginbtn.click()

# Fail login handler
try:
    elem = driver.find_element(by=By.CLASS_NAME, value='DraftEditor-root')
    elem.is_displayed()
    pass
except NoSuchElementException:
    driver.implicitly_wait(10)
    inputemail = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    inputemail.send_keys(email[0])
    inputpassword = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
    inputpassword.send_keys(password)
    loginbtn = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
    loginbtn.click()
    pass

# Test Case 2 : Post a tweet
# Fill tweet content
driver.implicitly_wait(10)
driver.find_element_by_class_name('DraftEditor-root').click()
tweet=driver.find_element_by_class_name('public-DraftEditorPlaceholder-root')
ActionChains(driver).move_to_element(tweet).send_keys(text_to_tweet).perform()

# Hit tweet button
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span").click() #Text
time.sleep(10)

# Test Case 3 : Post an image [screenshoot of web browser]
# Take screenshoot and upload it
driver.save_screenshot("home-twitter.png")
win_username = os.getenv('username')
ss_image = os.path.join("C:\Users\\" + win_username + "\Documents\Twitter Automation\home-twitter.png")

driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/input').send_keys(ss_image)
time.sleep(10)

# Post it as tweet
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span").click() #Text
time.sleep(10)

print("Success create a Tweet and an image post!")


# -----------------------------------------------------------------------------------
# | Created for Twitter automation on 17 of August 2021 using Visual Studio Code    |
# | Frisco Kharisma                                                                 |
# -----------------------------------------------------------------------------------