import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = input("Enter your username: ")
PASSWORD = input("Enter your password: ")

def get_followers():
    pass

def get_following():
    pass

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

browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]').click()
browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()