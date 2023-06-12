# def brick(height):
#     print("#" * height)

# def main():
#     for _ in range(3):
#         brick(3)

# main()
'''
###
###
###
'''


# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main() # ????


def main():
    print_square(int(input("Height: ")))

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("*" * width)

main()
'''
*****
*****
*****
*****
*****
'''