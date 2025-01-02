import re
import time

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import CORRESPONDENCE_STUDY_FORM
from MainFolder.config import DAY_STUDY_FORM



class P9_bntu(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        study_form = None
        is_shortened = False
        budg_paid = None
        contest = None
        if url_number == 1:
            study_form = DAY_STUDY_FORM
            budg_paid = "paid"
        if url_number == 2:
            study_form = CORRESPONDENCE_STUDY_FORM
            budg_paid = "paid"
        if url_number == 3:
            study_form = DAY_STUDY_FORM
            budg_paid = "budget"
        if url_number == 4:
            study_form = CORRESPONDENCE_STUDY_FORM
            budg_paid = "budget"
        if url_number == 5:
            study_form = DAY_STUDY_FORM
            budg_paid = "budget"
        if url_number == 6:
            study_form = CORRESPONDENCE_STUDY_FORM
            budg_paid = "budget"
            is_shortened=True
        i: int = 0
        dto = list()
        faculty: str = ""
        for row in rows:
            if re.match(r".*факультет.*", row[0]) or re.match(r"Факультет.*", row[0]):
                faculty = row[0]
                match = re.search(r"\((.*?)\)", row[0])
                if match:
                    faculty = row[0].split("(")[0][:-1]#вконце убирай пробел между скобкой и названием факультета
                    if match.group(1) == "сокращенный срок":
                        is_shortened = True
                    else:
                        is_shortened = False
            else:
                if i < 2:
                    i += 1
                    continue
                if len(row) == 1:
                    continue
                else:
                    # если ячеек на одну меньше, значит верхний балл конкурса дублируется
                    if len(row) == 5:
                        contest = row[3]
                    if row[2] == 0:
                        continue
                    dto.append(DTO(
                        row[1],
                        row[0],
                        row[len(row)-1] if budg_paid=="budget" else None,
                        row[len(row)-1] if budg_paid=="paid" else None,
                        faculty,
                        row[2] if budg_paid=="budget" else None,
                        row[2] if budg_paid=="paid" else None,
                        study_form,
                        is_shortened,
                        contest,
                        None
                    ))

        return dto

    #Сделать чет с филиалом в солигорске
    #Международный институт дистанционного образования (полный срок) и Международный институт дистанционного образования (сокращенный срок) или мб вообще нахуй не нужно
    #Добавляются записи из него под другим факультетом их надо удалить

    def merge_lists(self,
                   paid_list:list[DTO],
                   budget_list:list[DTO]) -> list[DTO]:
        result_list = list()
        is_added = False
        temp = paid_list[0]
        for paid_element in paid_list:
            for budget_element in budget_list:
                if paid_element.name.replace(" ","") == budget_element.name.replace(" ","") and \
                        paid_element.specialty_code == budget_element.specialty_code and \
                        paid_element.faculty == budget_element.faculty and \
                        paid_element.study_form == budget_element.study_form and \
                        paid_element.is_shortened == budget_element.is_shortened:
                    result_element = budget_element
                    result_element.plan_paid = paid_element.plan_paid
                    result_element.passing_score_paid = paid_element.passing_score_paid
                    if budget_element.contest == None:
                        budget_element.contest=" "
                    if paid_element.contest == None:
                        paid_element.contest=" "
                    result_element.contest = budget_element.contest + "/" + paid_element.contest
                    result_list.append(result_element)
                    break
                elif budget_list[-1] == budget_element:
                    result_list.append(paid_element)

        for budget_element in budget_list:
            # Проверяем, есть ли элемент с таким же именем в result_list
            if not any(result_element.name.replace(" ","") == budget_element.name.replace(" ","") for result_element in result_list):
                result_list.append(budget_element)  # Добавляем, если имени нет в result_list
        return result_list