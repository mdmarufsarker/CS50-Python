def f(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

f(1, 2, 3, a=4, b=5)

# Positional args: (1, 2, 3)
# Keyword args: {'a': 4, 'b': 5}