"""
Fibonacci Solution
"""

def fib(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# verify
print(fib(0) == 0)   # Output: 0
print(fib(1) == 1)   # Output: 1
print(fib(5) == 5)   # Output: 5
print(fib(10) == 55)  # Output: 55
print(fib(15) == 610)  # Output: 610

