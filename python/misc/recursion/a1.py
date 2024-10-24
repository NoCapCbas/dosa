"""
Recursive factorial
"""

def recursive_factorial(num:int) -> int:

    # base case
    if num == 1:
        return num 

    fact = num * recursive_factorial(num - 1)
    return fact

# verify

assert recursive_factorial(4) == 24
