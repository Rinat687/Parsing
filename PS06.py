import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

url = "https://ufa.hh.ru/vacancies/programmist"
driver.get(url)

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vacancy-card--n77Dj8TY8VIUF0yM")))

vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--n77Dj8TY8VIUF0yM")

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, '[data-qa="vacancy-title"]').text
        company = vacancy.find_element(By.CSS_SELECTOR, '[data-qa="vacancy-company-name"]').text

        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, '[data-qa="vacancy-salary"]').text
        except NoSuchElementException:
            salary = "Зарплата не указана"

        link = vacancy.find_element(By.CSS_SELECTOR, 'a[data-qa="vacancy-title-link"]').get_attribute('href')
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

# Запись данных в CSV
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)