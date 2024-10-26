# reverse_linked_list.py
"""
Reverse a linked list
Given the beginning of a singly linked list head, 
reverse the list, and return the new beginning of the list.
Level: Easy

Example 2:
Input: head = []

Output: []


"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def reverse_linked_list(head:Node):
    """
    Recursivly reverse linked list
    Time: O(n)
    Space: O(n)
    1 -> 2 -> 3 -> None
    c1  c2    c
    """
    
    if not head:
        return

    curr = head
    if curr.next:
        new_node = reverse_linked_list(curr.next)
        new_node.next = curr
    else:
        curr
    
    prev_node = curr
    
    return


LL1 = Node(1, Node(2, Node(3)))
print(reverse_linked_list(LL1))
