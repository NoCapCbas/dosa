""" 
Problem 4:
Given a linked list, return the number of values that occur twice.

### Example 1:
head = 1 -> 2 -> 2 -> 3 -> 3 -> None
numPairs(head) == 1

"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def numPairs():
    pass
