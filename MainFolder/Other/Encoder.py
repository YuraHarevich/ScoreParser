import json

from MainFolder.Model.edu.EducationalInstitution import EducationalInstitution
from MainFolder.Model.Speciality import Speciality


class EducationalInstitutionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, EducationalInstitution):
            return obj.to_dict()
        elif isinstance(obj, Speciality):
            return obj.to_dict()
        return super().default(obj)