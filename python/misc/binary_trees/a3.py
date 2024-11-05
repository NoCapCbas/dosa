"""
Find Height of a Binary Tree

Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 2


Explore:
    - where do we start?
        - root node
    - how do we move?
        - recursively, returning level
    - what are the boundaries?
        - node is None
    - what is the action?
        - increment each level

Brainstorm:
    - Approach 1:
        base case, return 0
        else return 1
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_height(node:TreeNode) -> int:
    # base case return 0 
    if node is None:
        return -1


    # recurse passing node.left and node.right separately
    # store returned val in left_val, right_val, return the max between the two

    left_val = tree_height(node.left)
    right_val = tree_height(node.right)
    max_val = max(left_val, right_val)
    return max_val + 1

    
    

# Verify Test Cases
print(tree_height(None), -1) # -1
print(tree_height(TreeNode(1, TreeNode(2), TreeNode(3))), 1) # 1
print(tree_height(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 3) # 3
print(tree_height(TreeNode()), 0) # 0

"""
Conclusion:
    Time Complexity:
        O(n), due to hitting each node in tree
    Space Complexity:
        O(n), due to stack call of node traversal

# cleaner solution
def tree_height(root: TreeNode) -> int:
    if not root:
        return -1
    return 1 + max(tree_height(root.left), tree_height(root.right))
"""

