"""
Find Three Largest Numbers

Explore:
    - brute force, find max three times, removing that max each time
    - start with empty list, loop adding ints to list if curr is greater than any of three
    - sort array, grab last 3

Brainstorm:
    where to start?
        - start at the 0 index of list
    how to move?
        - iterate through list
    what are the boundaries?
        - end of list
    what is the action?
        - get three largest
"""

def find_three_largest(arr:list[int]) -> list[int]:
    
    arr.sort()
    return arr[-3:]

print(find_three_largest([1,5,8,3,9,54,32,78]) == [32, 54, 78])

"""
Conclusion:
    Time Complexity:
        O(nlogn), due to sorting worst case

    Space Complexity:
        O(1), sorting is done in place

"""
