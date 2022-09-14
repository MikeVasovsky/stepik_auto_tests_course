from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 150);")
    rez=browser.find_element(By.ID,"answer")
    rez.send_keys(y)
    check=browser.find_element(By.ID,'robotCheckbox').click()
    robot=browser.find_element(By.ID,'robotsRule').click()
    ok=browser.find_element(By.TAG_NAME,'button')
    ok.click()
finally:
   
    time.sleep(10)
   
    
