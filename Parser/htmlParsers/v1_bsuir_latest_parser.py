import requests
from bs4 import BeautifulSoup
from Parser.functions.find_name_between_brakets import brakets
from Parser.functions.get_html_content import get_html_content
from Parser.functions.get_rows import get_rows
from Parser.models.Speciality import Speciality
# Константы


qualification = "бакалавр"
year=2024
plan_paid = -1
plan_budget = -1
passing_score_paid=None
passing_score_budget=None
study_duration=4
education_level="ВО"
exam_type="экзамен"
after_grade=11
note = ""


def parse_bsuir_latest(year:int) -> list:
    url = f"https://abitur.bsuir.by/prokhodnye-bally-{year}-goda"
    table = get_html_content(url)
    rows = get_rows(table)

    specialities = list()
    for row in rows[3:]:
        faculty = row[0]
        specialty_code = row[1][:12]
        name = brakets(row[1])
        # Объект для дневной формы
        if row[3] != '' or row[4] != '':
            passing_score_budget=None
            passing_score_paid = None
            if row[3] != '':
                passing_score_budget = row[3]
            if row[4] != '':
                passing_score_paid = row[4]

            specialities.append(Speciality(
                name, specialty_code, qualification, passing_score_paid, passing_score_budget, year,
                faculty, plan_paid, plan_budget, study_duration, education_level, "Дневная",
                exam_type, False, after_grade, note))
        # Объект для заочной полной формы
        if row[5] != '' or row[6] != '':
            passing_score_budget = None
            passing_score_paid = None
            if row[5] != '':
                passing_score_budget = row[5]
            if row[6] != '':
                passing_score_paid = row[6]

            specialities.append(Speciality(
                name, specialty_code, qualification, passing_score_paid, passing_score_budget, year,
                faculty, plan_paid, plan_budget, study_duration, education_level, "Заочная",
                exam_type, False, after_grade, note))
        # Объект для заочной сокращенной формы
        if row[7] != '' or row[8] != '':
            passing_score_budget = None
            passing_score_paid = None
            if row[7] != '':
                passing_score_budget = row[7]
            if row[8] != '':
                passing_score_paid = row[8]
            specialities.append(Speciality(
                name, specialty_code, qualification, passing_score_paid, passing_score_budget, year,
                faculty, plan_paid, plan_budget, study_duration, education_level, "Заочная",
                exam_type, True, after_grade, note))

    return specialities