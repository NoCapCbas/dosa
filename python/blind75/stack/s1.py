"""
Valid Parentheses Solution

Time Complexity: O(n)
    Due to iterating over every character in string

Space Complexity: O(n)
    Due to having to append chrs to stack as iterating
    
"""

def valid_parentheses(string:str) -> bool:
    stack = []
    closeToOpen = { ')':'(', ']':'[', '}':'{'}

    for chr in string:
        if chr in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(chr)

    return True if not stack else False


