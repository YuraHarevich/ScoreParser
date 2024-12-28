from MainFolder.Model.DTO.DTO import DTO
from MainFolder.functions import *
from MainFolder.Model.DTO.ParentDTOModule import ParentDTOModule
from MainFolder.config import *

class BSUIR(ParentDTOModule):
    def return_dto(self) -> DTO:
        str = get_html_content(BNTU_URL)
        print(str)
        return DTO("Yura")