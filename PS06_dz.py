import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Firefox()

# Открытие страницы
url = "https://www.divan.ru/category/svet"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(3)

# Поиск всех элементов товаров
svets = driver.find_elements(By.CLASS_NAME, "lsooF")

# Открытие файла для записи данных
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])

    # Обработка каждого товара
    for svet in svets:
        try:
            # Извлечение названия товара
            name = svet.find_element(By.CLASS_NAME, "ui-GPFV8").text.strip()  # Удаляем лишние пробелы
            # Извлечение текста с ценами
            price_text = svet.find_element(By.CLASS_NAME, "pY3d2").text.strip()  # Удаляем лишние пробелы
            # Разделение текста на строки и выбор первой цены
            price = price_text.split('\n')[0]  # Берем только первую цену
            # Извлечение ссылки
            url = svet.find_element(By.TAG_NAME, "a").get_attribute("href").strip()  # Удаляем лишние пробелы
            # Запись данных в файл
            writer.writerow([name, price, url])
        except Exception as e:
            print(f"Ошибка при обработке элемента: {e}")

# Закрытие браузера
driver.quit()