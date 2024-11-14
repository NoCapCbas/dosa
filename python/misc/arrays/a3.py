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
    for item in arr:
        if type(item) is int:
            total += item
        else:
            total += sum_nested_list(item)
    return total

# verify

print(sum_nested_list([1, 2, 3]) == 6)
print(sum_nested_list([1, [1, 2, 3], 3]) == 10)
print(sum_nested_list([1, [1, [1, [1, [1]]]]]) == 5)

"""
Conclusion:
    Time Complexity:
        o(n), due to looping through each item and nested item
    Space Complexity:
        o(n), due to call stack of each nested array
"""

