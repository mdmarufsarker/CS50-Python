# take username
name = input("Name: ")
# print hello, username
print("Hello, " + name)
# using f-string (formatted string)
print(f"Hello, {name}")
# using format method
print("Hello, {}".format(name))
# using %s (string)
print("Hello, %s" % name)
print("Hello,", name)

'''CS50-Python/Functions, Variables/variables.py
In python the print function used new line by default but we can change it by using end parameter. Also we can use sep parameter to separate the values.
'''

print("Hello", end="") # ebar new line print hobe na
print("Hello", end="\t") # ebar tab print hobe

print()

# sep parameter bujte hole jana lagbe j python a jokhon amra 2 print value print kori tokhon auto ekta space majhe bose jay
print("Hello", "Maruf") # Hello Maruf
# but ami kono space na diye print korte chai
print("Hello", "Maruf", sep="") # HelloMaruf
# ba onno kono character diyeo print korte pari
print("Hello", "Maruf", sep="*") # Hello*Maruf



print(name.strip()) # removes all whitespace characters from both ends
print(name) # Maruf Sarker
print(name.upper()) # MARUF SARKER
print(name.lower()) # maruf sarker
print(name.title()) # Maruf Sarker
print(name.capitalize()) # Maruf sarker
print(name.swapcase()) # mARUF sARKER


# strip example
myName = "Maruf Sarker"
fName, lName = myName.split()
print(fName, lName) # Maruf Sarker