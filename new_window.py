from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
first_window = browser.window_handles[0]

browser.find_element_by_class_name("btn-primary").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x =  browser.find_element_by_id("input_value").text
answer = browser.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))

button = browser.find_element_by_class_name("btn-primary").click()
