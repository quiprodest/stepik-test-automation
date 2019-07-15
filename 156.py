from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# См. в комментах к этой задаче ответ преподавателя от 08.07.2019: 
# "здесь проверяем, что можно зарегистрироваться, используя поля имя-фамилия-почта. 
# Проверять обязательность не обязательно :D главное чтобы это были именно те самые поля."
element1 = browser.find_element_by_css_selector('input[placeholder="Введите имя"]')
element1.send_keys("!")

element2 = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]')
element2.send_keys("!")

element3 = browser.find_element_by_css_selector('input[placeholder="Введите Email"]')
element3.send_keys("!")

# Отправляем заполненную форму:
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# Ждем загрузки страницы:
time.sleep(1)

# Находим элемент, содержащий текст:
welcome_text_elt = browser.find_element_by_tag_name("h1")
# Записываем в переменную welcome_text текст из элемента welcome_text_elt:
welcome_text = welcome_text_elt.text

# С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта:
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
