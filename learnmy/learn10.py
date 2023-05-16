# Конструкторы, переопределение методов

class Cat:
    name = None
    age = None
    isHappy = None
    
    def __init__(self, name, age, isHappy):
        # pass  - default
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy
        self.set_data(name, age, isHappy)
        self.get_data()
    
    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    
    def get_data(self):
        print(self.name,"age:",self.age,"Happy:",self.isHappy)

cat1 = Cat("Барсик", 3, True)

cat2 = Cat("Жопен", 2, False)


cat1.get_data()
cat2.get_data()
