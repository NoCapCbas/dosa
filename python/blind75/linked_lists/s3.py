"""
Reorder List Solution
Iterative Approach:
    Time Complexity: O(n+m)
        Due to iterating over every item in linked list,
        plus the every item in the second list
    Space Complexity: O(1)
        Only constant variables created

Recursive Approach:
    Time Complexity: O(n+m)
        Due to iterating over every item in linked list,
        plus the every item in the second list
    Space Complexity: O(n+m)
        Due to iterating over every item in linked list,
        plus the every item in the second list the call stack will
        also be n+m 
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def iterative_approach(l1:Node, l2:Node): 
    dummy = Node('x')
    curr = dummy
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            curr.next = l1
            l1 = l1.next
        elif l2.value <= l1.value:
            curr.next = l2
            l2 = l2.next
    if l1 is not None:
        curr.next = l1
    elif l2 is not None:
        curr.next = l2
    return dummy.next

def recursive_approach(l1:Node, l2:Node):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.value <= l2.value:
        l1.next = recursive_approach(l1.next, l2)
        return l1
    elif l2.value <= l1.value:
        l2.next = recursive_approach(l1, l2.next)
        return l2



