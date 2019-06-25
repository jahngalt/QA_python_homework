from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button = browser.find_element_by_id("book").click()
x = browser.find_element_by_id("input_value").text
field = browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
browser.find_element_by_id("solve").click()
