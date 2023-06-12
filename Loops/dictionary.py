students = {
    "Harry": "Gryffindor",
    "Draco": "Slytherin",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
}

for key, value in students.items():
    print(f"{key} is in {value}")

'''
Harry is in Gryffindor
Draco is in Slytherin
Ron is in Gryffindor
Hermione is in Gryffindor
'''

for student in students:
    print(student, students[student], sep=", ")

'''
Harry, Gryffindor
Draco, Slytherin
Ron, Gryffindor
Hermione, Gryffindor
'''