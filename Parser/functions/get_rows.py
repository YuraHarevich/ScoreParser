from bs4 import BeautifulSoup

# Укажите URL страницы
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