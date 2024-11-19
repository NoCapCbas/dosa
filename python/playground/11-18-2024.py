

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_fib():
    # Test cases
    print(f"fib(0) == {fib(0)}")  # Base case, should return 0
    print(f"fib(1) == {fib(1)}")  # Base case, should return 1
    print(f"fib(2) == {fib(2)}")  # Should return 1
    print(f"fib(3) == {fib(3)}")  # Should return 2
    print(f"fib(5) == {fib(5)}")  # Should return 5
    print(f"fib(10) == {fib(10)}")  # Should return 55
    print(f"fib(15) == {fib(15)}")  # Should return 610



if __name__ == "__main__":
    test_fib()
