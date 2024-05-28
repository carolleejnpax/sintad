from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.example.com")
element = driver.find_element(By.ID, "some_id")
