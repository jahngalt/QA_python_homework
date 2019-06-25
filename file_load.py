#Тест выполняет регистрацию в рег. форме и прикрепляет файл file.txt
import os
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

first_name = browser.find_element_by_name('firstname')
first_name.send_keys("asfas")

last_name = browser.find_element_by_name("lastname")
last_name.send_keys("asfsa")

e_mail = browser.find_element_by_name("email")
e_mail.send_keys("blabla@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')
load = browser.find_element_by_name("file").send_keys(file_path)

button = browser.find_element_by_class_name("btn-primary").click()
