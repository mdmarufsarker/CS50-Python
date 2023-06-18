# run this program with `mypy meows2.py` to check for type errors

def meow(n: int) -> str:
    return "meow\n" * n

# def meow(n):
#     """Meow n times."""
#     return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)

print(meows, end="")

