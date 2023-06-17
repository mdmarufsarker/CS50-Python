def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Enter name: ")
    house = input("Enter house: ")
    return (name, house) # tuple packing (name, house) --> immutable (cannot be changed)

if __name__ == "__main__":
    main()