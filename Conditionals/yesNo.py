res = input("Do you agree? ").strip().lower()
# strip() removes leading and trailing whitespace
# lower() converts to lowercase

if res == 'y' or 'yes':
    print("Agreed.")
else:
    print("Not agreed.")


if res.startswith('y'):
    print("Agreed.")
else:
    print("Not agreed.")