import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Инициализация переводчика
translator = Translator()

# Функция для получения информации о случайном слове
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Возвращаем словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    # Обработка ошибок
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Функция для перевода текста на русский язык
def translate_to_russian(text):
    try:
        translated = translator.translate(text, src='en', dest='ru')
        return translated.text
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text

# Функция для игры
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Получаем слово и его определение
        word_dict = get_english_words()
        if word_dict is None:
            continue

        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский
        translated_word = translate_to_russian(english_word)
        translated_definition = translate_to_russian(word_definition)

        # Начинаем игру
        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")
        if user.lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Запрос на повтор игры
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

# Запуск игры
word_game()