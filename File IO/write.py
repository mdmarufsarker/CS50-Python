import csv

name = input("Enter your name: ")
home = input("Enter your home address: ")

with open("harryPotter.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])

    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})