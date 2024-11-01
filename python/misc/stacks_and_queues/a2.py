
"""
## Problem 2: Valid Parentheses
Given a string containg the only the following characters:
'{}[]()'
Determine if the input string is valid.
Open brackets must be closed and in the correct order.

# Explore

# Brainstorm
- get length of string
- divide by 2, if there is remainder early return, 
because it must be even sincethe needs to be open and close symbol
- if no remainder continue to half length of string and add each
item to queue, then iterate through queue popping off item and comparing them to the remaining string, if chars do not match return False, if reaches the end return True

"""


def valid_parentheses(chrs:str):
    import queue
    map = {
        "(":")",
        "[":"]",
        "{":"}",
    }
    if len(chrs) % 2 != 0:
        return False

    q = queue.Queue() 
    for idx in range(len(chrs)):
        bracket = chrs[idx]

        if bracket in map:
            q.put(map[bracket])
        else:
            bracket_match = q.get()
            if bracket != bracket_match:
                return False
            

    return True

# Verify
print(valid_parentheses("()")==True)
print(valid_parentheses("()[]{}")==True)
print(valid_parentheses("(]")==False)
print(valid_parentheses("([]]")==False)






