"""
Backspace String Compare


Explore:
    - where do we start?
        - get new string backspace accounted for
    - how do we move?
        - left to right of each string
    - what are the boundaries?
        - end of string
    - what is the action?
        - remove char before '#', and dont append '#' to queue

Brainstorm:
    Approach 1:
        - use queue to create new string, 
        can create a seperate function for this
"""

def backspace_compare(s1, s2):
    def backspace(string):
        q = []
        for char in string:
            if char == '#' and q:
                    q.pop()
            else:
                q.append(char)
        return ''.join(q)
    
    new_s1 = backspace(s1)
    new_s2 = backspace(s2)
    return new_s1 == new_s2


# verify



"""
Conclusion:
    Time Complexity:
        - O(n+m), due to iterating through sstring 1 plus string 2
    Space Complexity:
        - O(n+m), same as time due to appending each character not backspaced to queue, in order to compare final result
"""
