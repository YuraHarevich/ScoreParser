from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import DAY_STUDY_FORM


class P2_mgke(ParentDTOModule):
    def return_dto(self, rows: list[list]) -> list[DTO]:
        dto= list()
        for row in rows:
            if row[0] == 'Специальность и квалификация' or row[0] == 'Поступление в МГКЭ на основе общего базового образования (9 классов)' or row[0] == 'Поступление в колледж электроники в Минске на основе специального образования':
                continue
            else:
                score1 = row[2].split("/")[0]
                score2 = row[2].split("/")[1]
                dto.append(DTO(
                    row[0],
                    None,
                    score1 if score1 != 'нет набора' else None,
                    score2 if score2 != 'нет набора' else None,
                    None,
                    None,
                    None,
                    DAY_STUDY_FORM,
                    False,
                    None
                ))

        return dto