# Inheritance

class Wizard:
    def __init__(self, name):
        if not name:
            raise Exception("Name cannot be empty.")
        self.name = name

class Student (Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
class Professor (Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Harry")

maruf = Student("Harry", "Gryffindor")
print(f"{maruf.name} from {maruf.house}")

snape = Professor("Snape", "Potions")
print(f"{snape.name} teaches {snape.subject}")