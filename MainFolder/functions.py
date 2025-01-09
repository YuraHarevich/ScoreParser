import re

import pdfplumber
import requests
from bs4 import BeautifulSoup

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.HTML.P9_bntu import P9_bntu
from MainFolder.Model.Speciality import Speciality
from MainFolder.Model.edu.HigherEducationInstitution import HigherEducationInstitution
from MainFolder.config import *
import fitz


def find_beetween_brakets(target_string: str):
    second_part_start = target_string.find('«') + 1
    second_part_end = target_string.find('»')
    return target_string[second_part_start:second_part_end]


def get_html_content(url: str,table_number=0):
    #Добавление заголовка для того, чтобы сервера не отклоняли запросы выглядящие как автоматические
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        response.encoding = 'utf-8'
        print(response)
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")
        tables = soup.find_all("table")

        return tables[table_number] if tables[table_number] else None

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

def bntu_request()->HigherEducationInstitution:
    h = HigherEducationInstitution(BNTU_NAME)
    str1 = get_html_content(BNTU_URL_1)
    rows1 = get_rows(str1)
    str2 = get_html_content(BNTU_URL_2)
    rows2 = get_rows(str2)
    str3 = get_html_content(BNTU_URL_3)
    rows3 = get_rows(str3)
    str4 = get_html_content(BNTU_URL_4)
    rows4 = get_rows(str4)
    str5 = get_html_content(BNTU_URL_5)
    rows5 = get_rows(str5)
    str6 = get_html_content(BNTU_URL_6)
    rows6 = get_rows(str6)

    parser = P9_bntu()
    first = parser.return_dto(rows1, 1)[:2]
    second = parser.return_dto(rows3, 3)[6:12]


    for dto in parser.merge_lists(parser.return_dto(rows1, 1),parser.return_dto(rows3, 3)):
        h.add_speciality(Speciality(), dto)
    print("Ну хоть что-то")
    for dto in parser.merge_lists(parser.return_dto(rows2, 2),parser.return_dto(rows4, 4)):
        h.add_speciality(Speciality(), dto)
    for dto in parser.return_dto(rows5, 5):
        h.add_speciality(Speciality(), dto)
    for dto in parser.return_dto(rows6, 6):
        h.add_speciality(Speciality(), dto)
    return h

# Функция для исправления разрывов между словами (например, "Менеджме нт" на "Менеджмент")
def fix_word_breaks(line):
    # Исправляем разрывы между частями слова (например, "Менеджме нт" на "Менеджмент")
    fixed_line = re.sub(r'([а-яА-Я]+)\s+(й|ий|ес)\b', r'\1\2', line)

    # Убираем лишние пробелы
    fixed_line = re.sub(r'\s+', ' ', fixed_line).strip()

    return fixed_line

def extract_pdf(pdf_path) -> list[list]:
    with pdfplumber.open(pdf_path) as pdf:
        all_data = []
        table = list()
        for page in pdf.pages:
            # Извлекаем таблицу с текущей страницы
            for element in page.extract_table():
                table.append(element)
        return table

def extract_pdf_with_fitz(pdf_path) -> list[list]:
    all_data = []
    doc = fitz.open(pdf_path)

    for page in doc:
        # Извлекаем текст строки с координатами
        blocks = page.get_text("blocks")
        for block in blocks:
            lines = block[4].split("\n")  # Разделение на строки
            all_data.extend([line.split() for line in lines])  # Разделяем строки на ячейки
    return all_data