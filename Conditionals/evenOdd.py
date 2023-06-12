def main():
    n = int(input("n: "))
    if isEven(n):
        print("even")
    else:
        print("odd")

# way 1
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# way 2
def isEven(n):
    return n % 2 == 0

# way 3
def isEven(n):
    return True if n % 2 == 0 else False

main()