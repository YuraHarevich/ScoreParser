import re

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import *


class P8_bguki(ParentDTOModule):
    def return_dto(self,rows:list[list],url_number = None) -> list[DTO]:
        i:int = 0
        dto = list()
        faculty:str = ""
        for row in rows:
            if row[0] == "" and row[1] == "":
                break
            if re.match(r"^Факультет", row[1]):
                faculty = row[1]
            else:
                if i<3:
                    i+=1
                    continue
                if not(row[2]=="-" and row[7]=="-"):
                    is_shortened = False
                    name =  row[0]
                    if re.match(r".+-сокращенный срок", row[0]):
                        is_shortened = True
                        name = row[0].split("-")[0]
                    dto.append(DTO(
                        name,
                        None,
                        row[2],
                        row[7],
                        faculty,
                        None,
                        None,
                        DAY_STUDY_FORM,
                        is_shortened,
                        row[1]+"/"+row[6],
                        None
                    ))
                if not (row[4] == "-" and row[9] == "-"):
                    is_shortened = False
                    name = row[0]
                    if re.match(r".+–сокращенный срок", row[0]):
                        is_shortened = True
                        name = row[0].split("–")[0]
                    dto.append(DTO(
                        name,
                        None,
                        row[4],
                        row[9],
                        faculty,
                        None,
                        None,
                        CORRESPONDENCE_STUDY_FORM,
                        is_shortened,
                        row[3] + "/" + row[8],
                        None
                    ))
        return dto