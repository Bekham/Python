class Worker:
    __income = {'Engineer': {"wage": 1200, "bonus": 700}, 'Master': {"wage": 1000, "bonus": 500}}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'Worker {self.name} {self.surname}'

    def get_total_income(self):
        return f' Total {self.position} salary {sum(item for item in Worker._Worker__income[self.position].values())}.'


p = Position('Ivan', 'Ivanov', 'Engineer')
print(p.get_full_name())
print(p.get_total_income())
e = Position('Petr', 'Petrov', 'Master')
print(e.get_full_name())
print(e.get_total_income())
