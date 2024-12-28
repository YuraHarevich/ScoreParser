import requests
from bs4 import BeautifulSoup


def find_beetween_brakets(target_string: str):
    second_part_start = target_string.find('«') + 1
    second_part_end = target_string.find('»')
    return target_string[second_part_start:second_part_end]


def get_html_content(url:str):
    try:
        response = requests.get(url,verify=False)
        response.raise_for_status()
        print(response)
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table")
        if table:
            return table
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")


def get_rows(table):
    if table:
        rows = []
        # Поиск всех строк таблицы
        for tr in table.find_all("tr"):
            # Извлечение всех ячеек из строки (как <td>, так и <th>)
            cells = tr.find_all(["td", "th"])
            # Получение текста из ячеек
            row = [cell.get_text(strip=True) for cell in cells]
            rows.append(row)
        return rows
    else:
        return None