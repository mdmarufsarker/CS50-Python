import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})

'''
def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
'''
# Here I am going to use lamda function. Why? Because here get_name and get_house are only used once. So, it is better to use lambda function which is anonymous function and can be used only once. Here lambda function doesn't have any name. It is just a function. It is just a function which takes student as an argument and returns student["name"].

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")