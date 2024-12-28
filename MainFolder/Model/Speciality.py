from MainFolder.config import DEFAULT_EDUCATIONAL_YEAR


class Speciality:
    def __init__(
        self,
        name: str = None,
        specialty_code: str = None,
        qualification: str = None,
        passing_score_paid: int = None,
        passing_score_budget: int = None,
        year: int = DEFAULT_EDUCATIONAL_YEAR,
        faculty: str = None,
        plan_paid: int = None,
        plan_budget: int = None,
        study_duration: int = None,
        education_level: str = None,  # ССО/ВО/ПТО
        study_form: str = None,       # Дневное/Заочное
        exam_type: str = None,        # Тип экзамена: экзамены и проходной балл
        is_shortened: bool = None,    # Обычное/Сокращенное
        after_grade: int = None,      # После 9/11
        contest: float = None,          # Конкурс
        note: str = None              # Примечание
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
        self.contest = contest
        self.note = note


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
            'contest': self.contest,
            'note': self.note
        }


        # Сеттеры для каждого поля
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value: str):
            self._name = value

        @property
        def specialty_code(self):
            return self._specialty_code

        @specialty_code.setter
        def specialty_code(self, value: str):
            self._specialty_code = value

        @property
        def qualification(self):
            return self._qualification

        @qualification.setter
        def qualification(self, value: str):
            self._qualification = value

        @property
        def passing_score_paid(self):
            return self._passing_score_paid

        @passing_score_paid.setter
        def passing_score_paid(self, value: int):
            self._passing_score_paid = value

        @property
        def passing_score_budget(self):
            return self._passing_score_budget

        @passing_score_budget.setter
        def passing_score_budget(self, value: int):
            self._passing_score_budget = value

        @property
        def year(self):
            return self._year

        @year.setter
        def year(self, value: int):
            self._year = value

        @property
        def faculty(self):
            return self._faculty

        @faculty.setter
        def faculty(self, value: str):
            self._faculty = value

        @property
        def plan_paid(self):
            return self._plan_paid

        @plan_paid.setter
        def plan_paid(self, value: int):
            self._plan_paid = value

        @property
        def plan_budget(self):
            return self._plan_budget

        @plan_budget.setter
        def plan_budget(self, value: int):
            self._plan_budget = value

        @property
        def study_duration(self):
            return self._study_duration

        @study_duration.setter
        def study_duration(self, value: int):
            self._study_duration = value

        @property
        def education_level(self):
            return self._education_level

        @education_level.setter
        def education_level(self, value: str):
            self._education_level = value

        @property
        def study_form(self):
            return self._study_form

        @study_form.setter
        def study_form(self, value: str):
            self._study_form = value

        @property
        def exam_type(self):
            return self._exam_type

        @exam_type.setter
        def exam_type(self, value: str):
            self._exam_type = value

        @property
        def is_shortened(self):
            return self._is_shortened

        @is_shortened.setter
        def is_shortened(self, value: bool):
            self._is_shortened = value

        @property
        def after_grade(self):
            return self._after_grade

        @after_grade.setter
        def after_grade(self, value: int):
            self._after_grade = value

        @property
        def contest(self):
            return self._contest

        @contest.setter
        def contest(self, value: str):
            self._contest = value

        @property
        def note(self):
            return self._note

        @note.setter
        def note(self, value: str):
            self._note = value