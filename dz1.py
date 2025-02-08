import requests


#  Отправляем GET-запрос к API GitHub для поиска репозиториев с кодом html
url = "https://api.github.com/search/repositories"
params = {
    "q": "html",  # Параметр для поиска репозиториев с упоминанием "html"
    "sort": "stars",  # Сортировка по количеству звезд
    "order": "desc"  # В порядке убывания
}

response = requests.get(url, params=params)

#  Распечатываем статус-код ответа
print("Статус-код ответа:", response.status_code)

#  Распечатываем содержимое ответа в формате JSON
if response.status_code == 200:  # Проверяем, что запрос успешен
    data = response.json()  # Преобразуем ответ в JSON
    print("Содержимое ответа (JSON):")
    print(data)
else:
    print("Ошибка при выполнении запроса:", response.status_code)