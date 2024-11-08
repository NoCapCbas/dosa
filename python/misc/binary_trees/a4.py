"""
Find Only Children

Given a binary tree:
                 1
                / \
               7   3
              / \   \
             4   5   4

returns [3]

Explore:
    - where do we start?
        - root node
    - how do we move?
        - recursively, returning only childs
    - what are the boundaries?
        - node is None
    - what is the action?
        return only list of parents nodes w/ only one child

Brainstorm:
    - Approach 1:
        base case, return empty list

        check left, check right
        if only left or only right exists 
            return current node value
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_only_children(node:TreeNode) -> list[int]:
    # base case return []
    if node is None:
        return None

    left_child = find_only_children(node.left) 
    right_child = find_only_children(node.right)
    if left_child is None and right_child is not None:
        return right_child + [node.value]
    elif right_child is None and left_child is not None:
        return left_child + [node.value]

    return left_child + right_child   

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

