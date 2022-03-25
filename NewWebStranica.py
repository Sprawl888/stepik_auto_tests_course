import time
import math
from selenium import webdriver

link = " http://suninjuly.github.io/redirect_accept.html"
try:

        browser = webdriver.Chrome()
        browser.get(link)
        browser.maximize_window()
        # остановить бегающую строку
        # browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
        browser.find_element_by_css_selector("button.trollface.btn").click()

        # перейти по вкладке
        browser.switch_to.window(browser.window_handles[1])

        # поиск текста в элементе
        x = browser.find_element_by_id("input_value").text
         # функция просчета
        def calc(x):
                return math.log(abs(12*math.sin(int(x))))
        y=calc(x)
        print(y)
        # вывод строкой результата
        browser.find_element_by_name("text").send_keys(str(y))
        browser.find_element_by_class_name("btn-primary").click()
finally:

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()