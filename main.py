from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

optionsChrome = webdriver.ChromeOptions()
optionsChrome.add_experimental_option("excludeSwitches", ["enable-automation"])
optionsChrome.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=optionsChrome)
driver.get("https://relax-family.vercel.app/")
driver.fullscreen_window()

username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys('poomrelax')
time.sleep(1)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('poomrelax11699')
submit = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div/div[2]/button')
submit.click()



#homework.click()