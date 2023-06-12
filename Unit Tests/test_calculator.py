from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(10) == 100
    except AssertionError:
        print("Tests failed!")
    
    try:
        assert square(2) == 4
    except AssertionError:
        print("Tests failed!")

if __name__ == "__main__":
    main()