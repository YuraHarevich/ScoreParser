from Parser.models.Speciality import SpecialityEncoder
from Parser.htmlParsers.v1_bsuir_latest_parser import parse_bsuir_latest
import json

#############Bsuir - 2024-2023
specialities2024 = parse_bsuir_latest(2024)
specialities2023 = parse_bsuir_latest(2023)
json_data = json.dumps(specialities2024, cls=SpecialityEncoder, indent=4, ensure_ascii=False)
print(json_data)
# qualification = "бакалавр"
# year=2024
# plan_paid = -1
# plan_budget = -1
# passing_score_paid=None
# passing_score_budget=None
# study_duration=4
# education_level="ВО"
# exam_type="экзамен"
# after_grade=11
# note = ""
#
# pdf_path = "../utils/test.pdf"
# import pdfplumber
# import pandas as pd
# import re
#
#
# def extract_specialities_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         all_data = []
#
#         # Проходим по каждой странице PDF
#         for page in pdf.pages:
#             # Извлекаем таблицу с текущей страницы
#             table = page.extract_table()
#
#             if table:
#                 # Обрабатываем таблицу
#                 for row in table[1:]:  # Пропускаем первую строку, так как это заголовки
#                     # Пример того, как извлекаются данные: код специальности, наименование и баллы
#                     if len(row) >= 3:
#                         # Извлекаем нужные элементы
#                         code = row[1]  # Код специальности
#                         name = row[2]  # Наименование специальности
#                         scores = row[3:]  # Баллы (могут быть в нескольких колонках)
#
#                         # Преобразуем баллы в формат строки, проверяем на None
#                         scores = ' '.join([score for score in scores if score and score.strip().isdigit()])
#                         if code == None:
#                             continue
#                         # Объединяем код, название и баллы
#                         all_data.append(f"{code} {name} {scores}")
#
#         return all_data
#
#
# def format_specialities(pdf_path):
#     # Извлекаем данные из PDF
#     specialities = extract_specialities_from_pdf(pdf_path)
#
#     # Дополнительное исправление форматирования (например, исправление разрывов между словами)
#     formatted_specialities = [fix_word_breaks(line) for line in specialities]
#
#     return formatted_specialities
#
#
# # Функция для исправления разрывов между словами (например, "Менеджме нт" на "Менеджмент")
# def fix_word_breaks(line):
#     # Исправляем разрывы между частями слова (например, "Менеджме нт" на "Менеджмент")
#     fixed_line = re.sub(r'([а-яА-Я]+)\s+(й|ий|ес)\b', r'\1\2', line)
#
#     # Убираем лишние пробелы
#     fixed_line = re.sub(r'\s+', ' ', fixed_line).strip()
#
#     return fixed_line
#
#
# # Извлекаем и форматируем данные
# specialities = format_specialities(pdf_path)
#
# # Печатаем результат
# for speciality in specialities:
#     print(speciality)
