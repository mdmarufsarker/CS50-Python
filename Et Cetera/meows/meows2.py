# run this program with `mypy meows2.py` to check for type errors

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)

print(meows)

