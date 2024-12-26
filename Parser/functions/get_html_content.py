import requests
from bs4 import BeautifulSoup

# Укажите URL страницы
def get_html_content(url:str):
    try:
        # Отправка GET-запроса
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ (200)
        print(response)
        # Получение HTML-кода
        html_content = response.text

        # Если требуется обработка HTML-кода
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table")
        if table:
            return table
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")