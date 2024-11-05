"""
Find Max Element in a Binary Tree (recursive)
Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 7


Explore:
    - where do we start?
        - start at the head
    - how do we move?
        - recurse through left and right nodes
    - what are the boundaries?
        - when node is none
    - what is the action?
        - find the maximum value, compare the returned value to 
        set maximum

Brainstorm:
    - check if none, return 
    - create helper function that takes in node and value
    and returns int

Plan:

    4, left:0, right:0

Implement:

"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_max(node:TreeNode) -> int:
    # recursive

    if not node:
        return float('-inf')

    tree_max_result = max(tree_max(node.left), tree_max(node.right), node.value)
    return tree_max_result


# Test Cases
print(tree_max(None), float("-inf"))
print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))), 3) # 3
print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
print(tree_max(TreeNode(1)), 1)
