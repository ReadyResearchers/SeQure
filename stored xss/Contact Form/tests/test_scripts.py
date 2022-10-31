from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pytest

def script_1(script):
    driver = webdriver.Chrome(executable_path="C:/Users/alexi/Desktop/chromedriver/chromedriver")
    driver.get("https://xss-game.appspot.com/level1/frame")
    search_field = driver.find_element(By.ID, 'query') # finds id named query
    search_field.send_keys(script) # searches for query;send script
    button = driver.find_element(By.ID, "button") # creates button
    time.sleep(5)
    driver.execute_script("arguments[0].click();", button) # finds button; presses button
    time.sleep(5)