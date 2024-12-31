from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM


class P4_arhemchik(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        i = 0
        for row in rows:
            if i == 0:
                i += 1
                continue
            dto.append(DTO(
                row[0][12:],
                row[0][:12],
                None,
                None,
                None,
                row[2],
                None,
                DAY_STUDY_FORM,
                False,
                None,
                row[1]
            ))
        return dto

#    (Вступительные испытания есть в таблице и проходных баллов нету)