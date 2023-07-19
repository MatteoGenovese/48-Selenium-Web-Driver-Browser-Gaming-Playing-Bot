from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/home/matteo/Development/Drivers/chromedriver")
driver = webdriver.Chrome(service=service)

url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)
timeout = time.time() + 5

score = driver.find_element(By.ID, "money")
cookie = driver.find_element(By.ID, "cookie")

cursor = driver.find_element(By.ID, "buyCursor")
grandma = driver.find_element(By.ID, "buyGrandma")
factory = driver.find_element(By.ID, "buyFactory")
mine = driver.find_element(By.ID, "buyMine")
shipment = driver.find_element(By.ID, "buyShipment")
alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
time_machine = driver.find_element(By.ID, "buyTime machine")

gameActors = [
    {"id": "buyCursor", "initial_cost": 15, "points_per_5_seconds": 1, "profit_per_cost_unit": 0.66666},
    {"id": "buyGrandma", "initial_cost": 100, "points_per_5_seconds": 10, "profit_per_cost_unit": 0.1},
    {"id": "buyFactory", "initial_cost": 500, "points_per_5_seconds": 20, "profit_per_cost_unit": 0.04},
    {"id": "buyMine", "initial_cost": 2000, "points_per_5_seconds": 50, "profit_per_cost_unit": 0.025},
    {"id": "buyShipment", "initial_cost": 7000, "points_per_5_seconds": 100, "profit_per_cost_unit": 0.01428},
    {"id": "buyAlchemy lab", "initial_cost": 50000, "points_per_5_seconds": 500, "profit_per_cost_unit": 0.01},
    {"id": "portal", "initial_cost": 1000000, "points_per_5_seconds": "?", "profit_per_cost_unit": 0},
    {"id": "buyTime machine", "initial_cost": 123456789, "points_per_5_seconds": "?", "profit_per_cost_unit": 0},
]

cookiePerSecond = driver.find_element(By.ID, "cps")


# cursor 15, 1, 3
# grandma 100, 10, 11
# factory 500, 20, 101
# mine 2000, 50, 200
# shipment 7000, 100, 700
# alchemy lab 50000, 500, 5000
def refreshCosts():
    cursorCost = driver.find_element(By.CSS_SELECTOR, "buyCursor b")
    grandmaCost = driver.find_element(By.CSS_SELECTOR, "buyGrandma b")
    factoryCost = driver.find_element(By.CSS_SELECTOR, "buyFactory b")
    mineCost = driver.find_element(By.CSS_SELECTOR, "buyMine b")
    shipmentCost = driver.find_element(By.CSS_SELECTOR, "buyShipment b")
    alchemy_labCost = driver.find_element(By.CSS_SELECTOR, "buyAlchemy\\ lab b")
    portalCost = driver.find_element(By.CSS_SELECTOR, "buyPortal b")
    time_machineCost = driver.find_element(By.CSS_SELECTOR, "#buyTime\\ machine b")
    cookiePerSecondCost = driver.find_element(By.CSS_SELECTOR, "#cps b")


cookiePerMinute = 0

timeAtStart = time.time()
timeUntilStart = time.time()
scoreUntilStart = 0
lastScore = 0

flag = False

# print(cursorCost)
# print(grandmaCost)
# print(factoryCost)
# print(mineCost)
# print(shipmentCost)
# print(alchemy_labCost)
# print(portalCost)
# print(time_machineCost)
# print(cookiePerSecondCost)

while True:
    newScore = int("".join(score.text.split(",")))
    cookie.click()
    if time.time() > timeout:
        timeUntilStart += 5
        scoreUntilStart += newScore - scoreUntilStart
        timeout = time.time() + 5
        cookiePerMinute = int((scoreUntilStart - lastScore) / (5 / 60))
        lastScore = scoreUntilStart
        print(f"timeUntilStart:{timeUntilStart}  | scoreTotal:{scoreUntilStart} | cpm:{cookiePerMinute} | {flag}")
    if newScore > 500:
        flag = True

    time.sleep(0.1)
