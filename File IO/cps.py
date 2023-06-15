import csv

students = []

with open("cps.csv") as file:
    reader = csv.reader(file)
    for timeStamp, name, email, discordHandle, batch2, university, contact, cfHandle, payment, bkash, fbProfile, accessDone, vjudgeHandle, hackerrankHandle, videoAccess, discordAccess, cfFriend, emailAdd in reader:
        student = {
            "name": name,
            "email": email,
            "contact": contact,
            "university": university,
            "fbProfile": fbProfile,
            "cfHandle": cfHandle,
            "vjudgeHandle": vjudgeHandle,
            "hackerrankHandle": hackerrankHandle,
            "discordHandle": discordHandle
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
                if search in student["name"] or search in student["email"] or search in student["contact"] or search in student["university"]:
                    # print each details on new line
                    print(f"Name: {student['name']}\nEmail: {student['email']}\nContact: {student['contact']}\nUniversity: {student['university']}\n")
        case 2:
            print("Enter user email: ", end="")
            search = input()
            for student in students:
                if search in student["name"] or search in student["email"] or search in student["contact"] or search in student["university"]:
                    print(f"Facebook Profile: {student['fbProfile']}\nCodeforces Handle: {student['cfHandle']}\nVjudge Handle: {student['vjudgeHandle']}\nHackerrank Handle: {student['hackerrankHandle']}\nDiscord Handle: {student['discordHandle']}\n")
        case 3:
            exit(0)
        case _:
            print("Invalid choice!")