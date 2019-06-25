from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

sum  = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

select = Select(browser.find_element_by_class_name("custom-select"))
select.select_by_value(str(sum))

button_file = browser.find_element_by_class_name("btn-default").click()

button = browser.find_element_by_class_name("btn-default").click()
