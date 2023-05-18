# Наследование, инкапсуляция, полиморфизм

class Building:
    __year =None
    __city = None
    # __ - инкапсулирует поля
    def __init__(self, year, city):
        self.year = year
        self.city = city
    
    def get_info(self):
        print("Year:",self.year, ". City:", self.city, end = "")


class School(Building):
    pupils = 0
    
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year,city)  # super - обращение к родителю
        self.pupils = pupils
    
    def get_info(self):
        super(School,self).get_info()
        print(". Pupils: ", self.pupils)

school = School(125, 2000, "Moscow")
school.get_info()