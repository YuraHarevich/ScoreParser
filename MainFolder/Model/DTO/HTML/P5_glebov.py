import re

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM


class P5_glebov(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        i = 0
        for row in rows:
            if i < 2:
                i += 1
                continue
            else:
                pattern = r"([^\d\(]+).*?(\d+[-\d]+).*?Квалификация:\s*(.*)"

                match = re.match(pattern, row[0], re.DOTALL)

                dto.append(DTO(
                    match.group(1).strip(),
                    match.group(2).strip(),
                    row[5],
                    row[6],
                    None,
                    row[1],
                    row[2],
                    DAY_STUDY_FORM,
                    False,
                    row[3] + "/" + row[4],
                    match.group(3).strip()
                ))
        return dto

    # вступительных экзаменов (рисунок, живопись или скульптура, композиция) и среднего балла документа об образовании