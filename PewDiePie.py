import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com")
search = driver.find_element_by_name("search_query")
search.send_keys("PewDiePie")
search.send_keys(Keys.RETURN)
# This was made to click on the video, and wait for it to load in the specified time inside the brackets. If it doesmt load then quit the program/
# This part works since his channel is the first one in the search query
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "channel-title"))
    )
    element.click()
except:
    driver.quit()
