class Student:
    def __init__(self, name, house, patronus):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise RuntimeError("Invalid house")
        
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house}'
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Enter name: ")
    house = input("Enter house: ")
    patronus = input("Enter patronus: ")
    
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()