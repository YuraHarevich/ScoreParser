import json


class Speciality:
    def __init__(
        self,
        name: str,
        specialty_code: str,
        qualification: str,
        passing_score_paid,#: int,
        passing_score_budget,#: int,
        year: int,
        faculty: str,
        plan_paid: int,
        plan_budget: int,
        study_duration: int,
        education_level: str,  # ССО/ВО/ПТО
        study_form: str,       # Дневное/Заочное
        exam_type: str,       # Тип экзамена: экзамены и проходной балл
        is_shortened: bool,    # Обычное/Сокращенное
        after_grade: int,      # После 9/11
        note: str = ""         # Примечание
    ):
        self.name = name
        self.specialty_code = specialty_code
        self.qualification = qualification
        self.passing_score_paid = passing_score_paid
        self.passing_score_budget = passing_score_budget
        self.year = year
        self.faculty = faculty
        self.plan_paid = plan_paid
        self.plan_budget = plan_budget
        self.study_duration = study_duration
        self.education_level = education_level
        self.study_form = study_form
        self.exam_type = exam_type
        self.is_shortened = is_shortened
        self.after_grade = after_grade
        self.note = note

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Specialty Code: {self.specialty_code}\n"
                f"Qualification: {self.qualification}\n"
                f"Passing Score (Paid): {self.passing_score_paid}\n"
                f"Passing Score (Budget): {self.passing_score_budget}\n"
                f"Year: {self.year}\n"
                f"Faculty: {self.faculty}\n"
                f"Plan Paid: {self.plan_paid}\n"
                f"Plan Budget: {self.plan_budget}\n"
                f"Study Duration: {self.study_duration}\n"
                f"Education Level: {self.education_level}\n"
                f"Study Form: {self.study_form}\n"
                f"Exam Type: {self.exam_type}\n"
                f"Is Shortened: {self.is_shortened}\n"
                f"After Grade: {self.after_grade}\n"
                f"Note: {self.note}\n\n\n\n\n")


    def to_dict(self):
        return {
            'name': self.name,
            'specialty_code': self.specialty_code,
            'qualification': self.qualification,
            'passing_score_paid': self.passing_score_paid,
            'passing_score_budget': self.passing_score_budget,
            'year': self.year,
            'faculty': self.faculty,
            'plan_paid': self.plan_paid,
            'plan_budget': self.plan_budget,
            'study_duration': self.study_duration,
            'education_level': self.education_level,
            'study_form': self.study_form,
            'exam_type': self.exam_type,
            'is_shortened': self.is_shortened,
            'after_grade': self.after_grade,
            'note': self.note
        }


class SpecialityEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Speciality):
            return obj.to_dict()
        return super().default(obj)