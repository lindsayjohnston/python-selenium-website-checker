from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import ezgmail

driver = webdriver.Chrome()

statuses = {}

# lindsaykjohnston.com
url = "https://www.lindsaykjohnston.com/"
try:
   driver.get(url)
   statuses[url] = "GOOD TO GO"
except:
   statuses[url] = "ERROR - Site didn't load."

if "ERROR" not in statuses[url]: 
   try:
      wait = WebDriverWait(driver, timeout=3)
      wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".top-title")))
      statuses[url] = "GOOD-TO-GO"
   except TimeoutException as ex:
      statuses[url] = "ERROR - Title didn't load."
   

# micahclayluebben.us
url = "https://www.micahclay.us/"
try:
   driver.get(url)
   statuses[url] = "GOOD TO GO"
except:
   statuses[url] = "ERROR - Site didn't load."

if "ERROR" not in statuses[url]:
   try:
      wait = WebDriverWait(driver, timeout=3)
      wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".headerGraphic")))
      statuses[url] = "GOOD TO GO"
   except TimeoutException as ex:
      statuses[url] = "ERROR - .headerGraphic not found"


# GitHub User Map
url = "https://api-map-upgraded-heroku-22.herokuapp.com/"
try:
   driver.get(url)
   statuses[url] = "GOOD TO GO"
except:
   statuses[url] = "ERROR - Site didn't load."

if "ERROR" not in statuses[url]:
   try:
      wait = WebDriverWait(driver, timeout=3)
      wait.until(EC.presence_of_element_located((By.ID, "city-input")))
      wait.until(EC.presence_of_element_located((By.ID, "get-map")))
      wait.until(EC.presence_of_element_located((By.ID, "marker-explanation")))
      statuses[url] = "GOOD TO GO"
   except TimeoutException as ex:
      statuses[url] = "ERROR - some elements weren't found."

if "ERROR" not in statuses[url]:
   driver.find_element(by = By.ID, value="city-input").send_keys("Spokane")
   driver.find_element(by= By.ID, value="get-map").click()

   try:
      wait = WebDriverWait(driver, timeout=15)
      mapExplanation = driver.find_element(by = By.ID, value= "marker-explanation")
      wait.until(EC.visibility_of(mapExplanation))
      statuses[url] = "GOOD TO GO"
   except TimeoutException as ex:
      statuses[url] = "ERROR - #marker-explanation not visiblesome elements weren't found."


# Chipotle Clone
url = "https://main.d25r1kk5mc9ae9.amplifyapp.com/"

try:
   driver.get(url)
   statuses["Chipotle"] = "GOOD TO GO"
except:
   statuses["Chipotle"] = "ERROR - Site didn't load"

print(statuses)

statusesString = str(statuses)

if "ERROR" in statusesString:
   print("Sending email error alert")
   ezgmail.send('lkjohnston10@gmail.com', 'Subject line', str(statuses))

driver.quit()

