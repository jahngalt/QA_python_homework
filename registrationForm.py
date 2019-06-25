from selenium import webdriver
import time

#fill the required fields
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_xpath("//input[@class = 'form-control first' and @required]")
first_name.send_keys("asfas")

last_name = browser.find_element_by_xpath("//input[@class = 'form-control second' and @required]")
last_name.send_keys("asfsa")

e_mail = browser.find_element_by_xpath("//input[@class = 'form-control third' and @required]")
e_mail.send_keys("blabla@mail.ru")

#click button
button = browser.find_element_by_css_selector("button.btn")
button.click()

#check that you can register
#wait to page load
time.sleep()

#find the element containing text
welcome_text_elt = browser.find_element_by_tag_name("h1")
#write to the variable welcome_text text from the element welcome_text_elt
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
