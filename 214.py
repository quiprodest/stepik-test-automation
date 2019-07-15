from selenium import webdriver
import time
import math


def calc(i):
    return str(math.log(abs(12 * math.sin(int(i)))))
	
	
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

# Считать значение для переменной x:
x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute('valuex')
# Посчитать математическую функцию от x:
y = calc(x)

# Ввести ответ в текстовое поле:
answer = browser.find_element_by_css_selector("#answer")
answer.send_keys(y)

# Отметить checkbox "Подтверждаю, что являюсь роботом":
checkb = browser.find_element_by_css_selector('#robotCheckbox')
checkb.click()

# Выбрать radiobutton "Роботы рулят!":
radiob = browser.find_element_by_css_selector('#robotsRule')
radiob.click()

# Нажать на кнопку Отправить:
button = browser.find_element_by_css_selector('button[type="submit"]')
button.click()

time.sleep(20)
browser.close()
browser.quit()
