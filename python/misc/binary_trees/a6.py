"""
Algo: Same Tree

Engineering Method:
    Explore:
        - where do i start?
            - start at head for each, tree
        - how do i move?
            - recursively move through each tree at the same time, 
                and if a value doesn't match return False early else continue, 
                until the end, if end is reached return True
        - what are the boundaries?
            - boundaries will be leaf nodes
        - what is the action?
            - compare each tree while moving through
    Brainstorm:
    Plan:
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Implement
def is_same_tree(node1:TreeNode, node2:TreeNode) -> bool:
    if node1 is None or node2 is None:
        return 
    if node1.value != node2.value:
        return False



    

# Verify
tree1 = TreeNode(1, TreeNode(7), TreeNode(3))


tree2 = TreeNode(1, TreeNode(3), TreeNode(3))

tree3 = TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(3)))

print(is_same_tree(tree1, tree1) == True)
print(is_same_tree(tree1, tree2) == False)
print(is_same_tree(tree2, tree3) == False)




