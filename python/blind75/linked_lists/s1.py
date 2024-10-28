"""
Reversed Linked List Solution
Iterative Approach:
    Time Complexity: O(n)
        Due to iterating over every item in linked list
    Space Complexity: O(1)
        Only constant variables created

Recursive Approach:
    Time Complexity: O(n)
        Due to iterating over every item in linked list
    Space Complexity: O(n)
        Due to call stack holding up to n nodes from linked list
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def iterative_approach(node:Node): 
    prev = None
    curr = node
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def recursive_approach(node:Node):
    if node is None or node.next is None:
        return node

    new_node = recursive_approach(node.next)
    node.next.next = node
    node.next = None
    return new_node
    pass


