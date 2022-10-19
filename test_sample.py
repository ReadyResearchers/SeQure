from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def test_setup():
    global driver
    s = Service("C:/Users/alexi/Desktop/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.get("https://xss-game.appspot.com/level1/frame")
    
def test_login():
    driver.find_element(By.ID, 'query').send_keys("-prompt(8)-")
    button = driver.find_element(By.ID, "button")
    driver.implicitly_wait(10)
    driver.execute_script("arguments[0].click();", button)
    #sx = driver.find_element(By.CSS_SELECTOR, 'b')
    #assert x == "Sorry, no results were found for \"-prompt(8)-\". Try again."
    
def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed.")

