from MainFolder.Model.DTO.DTO import DTO
from MainFolder.functions import *
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import *



class P1_bsuir(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        for row in rows[3:]:
            faculty = row[0]
            specialty_code = row[1][:12]
            name = find_beetween_brakets(row[1])
            # Объект для дневной формы
            if row[3] != '' or row[4] != '':
                passing_score_budget = None
                passing_score_paid = None
                if row[3] != '':
                    passing_score_budget = row[3]
                if row[4] != '':
                    passing_score_paid = row[4]
                dto.append(DTO(
                    name,
                    specialty_code,
                    passing_score_budget,
                    passing_score_paid,
                    faculty,
                    None,
                    None,
                    DAY_STUDY_FORM,
                    False,
                    None
                ))
            # Объект для заочной полной формы
            if row[5] != '' or row[6] != '':
                passing_score_budget = None
                passing_score_paid = None
                if row[5] != '':
                    passing_score_budget = row[5]
                if row[6] != '':
                    passing_score_paid = row[6]

                dto.append(DTO(
                    name,
                    specialty_code,
                    passing_score_budget,
                    passing_score_paid,
                    faculty,
                    None,
                    None,
                    CORRESPONDENCE_STUDY_FORM,
                    False,
                ))
            # Объект для заочной сокращенной формы
            if row[7] != '' or row[8] != '':
                passing_score_budget = None
                passing_score_paid = None
                if row[7] != '':
                    passing_score_budget = row[7]
                if row[8] != '':
                    passing_score_paid = row[8]
                dto.append(DTO(
                    name,
                    specialty_code,
                    passing_score_budget,
                    passing_score_paid,
                    faculty,
                    None,
                    None,
                    CORRESPONDENCE_STUDY_FORM,
                    True,
                    None
                ))
        return dto