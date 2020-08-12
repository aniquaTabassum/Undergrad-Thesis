from methodology import Gender


class Male(Gender.Gender):
    def __init__(self, marital_status, spouse_moving_status, spouse_employment_status):
        Gender.Gender.__init__(self)
        if (marital_status == 1) and (spouse_moving_status == 3):
            if spouse_employment_status == 6:
                self.security = 0.75
                self.schooling = 1.5
                self.house_rent = 2.5
                self.distance_from_HT = 0.25
                self.house_rent_levels_list = [0.33, 0.66, 1.0]
            else:
                self.security = 1.25
                self.schooling = 1.5
                self.house_rent = 2.0
                self.distance_from_HT = 0.25

        else:
            self.security = 1.0
            self.schooling = 1.25
            self.house_rent = 1.25
            self.distance_from_HT = 1.5
            self.distance_from_HT_levels_list = [0.66, 1.0, 0.33]



