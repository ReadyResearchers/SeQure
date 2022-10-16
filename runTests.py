from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def testScripts(script):
    driver = webdriver.Chrome(executable_path="C:/Users/alexi/Desktop/chromedriver/chromedriver")
    driver.get("https://xss-game.appspot.com/level1/frame")
    search_field = driver.find_element(By.ID, 'query') # finds id named query
    search_field.send_keys(script) # searches for query;send script
    button = driver.find_element(By.ID, "button") # creates button
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