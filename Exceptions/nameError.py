import sys

def main():
    x = get_int("x: ")
    print(f"x = {x}")

def get_int(x):
    while True:
        try:
            return int(input(x))
        except ValueError:
            # pass
            print("Error: x must be an integer.")
            # sys.exit()
        else:
            break

if __name__ == "__main__":
    main()

