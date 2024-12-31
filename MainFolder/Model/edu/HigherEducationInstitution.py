from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.edu.EducationalInstitution import EducationalInstitution
from MainFolder.Model.Speciality import Speciality
from MainFolder.config import DEFAULT_HIGHER_EDUCATIONAL_LEVEL, DEFAULT_HIGHER_STUDY_DURATION, ELEVEN_AFTER_GRADE


class HigherEducationInstitution(EducationalInstitution):
    def __init__(self, name: str):
        super().__init__(name)


    def add_speciality(self, speciality: Speciality, dto:DTO):
        speciality.education_level = DEFAULT_HIGHER_EDUCATIONAL_LEVEL  # Присваиваем уровень образования
        speciality.study_duration = DEFAULT_HIGHER_STUDY_DURATION
        speciality.after_grade = ELEVEN_AFTER_GRADE
        super().add_speciality(speciality,dto)


    def to_dict(self):
        return {
            'name': self.name,
            'specialities': [speciality.to_dict() for speciality in self.specialities]
        }

