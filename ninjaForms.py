from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import sys
import time
import os



def reflectedCrossSite(url):
    results = []

    # name and message  ==============================================================================
    try:
        print("\n\t [+] Test #1")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-message').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
        print("\n\t [+] HTML elements found:\n")
        print(checkAlert.getText())
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
    # subject and name ======================================================================================
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #2")
        options = Options()
        options.headless = True 
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-subject').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-name').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
        print("\n\t [+] HTML elements found:\n")
        print(checkAlert)
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
    # email and name ===========================================================================================
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #3")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-email').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-name').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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
    # subject and message ================================================================================
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #4")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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
    # email and subject ==========================================================================================
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #5")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-email').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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
    # message and email =================================================================================
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #6")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-email').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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

    # three input levels ****************************************************************************************************************************************

    # name and subject and email ============================================================================ 
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #7")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        driver.find_element(By.NAME, "email-430").send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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
    
    # message and subject and email ============================================================================ 
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #8")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        driver.find_element(By.NAME, "email-430").send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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

    # message and name and email ============================================================================ 
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #9")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-name').send_keys("Message trial #2")
        driver.find_element(By.NAME, "email-430").send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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

    # message and subject and name ============================================================================ 
    try:
        print("------------------------------------------------------------------------------------------")
        print("\n\t [+] Test #10")
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        driver.find_element(By.NAME, "name").send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.implicitly_wait(15)
        # by class name
        checkAlert = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
        mailSentOK = "Thank you for your message. It has been sent."
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