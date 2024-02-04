# ----- Выбор товара в магазине и его оформление -----
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
# ----- инициализация библиотеки для Chrome -----
from selenium.webdriver.chrome.options import Options
# ----- Использование Jenkins в headless режиме (без графического интерфейса) -----
options = Options()
options.headless = True
browser = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

fake = Faker(["ru_RU"])  # Работаем с кириллицей
link = "https://pitergsm.ru/personal/profile/index.php"  # Ссылка для подключения к ресурсу
browser = webdriver.Chrome()  # Отключить при использовании в headless режиме
browser.maximize_window()  # Максимальный размер экрана
browser.get(link)  # Устанавливаем подключение к ресурсу
wait = WebDriverWait(browser, 10)
# ---------------------Рандомизатор полей--------------------------
randomName = fake.name_male()  # Рандомизируем поле name-Name
randomComment = fake.text()  # Рандомизируем поле сomment-Комментарий к заказу
def generate_phone_number(): # Рандомизируем поле phone-телефон (т.к. ограничение на сайте, номер с цифры 9)
    phone_number = "9"
    for _ in range(9):
        phone_number += str(fake.random_digit())
    return phone_number
# ---------------------Авторизация--------------------------
string_login = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body > div > div > form > div:nth-child(4) > div > input")
string_login.send_keys('and_3812')
string_pass = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body > div > div > form > div:nth-child(5) > div > input")
string_pass.send_keys('08and08')
submit = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body > div > div > form > input.btn.btn_green.btn_txt-big").click()
# ---------------------Поиск товара--------------------------
gorod1 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-line__side > div.sh-geo.sh-line__geo > div > a.sh-geo__city.js-show-popup").click()  # Выбор города по кнопке "Нет, выбрать другой"
gorod2 = browser.find_element(By.CSS_SELECTOR, "#pop-city > div > div > div.popup__content > ul > li:nth-child(10) > div").click()  # Выбрать в списке город "Омск"
time.sleep(3)
mag1 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(6) > a").click()  # Переход во вкладку "Смартфоны"
mag2 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > div.page-head__nav > ul > li:nth-child(5) > a").click()  # Выбор категории "Samsung"
mag3 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > div.page-head__nav > ul > li:nth-child(2) > a").click()  # Выбор категории "Galaxy S"
mag4 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > div.page-head__nav > ul > li:nth-child(4) > a").click()  # Переход во вкладку "Galaxy S23"
mag5 = browser.find_element(By.CSS_SELECTOR, "#catalog > div:nth-child(2) > div > a").click()  # Выбор товара "Смартфон Samsung Galaxy S23 8/128Gb, бежевый"
mag6 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body.product > div.product-head > div.product-info > div.product-info__unit.product-info__unit--params > div > form > div:nth-child(4) > ul > li:nth-child(3) > label > span").click()  # Изменить цвет товара на черный
mag7 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body.product > div.product-head > div.product-info > div.product-info__unit.product-info__unit--offers > div.product-price > div.product-price__buy > a.btn.btn_green.product-price__buy-btn.product-buy-trigger.detail-product-buy-trigger").click()  # Клик по кнопке "Купить"
time.sleep(3)
product = browser.find_element(By.LINK_TEXT, "В корзину").click()  # Переход в корзину по кнопке "В корзину"
time.sleep(3)
quantity = browser.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div/div[1]/div/div/div[3]/div/div/a[2]").click()  # Устанавливаем количество товара "Часы Samsung Galaxy Watch 5 Pro 45mm (SM-R920) (Серый титан)"
order = browser.find_element(By.CSS_SELECTOR, "#basket_form > div.tiles__slim > div > div > div.resume__final > button").click()  # Клик по кнопке "Оформить заказ"
time.sleep(3)
quantity = browser.find_element(By.CSS_SELECTOR, "#soa-property-1").clear() # Очистка значения по умолчанию в имени
# --------------Работа с рандомными данными--------------------
fieldName = browser.find_element(By.CSS_SELECTOR, "#soa-property-1")
fieldName.send_keys(randomName)
phone = generate_phone_number()
fieldPhone = browser.find_element(By.CSS_SELECTOR, "#soa-property-3")
fieldPhone.send_keys(phone)
textarea = browser.find_element(By.CSS_SELECTOR, "#bx-soa-order > div.col-sm-9.bx-soa.tiles__wide > div:nth-child(4) > div.form__line > textarea")
textarea.send_keys(randomComment)
# --------------Работа с рандомными данными (оформление доставки)------------------
dostavka1 = browser.find_element(By.CSS_SELECTOR, "#delivery-id-DELIVERY > div > div:nth-child(1) > div > div > label:nth-child(2) > span").click()  # Выбор доставки "... из пунктов самовывоза"
time.sleep(3)
dostavka2 = browser.find_element(By.CSS_SELECTOR, "#sdek_pickpoint_21 > div > a").click()  # Кликунуть по кнопке "Выбрать пункт самовывоза"
time.sleep(3)
dostavka3 = browser.find_element(By.CSS_SELECTOR, "#PVZ_OMS99").click()  # Выбор адреса для самовывоза
time.sleep(3)
dostavka4 = browser.find_element(By.CSS_SELECTOR, "#SDEK_button").click()  # Клик по кнопке "Выбрать"
time.sleep(5)
button = browser.find_element(By.CSS_SELECTOR, "#bx-soa-total-panel > div.bx-soa-cart-total.resume > div.bx-soa-cart-total-button-container.visible-xs > a").click()  # Переход на оформить заказ
time.sleep(7)
# Ответ "Заказ сформирован" с предложением оплатить