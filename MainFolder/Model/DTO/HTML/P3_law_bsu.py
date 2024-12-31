from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule


class P3_law_bsu(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        i = 0
        for row in rows:
            if i == 0:
                continue
            i+=1
            dto.append(DTO(
                "Юридический колледж БГУ",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                False,
                None
            ))
        return None