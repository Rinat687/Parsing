import requests



#  Создаем словарь с данными для отправки
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

#  Отправляем POST-запрос к API
url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.post(url, json=data)

    #  Распечатываем статус-код ответа
    print("Статус-код ответа:", response.status_code)

    #  Распечатываем содержимое ответа
    if response.status_code == 201:  # 201 означает, что запрос успешен и данные созданы
        print("Содержимое ответа (JSON):")
        print(response.json())
    else:
        print("Ошибка при выполнении запроса:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Ошибка при выполнении запроса:", e)