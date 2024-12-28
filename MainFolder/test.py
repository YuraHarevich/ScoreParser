import json

from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Other.Encoder import EducationalInstitutionEncoder
from MainFolder.Model.edu.HigherEducationInstitution import HigherEducationInstitution
from MainFolder.Model.edu.ProfessionalTechnicalEducation import ProfessionalTechnicalEducation
from MainFolder.Model.Speciality import Speciality
from MainFolder.functions import get_html_content
from MainFolder.config import *
from Parser.functions.get_rows import get_rows

# #едино для универа
# h = HigherEducationInstitution("БГУ")
# p = ProfessionalTechnicalEducation("ПТУ")
# #
# dto = DTO(
#     "Software Engineering",
# "SE123",
#     85,
#     75,
#     "ФИТУ",
#     34,
#     20,
#     "Дневная",
#     True,
#     1.2
# )
# sp = Speciality()
# #вручную для спецухи
# h.add_speciality(sp,dto)
# p.add_speciality(sp,dto)
# print(json.dumps(p, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False))
# print(json.dumps(h, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False))

str = get_html_content(BSUIR_URL)
str1 = get_rows(str)
for row in str1:
    print(row)
