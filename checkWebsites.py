from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

statuses = []

# lindsaykjohnston.com
url = "https://www.lindsaykjohnston.com/"
driver.get(url)

try:
   wait = WebDriverWait(driver, timeout=3)
   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shmop-title")))
except TimeoutException as ex:
   print("TimeoutException has been thrown for lindsaykjohnston.com." )


heading = driver.find_element(by = By.CLASS_NAME, value="top-title")

if heading.text != "lindsay k. johnston":
   statuses.append(url + " : " + "ERROR")
else:
   statuses.append(url + " : " + "GOOD-TO-GO")

# micahclayluebben.us
url = "https://www.micahclay.us/"
driver.get(url)
mainImgAltTag = driver.find_element(by = By.CLASS_NAME, value="headerGraphic").get_attribute("alt")
if mainImgAltTag != "micah-clay-logo":
   statuses.append(url + " : " + "ERROR")
else:
   statuses.append(url + " : " + "GOOD-TO-GO")

# # GitHub User Map
# url = "https://api-map-upgraded-heroku-22.herokuapp.com/"
# driver.get(url)
# driver.find_element(by = By.ID, value="city-input").send_keys("Spokane")
# driver.find_element(by= By.ID, value="get-map").click()

# mapExplanation = driver.find_element(by = By.ID, value= "marker-explanation")

# wait = WebDriverWait(driver, timeout=10)
# wait.until(EC.visibility_of(mapExplanation))

# if mapExplanation.text != "Click a marker to see the number of GitHub users.":
#    statuses.append(url + " : " + "ERROR")
# else:
#    statuses.append(url + " : " + "GOOD-TO-GO")

print(statuses)

driver.quit()

