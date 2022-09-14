from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link='http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    step1=browser.find_element_by_css_selector('form button').click()
   
    confirm = browser.switch_to.alert   
    confirm.accept()
    x=browser.find_element_by_id('input_value').text
    #x=int(x) наврядли дело в этом
    y=calc(x)
    b=browser.find_element_by_id('answer')
    b.click
    b.send_keys(y)
    step=browser.find_element_by_class_name('btn').click()
finally:
   
    time.sleep(10)
   
