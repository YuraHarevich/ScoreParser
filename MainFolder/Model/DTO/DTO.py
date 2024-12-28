class DTO:
    def __init__(
        self,
        name: str = None,
        specialty_code: str = None,
        passing_score_paid: int = None,
        passing_score_budget: int = None,
        faculty: str = None,
        plan_paid: int = None,
        plan_budget: int = None,
        study_form: str = None,
        is_shortened: bool = None,
        contest: float = None
    ):
        self.name = name
        self.specialty_code = specialty_code
        self.passing_score_paid = passing_score_paid
        self.passing_score_budget = passing_score_budget
        self.faculty = faculty
        self.plan_paid = plan_paid
        self.plan_budget = plan_budget
        self.study_form = study_form
        self.is_shortened = is_shortened
        self.contest = contest