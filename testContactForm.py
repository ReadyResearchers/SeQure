"""Tester to check the version and HTML elements."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

def test_setup():
    global driver
    options = Options()
    options.headless = True
    s = Service("C:/Program Files/chromedriver")
    driver = webdriver.Chrome(service=s, options=options)
    driver.implicitly_wait(10)
    driver.get("https://lex.chompe.rs/contact-form-5-5-2/")

def test_send_email():
    try: # these try blocks will get what version we are working with
        driver.find_elements(By.NAME,"your-subject")
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)

    except:
        print("Element does not exist.")

def test_stay_open():
    time.sleep(10)
    driver.quit()
    print("Test completed.")
