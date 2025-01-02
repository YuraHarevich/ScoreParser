import re

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM


class P13_visotsky(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        for row in rows:
            match = re.match(r"^([\d\-]+)([^\d]+)\d+.*$", row[0])
            if match:
                dto.append(DTO(
                    match.group(2).strip(),
                    match.group(1).strip(),
                    None,
                    None,
                    None,
                    row[5],
                    None,
                    DAY_STUDY_FORM,
                    False,
                    None,
                    row[1]
                ))
            if row[0] == 'на платной основе':
                dto[-1].plan_paid = row[3]
        return dto