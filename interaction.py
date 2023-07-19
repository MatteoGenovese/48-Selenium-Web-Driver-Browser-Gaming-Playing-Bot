from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/home/matteo/Development/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

driver.maximize_window()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()
