from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")


x =  browser.find_element_by_id("treasure").get_attribute("valuex")


answer = browser.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))

robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
robots_rule = browser.find_element_by_css_selector("#robotsRule").click()

button = browser.find_element_by_css_selector("button.btn.btn-default").click()
