# names = []

# for _ in range(3):
#     names.append(input("Enter a name: "))

# print(names)

# # sort names
# for name in sorted(names):
#     print(f"Hello, {name}!")

# # sort names in reverse
# for name in sorted(names, reverse=True):
#     print(f"Hello, {name}!")



name = input("Enter a name: ")

with open("names.txt", "a") as file:
    file.write(name + "\n")


# Reading from a file
# Way 1
with open("names.txt", "r") as file:
    lines = file.readlines()
    for line in sorted(lines):
        print("Hello", line, end="", sep=" ")


# Way 2
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print("Hello", name)


# Way 3
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("Hello", line.strip()) 