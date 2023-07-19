from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"  # Percorso di installazione di Brave
# options.add_argument("--headless")  # Esegui in modalità headless (senza interfaccia grafica)
options.add_argument("--no-sandbox")  # Imposta l'opzione --no-sandbox per evitare errori di sandboxing

chrome_driver_path = Service("/home/matteo/Development/Drivers/chromedriver")

driver = webdriver.Chrome(service=chrome_driver_path, options=options)
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time
url = "https://www.python.org/"
driver.get(url)

dates_list = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li time")
dates = []
events_list = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = []
links = []

for event in events_list:
    events.append(event.text)
    links.append(str(event.get_attribute("href")))

# month_and_day = driver.find_element(by=By.CSS_SELECTOR, value=".event-widget div ul li time")
for date in dates_list:
    dates.append(str(date.get_attribute("datetime")).split("T")[0])

event_dict = {}
for n in range(len(events_list) - 1):
    event_dict[n] = {
        "time": dates[n],
        "event_name": events[n],
        "link": links[n]
    }

print(event_dict)

driver.quit()
