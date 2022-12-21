from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os


def reflectedCrossSite(url):
    results = []

    # name and message==================================================================================WRONG
    try:
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("Message trial #2")
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # name and message  =================================================================> WRONG
    try:
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
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # name and subject ============================================================================ RIGHT
    try:
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # subject and name ======================================================================================RIGHT (for some reason)
    try:
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
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # name and email =======================================================================================WRONG
    try:
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-name').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-email').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # email and name ===========================================================================================WRONG
    try:
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
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # message and subject ====================================================================================WRONG
    try:
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-message').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-subject').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # subject and message ================================================================================WRONG
    try:
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
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # subject and email ====================================================================================WRONG
    try:
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-subject').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-email').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # email and subject ========================================================================================== WRONG
    try:
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
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # email and message ===================================================================================== WRONG
    try:
        options = Options()
        options.headless = True
        s = Service("C:/Users/Lex Caldwell/Downloads/chromedriver")
        driver = webdriver.Chrome(service=s, options=options) # path to chromedriver
        driver.get(url)
        # This finds the element and passes in a script
        driver.find_element(By.NAME, 'your-email').send_keys("<script>alert('alert')</script>")
        driver.find_element(By.NAME, 'your-message').send_keys("Message trial #2")
        print("\n\t [+] HTML elements found:\n")
        # this finds the button
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        # this clicks the button
        driver.execute_script("arguments[0].click();", button)
        print("\n\t [+] Button was successfully pressed:\n")
        driver.quit() # closes the window
        results.append(True)
    except:
        print("\n\t [+] Element does not exist.")
        results.append(False)
    # message and email ================================================================================= WRONG
    try:
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
        driver.quit() # closes the window
        results.append(True)
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