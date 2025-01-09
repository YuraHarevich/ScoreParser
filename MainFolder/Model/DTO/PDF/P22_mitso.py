import re

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM, CORRESPONDENCE_STUDY_FORM


class P22_mitso(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        study_form = DAY_STUDY_FORM
        is_shortened = False
        counter = 0
        for row in rows[1:]:
            if row[1] is not None:
                if re.match(r"^Форма обучения.*", row[1]):
                    if counter == 1:
                        study_form = CORRESPONDENCE_STUDY_FORM
                    if counter == 2:
                        is_shortened = True
                counter+=1
            if row[2] is not None:
                if re.match(r"^Форма обучения.*", row[2]):
                    if counter == 1:
                        study_form = CORRESPONDENCE_STUDY_FORM
                    if counter == 2:
                        is_shortened = True
                counter+=1
            if row[3] is not None:
                if re.match(r"^Форма обучения.*", row[3]):
                    if counter == 1:
                        study_form = CORRESPONDENCE_STUDY_FORM
                    if counter == 2:
                        is_shortened = True
                counter+=1
            else:
                dto.append(DTO(
                    row[0].replace("\n", " "),
                    None,
                    None,
                    row[5],
                    None,
                    None,
                    None,
                    study_form,
                    is_shortened,
                    None,
                    None
                ))
        return dto