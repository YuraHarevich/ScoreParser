import re

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM, CORRESPONDENCE_STUDY_FORM


class P24_bgufk(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        first_part = ""
        code = None
        second_part = ""
        for row in rows[5:]:
            if re.match("^\d+-\d+-\d+-\d+$",row[1]):
                code = row[1]
                first_part = row[0].replace("\n"," ")
                second_part = ""
                if row[0] == 'Тренерская деятельность ( с\nуказанием вида спорта)':
                    first_part = "Тренерская деятельность"
            else:
                second_part = row[0]
            if row[0] == 'Профилизации:':
                continue
            dto.append(DTO(
                first_part +" ("+ second_part+")",
                code,
                row[2],
                row[5],
                None,
                None,
                None,
                DAY_STUDY_FORM,
                False,
                None,
                None
            ))
        return dto