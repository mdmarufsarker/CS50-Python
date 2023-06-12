import pytest

from hello import hello

def test_hello():
    hello() == "Hello, world!"

def test_alice():
    hello("Alice") == "Hello, Alice!"

def test_bob():
    hello("Bob") == "Hello, Bob!"

if __name__ == "__main__":
    test_hello()