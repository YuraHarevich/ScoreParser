from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM


class P20_mggyor(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        i:int = 0
        for row in rows:
            if i > 3 and not i == 12:
                dto.append(DTO(
                    row[0],
                    None,
                    None,
                    None,
                    None,
                    row[1],
                    None,
                    DAY_STUDY_FORM,
                    False,
                    None,
                    None
                ))
            i+=1
        return dto