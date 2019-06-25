#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver


link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)



firstname = browser.find_element_by_name("first_name")
firstname.send_keys("Vasya")

lastname = browser.find_element_by_name("last_name")
lastname.send_keys("Pupkin")

city = browser.find_element_by_class_name("form-control.city")
city.send_keys("New York")

country = browser.find_element_by_id("country")
country.send_keys("USA")

clickbutton = browser.find_element_by_xpath('//button[contains(text(), "Отправить")]')
clickbutton.click()
