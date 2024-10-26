"""
Merge two sorted lists
"""

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + '->' + str(self.next)

def merge_two_sorted_lists(node1:Node, node2:Node):

    # assign pointer for each list
    curr1, curr2 = node1, node2 
    dummy_head = Node('x')
    
    while curr1 or curr2:
        curr1_added = False
        curr2_added = False

        if curr1.value < curr2.value:     
            dumm
            


        # increment each if next exists
        if curr1_added:
            curr1 = curr1.next
        if curr2_added:
            curr2 = curr2.next
    

ll1, ll2 = Node(1,Node(2,Node(4))), Node(1,Node(3,Node(5)))
print(merge_two_sorted_lists())

ll1, ll2 = Node(1,Node(1,Node(4))), Node(1,Node(3,Node(5)))
print(merge_two_sorted_lists())

ll1, ll2 = Node(1,Node(2,Node(4))), Node(1,Node(3,Node(5)))
print(merge_two_sorted_lists())
