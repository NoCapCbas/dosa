"""
Find Most Frequent Node Value
Given a binary tree:
                 1
                / \
               7   3
              / \
             4   3
// returns 3


Explore:
    - where do we start?
        - root node
    - how do we move?
        - recursively through node.left, node.right
    - what are the boundaries?
        - node is none
    - what is the action?
        - return freq_map

Brainstorm:
    - Approach 1:
        - helper function to return freq_map
        - base case, return pass freq_map

Plan:



Implement:
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def most_freq_node_val(node:TreeNode) -> int:
    # recursively, w/helper
    def helper(node, freq_map):
        if node is None:
            return freq_map

        freq_map[node.value] = freq_map.get(node.value, 0) + 1
        freq_map = helper(node.left, freq_map)
        freq_map = helper(node.right, freq_map) 

        return freq_map

    freq_map = helper(node, {})
    max_val = float('-inf')
    for key, val in freq_map.items():
        if val > max_val:
            max_val = key
    return max_val


# Verify Test Cases
print(most_freq_node_val(None), float('-inf'))
print(most_freq_node_val(TreeNode(1, TreeNode(3), TreeNode(3))), 3) # 3
print(most_freq_node_val(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(2, None, TreeNode(2, TreeNode(9))))), 2)
print(most_freq_node_val(TreeNode(1)), 1)

"""
Conclusion:
    Time Complexity:
        O(n), due to recursively moving to every node in tree to get counts
    Space Complexity:
        O(n), due to stack call for each node + freq_map taking O(n) 
            space to store count of value
"""
