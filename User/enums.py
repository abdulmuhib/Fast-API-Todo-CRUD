from enum import Enum

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"


class Interest(str, Enum):
    Sports = "Sports"
    Gaming = "E-Gaming"
    Farming = "Farming"