import csv

students = []

with open("cps.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student = {
            "Name": row["Name"],
            "Email": row["Email"],
            "Contact": row["Mobile No"],
            "University": row["University Name"],
            "fbProfile": row["Contact"],
            "cfHandle": row["Codeforces User Name"],
            "vjudgeHandle": row["Vjudge User Name"],
            "hackerrankHandle": row["HackerRank User Name"],
            "discordHandle": row["Discord User Name"]
        }
        students.append(student)

while True:
    print("\nCPS Academy")
    print("-----------")
    print("1. Search for name, email, contact, university")
    print("2. Search for fbProfile, cfHandle, vjudgeHandle, hackerrankHandle, discordHandle")
    print("3. Exit")
    print("Enter your choice: ", end="")
    choice = int(input())

    match choice:
        case 1:
            print("Enter user email: ", end="")
            search = input()
            for student in students:
                if search in student["Name"] or search in student["Email"] or search in student["Contact"] or search in student["University"]:
                    # print each details on new line
                    print(f"Name: {student['Name']}\nEmail: {student['Email']}\nContact: {student['Contact']}\nUniversity: {student['University']}\n")
        case 2:
            print("Enter user email: ", end="")
            search = input()
            for student in students:
                if search in student["Name"] or search in student["Email"] or search in student["Contact"] or search in student["University"]:
                    print(f"Facebook Profile: {student['fbProfile']}\nCodeforces Handle: {student['cfHandle']}\nVjudge Handle: {student['vjudgeHandle']}\nHackerrank Handle: {student['hackerrankHandle']}\nDiscord Handle: {student['discordHandle']}\n")
        case 3:
            exit(0)
        case _:
            print("Invalid choice!")