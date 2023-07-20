from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
import selenium
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def refreshPPU(actors):
    for actor in actors:
        actor["profit_per_cost_unit"] = "{:.3f}".format(actor["points_per_5_seconds"] / int(actor["cost"]))
    return actors


def refreshCosts(actors):
    for actor in actors:
        actor["cost"] = int(
            parseWhitoutComa(driver.find_element(By.CSS_SELECTOR, f"{actor['element_css_selector']} b")))
    refreshPPU(actors)
    return actors

def parseWhitoutComa(textToParse: WebElement) -> str:
    if "-" in textToParse.text:
        senzatrattini = textToParse.text.split("-")[1].strip()
        return "".join(senzatrattini.split(","))
    else:
        return "".join(textToParse.text.split(","))

gameActors = [
    {"id": "buyCursor", "cost": 15, "points_per_5_seconds": 1, "profit_per_cost_unit": 0.66666,
     "element_css_selector": "#buyCursor"},
    {"id": "buyGrandma", "cost": 100, "points_per_5_seconds": 10, "profit_per_cost_unit": 0.1,
     "element_css_selector": "#buyGrandma"},
    {"id": "buyFactory", "cost": 500, "points_per_5_seconds": 20, "profit_per_cost_unit": 0.04,
     "element_css_selector": "#buyFactory"},
    {"id": "buyMine", "cost": 2000, "points_per_5_seconds": 50, "profit_per_cost_unit": 0.025,
     "element_css_selector": "#buyMine"},
    {"id": "buyShipment", "cost": 7000, "points_per_5_seconds": 100, "profit_per_cost_unit": 0.01428,
     "element_css_selector": "#buyShipment"},
    {"id": "buyAlchemy lab", "cost": 50000, "points_per_5_seconds": 500, "profit_per_cost_unit": 0.01,
     "element_css_selector": "#buyAlchemy\\ lab"},
    {"id": "portal", "cost": 1000000, "points_per_5_seconds": 6666, "profit_per_cost_unit": 0,
     "element_css_selector": "#buyPortal"},
    # {"id": "buyTime machine", "cost": 123456789, "points_per_5_seconds": ????, "profit_per_cost_unit": 0,
    #  "element_css_selector": "#buyTime\\ machine"},
]

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

cookiePerSecond = driver.find_element(By.ID, "cps")

exitForInvestmentsButton = driver.find_element(By.ID, "updateLog")

cookiePerMinute = 0

timeAtStart = time.time()
timeUntilStart = time.time()
scoreUntilStart = 0
lastScore = 0

flag = True

while True:
    newScore = int(parseWhitoutComa(score))
    cookie.click()
    if time.time() > timeout and flag:
        scoreUntilStart += newScore - scoreUntilStart
        timeout = time.time() + 5
        cookiePerMinute = int((scoreUntilStart - lastScore) / (5 / 60))
        lastScore = scoreUntilStart
        cookiePerSecond = driver.find_element(By.ID, "cps")
        print(f"timeUntilStart:{timeUntilStart}  | scoreTotal:{scoreUntilStart}")
        try:
            refreshCosts(gameActors)
            statistics = []
            for actor in gameActors:
                statistics.append(str(actor["profit_per_cost_unit"]))
            print(" | ".join(statistics))
            print("")
            maxNumber = 0
            index = -1
            indexMax = 0
            for statistic in statistics:
                index +=1
                if float(statistic)> maxNumber:
                    maxNumber = float(statistic)
                    indexMax = index

            driver.find_element(By.CSS_SELECTOR, gameActors[indexMax]["element_css_selector"]).click()
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
    time.sleep(0.1)
