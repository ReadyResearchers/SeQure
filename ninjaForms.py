from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import sys
import time
import os



def reflectedCrossSite(url):
    results = []
    test = 1
    with open('xssPayloads.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            # name and message  ==============================================================================
            try:
                print("\n\t [+] Test #1")
                options = Options()
                options.headless = True
                s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
                driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
                driver.get(url)
                # This finds the element and passes in a script
                driver.find_element(By.NAME, 'your-name').send_keys(line)
                driver.find_element(By.NAME, 'your-message').send_keys(line)
                print("\n\t [+] HTML elements found:\n")
                # this finds the button
                button = driver.find_element(By.XPATH, "//input[@type='submit']")
                # this clicks the button
                driver.execute_script("arguments[0].click();", button)
                print("\n\t [+] Button was successfully pressed:\n")
                driver.implicitly_wait(15)
                # by class name
                checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
                mailSentOK = driver.find_element(By.CLASS_NAME, '')
                print("\n\t [+] HTML elements found:\n")
                if (checkAlert == mailSentOK):
                    print("\n\t [+] Email was successfully sent.")
                    driver.quit() # closes the window
                    results.append(True)
                else:
                    print("\n\t [+] Email was not sent successfully.")
                    results.append(False)
            except KeyboardInterrupt:
                print("\n\t [+] KeyboardInterrupt exception caught.")
                sys.exit()
            except:
                print("\n\t [+] Element does not exist.")
                results.append(False)

    # grabs total results
    total_results = results.count(True) +  results.count(False)
    print(f"\n\t [+] Number of successful tries: {results.count(True)} out of {total_results}")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear() # clear screen
    print("[+] Welcome to SeQure!\n") # starting prompt
    url = input("[+] Enter the URL you would like to check: ")
    print("------------------------------------------------------------------------------------------")
    reflectedCrossSite(url)