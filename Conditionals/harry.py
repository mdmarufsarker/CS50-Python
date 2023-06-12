name = input("What is your name? ")

# using if, elif, else to check for name
if name == "Harry":
    print("Gryffindor!")
elif name == "Hermione":
    print("Gryffindor!")
elif name == "Draco":
    print("Slytherin!")
else:
    print("Hufflepuff!")


# using if, elif, else to check for name
if name == "Harry" or name == "Hermione":
    print("Gryffindor!")
elif name == "Draco":
    print("Slytherin!")
else:
    print("Hufflepuff!")


# using match case
match name:
    case "Harry":
        print("Gryffindor!")
    case "Hermione":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Hufflepuff!")


# using match case
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Hufflepuff!")