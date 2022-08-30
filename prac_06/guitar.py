class Guitar:


    def __init__(self,name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): ${}".format(self.name,self.year,self.cost)

    def get_age(self):
        YEAR = 2022
        return YEAR - self.year

    def is_vintage(self):
        vintage_year = 50
        return self.get_age() >= vintage_year


    def get_guitar(self):
         return f"{self.name:<5} ({self.year}), worth $ {self.cost}"



