import requests

#  Отправляем GET-запрос к API с параметром userId=1
url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1  # Фильтрация по userId
}

try:
    response = requests.get(url, params=params)

    #  Распечатываем статус-код ответа
    print("Статус-код ответа:", response.status_code)

    #  Распечатываем полученные записи
    if response.status_code == 200:  # Проверяем, что запрос успешен
        posts = response.json()  # Преобразуем ответ в JSON
        print("Полученные записи:")
        for post in posts:
            print(f"ID: {post['id']}")
            print(f"Заголовок: {post['title']}")
            print(f"Текст: {post['body']}")
            print("-" * 40)  # Разделитель для удобства чтения
    else:
        print("Ошибка при выполнении запроса:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Ошибка при выполнении запроса:", e)