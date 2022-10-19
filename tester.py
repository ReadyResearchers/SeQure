from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

s = Service("C:/Users/alexi/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=s) # path to chromedriver

def storedCrossSite():
    print()

def cookieCrossSite():
    print()

def reflectedCrossSite():
    # This finds the element and passes in a script
    #driver.find_element(By.NAME, 'your-name').send_keys("<Script>alert('Script Passed.')</scripT>") # version 2.0.1; 4.0.1
    #driver.find_element(By.NAME, 'scripttag').send_keys("<script>alert('Script Passed.')</script>") # version 2.0.1
    # this finds the button
    # button = driver.find_element(By.XPATH, "//input[@type='submit']") # button for version 2.0.1
    # button = driver.find_element(By.XPATH,"//input[@class='wpcf7-form-control wpcf7-submit']") # button for version 4.0.1
    #time.sleep(10) # sleeps for 5 seconds
    # this clicks the button
    # driver.execute_script("arguments[0].click();", button)
    #time.sleep(5) # sleeps for 5 seconds
    #driver.quit() # closes the window

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    #url = input("[+] Enter the URL you would like to check: ")
    #driver.get("https://lex.chompe.rs/contact-form-v4-0-1/") # version 4.0.1
    #driver.get("https://lex.chompe.rs/contact-form-7-v1-1/") # version 2.0.1
    #reflectedCrossSite()
    # https://xss-game.appspot.com/level1/frame
