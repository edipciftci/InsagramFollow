import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = input("Enter your username: ")
PASSWORD = input("Enter your password: ")

url = 'https://www.instagram.com/'
driver ='/usr/bin/chromedriver'
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(15)
browser.maximize_window()

username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
login = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
login.click()
