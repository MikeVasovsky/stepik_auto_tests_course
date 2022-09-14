from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    pict=browser.find_element(By.ID, "treasure")
    pict1=pict.get_attribute("valuex")
    #x_element = browser.find_element(By.ID, "input_value")
    #x = x_element.text
    y = calc(pict1)
    rez=browser.find_element(By.ID,"answer")
    rez.send_keys(y)
    im_not=browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    im_not.click()
    robot=browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot.click()
    sub=browser.find_element(By.CSS_SELECTOR, "body>div div button")
    sub.click()
    
finally:
   
    time.sleep(10)
   
    browser.quit()    
