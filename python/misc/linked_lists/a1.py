'''

Explore:
- iteratively
- recursively?

Brainstorm:
    Approach 1:
        iterate x times and link each node     
    Time: O(n)
    Space: O(n)

Plan:


'''
# Implement
class Node():
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def approach1(x, y):
    # iterative 
    prev_node = None
    # iterate through each idx through x
    for idx in range(x, 0, -1):
        if prev_node:
            node = Node(y, prev_node)
        else:
            # create last node 
            node = Node(y)

        prev_node = node
    return node
        
# Verify
print(Node(2, Node(2, Node(2))))
print(approach1(3, 2))

          

    

    
