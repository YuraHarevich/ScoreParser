import json

from MainFolder.Model.DTO.PDF.P21_bsu import P21_bsu
from MainFolder.Model.Speciality import Speciality
from MainFolder.Model.edu.HigherEducationInstitution import HigherEducationInstitution
from MainFolder.Other.Encoder import EducationalInstitutionEncoder
from MainFolder.config import BSUIR_NAME, BSU_NAME
from MainFolder.functions import fix_word_breaks, extract_pdf

pdf_path = "../utils/test2.pdf"
pdf_path1 = "../utils/test3.pdf"
import pdfplumber
import re
rows = extract_pdf(pdf_path)
parser = P21_bsu()

rows1 = extract_pdf(pdf_path1)

rows[27][0] = "Исторический факультет"
rows[34][0] = "Факультет журналистики"
rows[71][1]='объединенный конкурс:'
rows[72][0] = "Факультет философии и социальных наук"
rows[72][1]='социальная работа и консультирование'
rows[86][0] = "Филологический факультет"
rows[90][0] = None
rows[110][2] = '355'
rows[111][1]='объединенный конкурс:'
rows[116][1]='объединенный конкурс:'
rows[117][0] = "Военный факультет"
rows[120][0] = None


rows1[5][1]='объединенный конкурс:'

h = HigherEducationInstitution(BSU_NAME)

for dto in parser.return_dto(rows,1):
    h.add_speciality(Speciality(),dto)
for dto in parser.return_dto(rows1,2):
    h.add_speciality(Speciality(),dto)

print(json.dumps(h, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False))

with open('../utils/bsu.json', 'w', encoding='utf-8') as f:
     # Сохраняем результат в файл с использованием json.dumps
     json.dump(h, f, cls=EducationalInstitutionEncoder, indent=4, ensure_ascii=False)