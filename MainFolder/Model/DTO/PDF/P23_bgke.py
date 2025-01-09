import re

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM, CORRESPONDENCE_STUDY_FORM


class P23_bgke(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        for row in rows[1:]:
            print(row)
        #     # dto.append(DTO(
        #     #     row[0].replace("\n", " "),
        #     #     None,
        #     #     None,
        #     #     row[5],
        #     #     None,
        #     #     None,
        #     #     None,
        #     #     study_form,
        #     #     is_shortened,
        #     #     None,
        #     #     None
        #     # ))
        return dto