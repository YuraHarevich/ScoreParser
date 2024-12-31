import json

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.DTO.HTML.P1_bsuir import P1_bsuir
from MainFolder.Model.DTO.HTML.P2_mgke import P2_mgke
from MainFolder.Model.DTO.HTML.P3_law_bsu import P3_law_bsu
from MainFolder.Model.DTO.HTML.P4_arhemchik import P4_arhemchik
from MainFolder.Model.DTO.HTML.P5_glebov import P5_glebov
from MainFolder.Model.DTO.HTML.P8_bguki import P8_bguki
from MainFolder.Model.DTO.HTML.P9_bntu import P9_bntu
from MainFolder.Model.edu.SpecializedSecondaryEducation import SpecializedSecondaryEducation
from MainFolder.Other.Encoder import EducationalInstitutionEncoder
from MainFolder.Model.edu.HigherEducationInstitution import HigherEducationInstitution
from MainFolder.Model.edu.ProfessionalTechnicalEducation import ProfessionalTechnicalEducation
from MainFolder.Model.Speciality import Speciality
from MainFolder.functions import get_html_content, get_rows, bntu_request
from MainFolder.config import *

# str = get_html_content(BNTU_URL_2)
# rows = get_rows(str)
#
# parser = P9_bntu()


#h = HigherEducationInstitution(BSUIR_URL)
#h = SpecializedSecondaryEducation(MGKE_NAME) вторая таблица
#h = SpecializedSecondaryEducation(GKI_ARHEMCHIK_NAME)
#h = SpecializedSecondaryEducation(MGHK_GLEBOV_NAME)
#h = HigherEducationInstitution(BGUKI_NAME)
#h = HigherEducationInstitution(BNTU_NAME)



h = bntu_request()
print(json.dumps(h, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False))

with open('../utils/output.json', 'w', encoding='utf-8') as f:
    # Сохраняем результат в файл с использованием json.dumps
    json.dump(h, f, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False)


