"""
Recursive Max value for factorial
using answer 1
"""
def recursive_factorial(num:int) -> int:

    # base case
    if num == 1:
        return num 

    fact = num * recursive_factorial(num - 1)
    return fact


def recursive_max(arr:list) -> int:
    if len(arr) == 0:
        return 0
    val = arr.pop(0)
    
    if val <= 0:
        return 0
    # base case
    fact = recursive_factorial(val) 
    val2 = recursive_max(arr)
    max_val = max(val, val2)

    return max_val

assert recursive_max([3, 4, 9])
assert recursive_max([3, 4, -5, 0])

"""
Conclusion:
    Not optimal, but nice experiment
"""
