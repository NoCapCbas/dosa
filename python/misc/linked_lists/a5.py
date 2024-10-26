"""
Count elements in a linked list iteratively
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + '->' + str(self.next)

def num_sum(node:Node) -> int:
    curr = node
    sum_val = 0
    while curr:
        sum_val += curr.value
        #increment
        curr = curr.next
    print(sum_val)
    return sum_val


assert num_sum(Node(1,Node(2,Node(3)))) == 6
assert num_sum(Node(1,Node(2,Node(6)))) == 9
assert num_sum(Node(0)) == 0



