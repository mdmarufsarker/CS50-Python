import pytest

from calculator import square

def main():
    test_square()

def test_positive():
    assert square(10) == 100
    assert square(0) == 0
    assert square(2.5) == 6.25
    assert square(2) == 4
    assert square(3) == 9
    assert square(1000000) == 1000000000000
    
def test_negative():
    assert square(-1) == 1
    assert square(-2.5) == 6.25
    assert square(-2) == 4
    assert square(-1000000) == 1000000000000
    
def test_zero():
    assert square(0) == 0

# string is not a valid input
def test_str():
    with pytest.raises(TypeError):
        square("hello")

if __name__ == "__main__":
    main()