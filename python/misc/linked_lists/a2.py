"""
Explore:
    
Brainstorm:
    - link last node with head node
        - requires looping through linked list
        time complexity would be O(n)
        - linking tail to head, and storing constant variables
        space complexity O(1)

Plan:


"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)


def create_cycle(head:Node):
    """
    Link the last node to the head node, creating a cycle.
    """
    if not head:
        return

    current = head
    while current.next:

        current = current.next
    current.next = head
    return head


LL1 = Node(1, Node(2, Node(3)))

try:
    print(create_cycle(LL1))
    print(False)
except RecursionError:
    print(True)
