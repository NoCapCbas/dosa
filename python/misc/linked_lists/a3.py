# multiply_next_linked_list_value.py
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def multiply_next(head:Node) -> Node:
    """
    Multiply the value in each node by the value in the next node. 
    The tail node has no next node so multiply it by itself

    Example:
    input: 1 -> 2 -> 3 -> 4 -> None 
    output: 2 -> 6 -> 12 -> 16 -> None 
    """

    current = head
    while current.next:

        print(current.value)
        nxt = current.next 
        current.value = current.value * nxt.value
        print(current.value)
        print('------------')


        current = current.next
    current.value = current.value * current.value
    print(current.value)
    return head

LL1 = Node(1, Node(2, Node(3, Node(4))))
print(f"{multiply_next(LL1)} == {Node(2, Node(6, Node(12, Node(16))))}?")

    

