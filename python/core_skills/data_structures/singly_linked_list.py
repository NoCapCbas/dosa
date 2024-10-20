"""
Singly Linked List implementation
"""

class Node: 
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

