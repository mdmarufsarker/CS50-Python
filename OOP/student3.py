class Student:
    def __init__(self, fname="Maruf", lname="Sarker", house="Dhaka"):
        if not fname and not lname:
            raise RuntimeError("Missing first and last name")
        if not fname:
            raise RuntimeError("Missing first name")
        if not lname:
            raise RuntimeError("Missing last name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise RuntimeError("Invalid house")
        
        self.fname = fname
        self.lname = lname
        self.house = house

    def __str__(self):
        return f'{self.fname} {self.lname} from {self.house}'

def main():
    student = get_student()
    print(student)

def get_student():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    house = input("Enter house: ")
    try:
        return Student(fname, lname, house)
    except RuntimeError as error:
        print(error)
        return get_student()

if __name__ == "__main__":
    main()