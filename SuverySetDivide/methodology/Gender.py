import math


class Gender():
    def __init__(self):
        self.security = 1.0
        self.schooling = 1.0
        self.house_rent = 1.0
        self.distance_from_HT = 1.0
        self.security_levels_list = [0.33, 0.66, 1.0]
        self.schooling_levels_list = [0.33, 0.66, 1.0]
        self.house_rent_levels_list = [0.33, 1.0, 0.66]
        self.distance_from_HT_levels_list = [0.33, 1.0, 0.66]

    def satisfaction_function(self, security_level, schooling_level, house_rent_level, distance_from_HT_level):
        satisfaction = self.security_levels_list[security_level] * self.security + self.schooling_levels_list[schooling_level] * self.schooling + self.house_rent_levels_list[house_rent_level] * self.house_rent + self.distance_from_HT_levels_list[distance_from_HT_level] * self.distance_from_HT
        return satisfaction
