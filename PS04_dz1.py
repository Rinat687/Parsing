from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера (например, для Firefox)
driver = webdriver.Firefox()

def search_wikipedia(query):
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Даем странице время для загрузки

def scroll_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input("Нажмите Enter для продолжения...")

def show_related_links():
    try:
        links = driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output p a[href^='/wiki/']")
        if not links:
            print("Связанные ссылки не найдены.")
            return

        for i, link in enumerate(links):
            print(f"{i + 1}. {link.text}")

        choice = int(input("Выберите номер ссылки для перехода: ")) - 1
        if 0 <= choice < len(links):
            links[choice].click()
            time.sleep(2)  # Даем странице время для загрузки
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    try:
        query = input("Введите ваш запрос для поиска в Википедии: ")
        search_wikipedia(query)

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Ваш выбор: ")

            if choice == '1':
                scroll_paragraphs()
            elif choice == '2':
                show_related_links()
            elif choice == '3':
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()