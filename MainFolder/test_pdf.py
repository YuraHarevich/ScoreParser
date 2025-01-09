import json

from MainFolder.Model.DTO.PDF.P21_bsu import P21_bsu
from MainFolder.Model.DTO.PDF.P22_mitso import P22_mitso
from MainFolder.Model.DTO.PDF.P23_bgke import P23_bgke
from MainFolder.Model.DTO.PDF.P24_bgufk import P24_bgufk
from MainFolder.Model.Speciality import Speciality
from MainFolder.Model.edu.HigherEducationInstitution import HigherEducationInstitution
from MainFolder.Model.edu.SpecializedSecondaryEducation import SpecializedSecondaryEducation
from MainFolder.Other.Encoder import EducationalInstitutionEncoder
from MainFolder.config import MITSO_NAME, MGKE_NAME, BGUFK_NAME
from MainFolder.functions import extract_pdf, extract_pdf_with_fitz

pdf_path = "../utils/test6.pdf"
pdf_path1 = "../utils/test7.pdf"


rows = extract_pdf(pdf_path)
rows1 = extract_pdf(pdf_path1)
parser = P24_bgufk()

h = HigherEducationInstitution(BGUFK_NAME)

for dto in parser.return_dto(rows):
    h.add_speciality(Speciality(),dto)
for dto in parser.return_dto(rows1):
    h.add_speciality(Speciality(),dto)


print(json.dumps(h, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False))

with open('../utils/bgufk.json', 'w', encoding='utf-8') as f:
     # Сохраняем результат в файл с использованием json.dumps
     json.dump(h, f, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False)