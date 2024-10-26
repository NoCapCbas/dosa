"""
Find max element in a linked list
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + '->' + str(self.next)

def max_value(node:Node):
    if node is None:
        return 0
    curr = node
    max_value = float('-inf')
    while curr:

        if curr.value > max_value:
            max_value = curr.value
        # increment
        curr = curr.next
    return max_value

ll1 = Node(1,Node(2,Node(4)))
print(max_value(ll1) == 4)
ll1 = Node(9,Node(2,Node(4)))
print(max_value(ll1) == 9)
