from MainFolder.Model.DTO.DTO import DTO
from MainFolder.Model.edu.EducationalInstitution import EducationalInstitution
from MainFolder.Model.Speciality import Speciality
from MainFolder.config import DEFAULT_TECHNICHIAL_EDUCATIONAL_LEVEL, DEFAULT_OTHER_STUDY_DURATION, NINE_AFTER_GRADE


class ProfessionalTechnicalEducation(EducationalInstitution):
    def __init__(self, name: str):
        super().__init__(name)

    def add_speciality(self, speciality: Speciality, dto:DTO):
        speciality.education_level = DEFAULT_TECHNICHIAL_EDUCATIONAL_LEVEL
        speciality.study_duration = DEFAULT_OTHER_STUDY_DURATION
        speciality.after_grade = NINE_AFTER_GRADE
        super().add_speciality(speciality,dto)

    def to_dict(self):
        return {
            'name': self.name,
            'specialities': [speciality.to_dict() for speciality in self.specialities]
        }
