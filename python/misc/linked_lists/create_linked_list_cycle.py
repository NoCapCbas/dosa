
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)


def create_cycle(head:Node):
    """
    Link the last node to the head node, creating a cycle.
    Example:
    input: 1 -> 2 -> 3 -> None
    output:
    1 -> 2
    ^   
      \  |
        3
    Verify:
        The test should check for RecursionError
    """
    if not head:
        return

    current = head
    while current.next:

        current = current.next
    current.next = head
    print(head)
    return 


LL1 = Node(1, Node(2, Node(3)))

try:
    create_cycle(LL1) 
    print(False)
except RecursionError:
    print(True)
