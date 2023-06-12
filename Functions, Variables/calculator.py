x = int(input("x: "))
y = int(input("y: "))

print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x // y = {x // y}")
print(f"x % y = {x % y}")
print(f"x ** y = {x ** y}")

# x: 4 
# y: 7
# x + y = 11
# x - y = -3
# x * y = 28
# x / y = 0.5714285714285714
# x // y = 0
# x % y = 4
# x ** y = 16384


# print like this 43,278,177.00
m = float(input("m: "))
n = float(input("n: "))
ans = m + n
print(f"{m} + {n} = {ans:,.2f}")