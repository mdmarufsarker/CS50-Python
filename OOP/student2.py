def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"

    print(f'{student["name"]} from {student["house"]}')

def get_student():
    # Way 1:
    # student = {}
    # student["name"] = input("Enter name: ")
    # student["house"] = input("Enter house: ")
    # return student # dictionary packing {name: "Padma", house: "Ravenclaw"}

    # Way 2:
    # return {
    #     "name": input("Enter name: "),
    #     "house": input("Enter house: ")
    # }

    # Way 3:
    name = input("Enter name: ")
    house = input("Enter house: ")
    return {"name": name, "house": house}
    # dict --> mutable (can be changed)

if __name__ == "__main__":
    main()