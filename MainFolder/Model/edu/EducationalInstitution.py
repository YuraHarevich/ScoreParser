from abc import abstractmethod, ABC
from MainFolder.Model.DTO.DTO import DTO

from MainFolder.Model.Speciality import Speciality


class EducationalInstitution(ABC):
    def __init__(self, name: str):
        self.name = name
        self.specialities = []

    def add_speciality(self, speciality: Speciality,dto:DTO):
        speciality.name = dto.name
        speciality.specialty_code = dto.specialty_code
        speciality.passing_score_paid = dto.passing_score_paid
        speciality.passing_score_budget = dto.passing_score_budget
        speciality.faculty = dto.faculty
        speciality.plan_paid = dto.plan_paid
        speciality.plan_budget = dto.plan_budget
        speciality.study_form = dto.study_form
        speciality.is_shortened = dto.is_shortened
        speciality.contest = dto.contest
        speciality.qualification = dto.qualification
        self.specialities.append(speciality)


    @abstractmethod
    def to_dict(self):
        """Метод для преобразования объекта в словарь."""
        pass
