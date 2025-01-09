import pdfplumber

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import CORRESPONDENCE_STUDY_FORM, DAY_STUDY_FORM
from MainFolder.functions import extract_pdf

pdf_path = "../utils/test2.pdf"

class P21_bsu(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        dto = list()
        faculty = None
        # Обрабатываем таблицу
        for row in rows[1:]:
            if row[1] == None:
                continue
            if not row[0] is None:
                faculty = row[0].replace("\n", " ")
            if row[1] == "Название специальности":
                continue
            if row[1] == "объединенный конкурс:":
                continue
            if len(row) == 3:
                continue
            else:
                if row[2] == None:
                    row[2] = '"'
                dto.append(DTO(
                    row[1].replace("\n", " "),
                    None,
                    row[2].replace("\n", " ") if not row[2] == '"' else None,
                    row[3].replace("\n", " ") if not row[3] == '"'  else None,
                    faculty,
                    None,
                    None,
                    DAY_STUDY_FORM if url_number == 1 else CORRESPONDENCE_STUDY_FORM,
                    False,
                    None,
                    None
                ))

        return dto

# объединенный курс