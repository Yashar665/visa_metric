import selenium
import requests
import time
import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

# driver_path = ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
# driver = webdriver.Chrome(driver_path)
# driver.close()

while True:
    driver_path = ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
    driver = webdriver.Chrome(driver_path)
    driver.get("https://appointment.visametric.com/")
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[1]/select")
    elem.send_keys("Azerbaijan")
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[2]/select")
    elem.send_keys("Germany")
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/button")
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[1]/select")
    elem.send_keys("Schengen Visa (for stay up to 90 days)")
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[2]/div[1]/select")
    elem.send_keys("Normal")
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[3]/select")
    elem.send_keys("Baku")
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[4]/select")
    elem.send_keys("Individual")
    time.sleep(2)
    elem = driver.find_element(By.CLASS_NAME, "list-group")
    elem_text = elem.text
    text_char = [m.start() for m in re.finditer('\n', elem_text)]
    date = elem_text[0:text_char[-1]]
    message = 'Earliest date available: ' + date
    driver.close()
    requests.get("https://api.telegram.org/bot5482974644:AAGih1XSlgkKiyeHG-4iP357wFMVTvw_vQ8/sendMessage?chat_id=-681523419&text=" + message)
#     time.sleep(3600)
