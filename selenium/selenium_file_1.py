from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser.get(link)
button = browser.find_element(By.ID,"submit_button")
button.click()
browser.close()