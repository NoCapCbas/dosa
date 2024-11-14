"""
Flatten nested list sum


Explore:
    - where to start?
        - beginning of array
    - how to move?
        loop through initial arr
    - what are boundaries?
        - end of initial arr
    - what is the action?
        - sum ints

Brainstorm:
    - can use recursion to loop through array, then return sum

"""

def sum_nested_list(arr:list):
    total = 0
    for item in array:
        if type(item) is int:
            total += item
        else:
            total += sum_nested_list(item)
    return total

# verify

sum_nested_list([1, 2, 3]) == 6
sum_nested_list([1, [1, 2, 3], 3]) == 10
sum_nested_list([1, [1, [1, [1, [1]]]]]) == 5

