from selenium import webdriver
import math


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
answer = browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox.form-check-input").click()
robots_rule = browser.find_element_by_css_selector("#robotsRule.form-check-input").click()

button = browser.find_element_by_css_selector("button.btn.btn-default").click()
