"""
Count skipped pairs using only recursion no loops

Explore:
    - where do we start?
        - at the first char of string
    - how do we move?
        - recurse through string 
    - what are the boundaries?
        - last char of string
    - what is the action?
        - count skipped pairs

Brainstorm:
 - two pointers, 1 character away from each other
 - start one pointer at 0, other pointer at index 2, return 0 for strings under length of three
 - check if char of each pointer matches, then increment if match
 - return if last pointer reaches end of string
"""

def count_skipped_pairs(string):
    if len(string) < 3:
        return 0

    def helper(string, p1, p2, count):
        if p2 > len(string)-1:
            return count

        if string[p1] == string[p2]:
            count += 1

        count = helper(string, p1+1, p2+1, count)
        return count 

    count = helper(string, 0, 2, 0)
    return count
    


# verify
print(count_skipped_pairs("axa") == 1)
print(count_skipped_pairs("axax") == 2)
print(count_skipped_pairs("aaa") == 1)

