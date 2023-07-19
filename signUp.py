from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/home/matteo/Development/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)

url = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url)

data = {
    "first_name": "Matteo",
    "last_name": "Genovese",
    "my_email": "mgeno@icloud.com"
}

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email_box = driver.find_element(By.NAME, "email")

first_name.send_keys(data["first_name"])
last_name.send_keys(data["last_name"])
email_box.send_keys(data["my_email"])

sign_up_bottom = driver.find_element(By.TAG_NAME, "Button")
sign_up_bottom.click()

driver.quit()
