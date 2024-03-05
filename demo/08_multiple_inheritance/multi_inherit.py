
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hey, I'm {self.name}")

p = Person("Sam")
p.introduce()


class Employee(Person):
    def __init__(self, name, position):
        Person.__init__(self, name)
        self.position = position

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am the {self.position}")


class Soldier(Person):
    def __init__(self, name, rank):
        Person.__init__(self, name)
        self.rank = rank

    def introduce(self):
        print(f"SIR! I AM {self.rank} {self.name}! SIR!")


e = Employee("Helen", "Branch Manager")
e.introduce()

s = Soldier("Rutherford", "Seargent")
s.introduce()


class MilitarySubordinate(Employee, Soldier):
    def __init__(self, name, rank, position):
        Employee.__init__(self, name, position)
        Soldier.__init__(self, name, rank)


msb = MilitarySubordinate("Ali", "Commander", "Acquisition Officer")
msb.introduce()
