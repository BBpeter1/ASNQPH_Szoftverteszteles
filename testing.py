# testing Fibonacci number function

def fib(n: int) -> int:
    return n if n < 2 else fib(n-1)+fib(n-2)

def plus(n: int, b: int) -> int:
    return n+b

def szoveg(n: int) -> string:
    if n / 2 = 1:
        return "valami"
    else:
        return "semmi"


def test_fibonacci():
    assert fib(10) == 55

def test_plus():
    assert plus(5,5) == 10

def test_szoveg():
    assert szoveg(2) == "valami"
