import sys

if len(sys.argv) == 2:
    sys.exit(f"Hello, {sys.argv[1]}")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    print("Hello, world")

