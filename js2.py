from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")


x =  browser.find_element_by_id("input_value").text

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

answer = browser.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))

robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
robots_rule = browser.find_element_by_css_selector("#robotsRule").click()

button = browser.find_element_by_css_selector("button.btn.btn-default").click()
