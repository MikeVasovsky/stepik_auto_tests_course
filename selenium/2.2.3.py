from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
link='http://suninjuly.github.io/selects1.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    x_find=browser.find_element(By.ID,'num1')
    x=x_find.text
    y_find=browser.find_element(By.ID,'num2')
    y=y_find.text
    x=int(x)
    y=int(y)
    c=x+y
    c=str(c)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)
    sub=browser.find_element(By.CSS_SELECTOR, "body>div button").click()
finally:
   
    time.sleep(10)
   
    browser.quit()    
   
