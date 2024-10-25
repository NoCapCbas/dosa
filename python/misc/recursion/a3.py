
"""
Sum all the elements in an array, recursively
"""

def sum_arr_recursively(arr:list) -> int:
    
    # base case
    if len(arr) == 1:
        return arr[0]

    value = arr.pop(0)
    value += sum_arr_recursively(arr)
    return value

assert sum_arr_recursively([3, 2, 1]), 6
assert sum_arr_recursively([3, 2, 1, 2, 3]), 19
assert sum_arr_recursively([3]), 3 


