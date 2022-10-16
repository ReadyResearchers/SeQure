from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import time
import os

driver = webdriver.Chrome(executable_path="C:/Users/alexi/Desktop/chromedriver/chromedriver") # path to chromedriver

def sendScripts():
    # This function works
    driver.find_element(By.ID, 'query').send_keys("<Script>alert('Script Passed.')</scripT>")
    # this finds the button
    button = driver.find_element(By.ID,'button')
    time.sleep(10) # sleeps for 5 seconds
    # this clicks the button
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5) # sleeps for 5 seconds
    driver.quit() # closes the window

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    url = input("[+] Enter the URL you would like to check: ")
    driver.get(url) # opens an automated browser
    sendScripts()
    
    # https://xss-game.appspot.com/level1/frame
