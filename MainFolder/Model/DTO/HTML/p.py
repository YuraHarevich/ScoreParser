from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule


class P4_arhemchik(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        for row in rows:
            print(row)
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
                None,
                None
            ))
        return None