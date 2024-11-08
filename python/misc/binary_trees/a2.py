"""
<<<<<<< HEAD
Univalued Binary Tree
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Given a binary tree:
                 1
                / \
               1   1
              / \
             1   1
// returns True

Explore:
    - where do we start?
        - head
    - how do we move?
        - left right recursion
    - what are the boundaries?
        - node is None
    - what is the action?
        if value is equal to parent nodes

Brainstorm:
    - return compare left and right and curr,
        return True if they all match else False

Plan:

Implement:
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_univalue(node:TreeNode):

    def helper(node:TreeNode, uni_val):
        if node is None:
            return True, uni_val

        left_uni, left_val = helper(node.left, uni_val)
        right_uni, right_val = helper(node.right, uni_val)
        if left_uni == False or right_uni == False:
            return False, node.value
 
        if left_val != node.value and right_val != node.value:
            return False, node.value
        return True, node.value

    if node is None:
        return True
    is_uni, uni_val = helper(node, node.value)
    return is_uni
    

# Test Cases
print(is_univalue(None), True)
print(is_univalue(TreeNode(1, TreeNode(2), TreeNode(3))), False) # 3
print(is_univalue(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), False)
print(is_univalue(TreeNode(1)), True)
print(is_univalue(TreeNode(1, TreeNode(1, TreeNode(1)), TreeNode(1, None, TreeNode(1, TreeNode(1))))), True)
>>>>>>> origin/main
