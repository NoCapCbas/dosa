# reversal
# deletion, target removal
# etc...

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_fib():
    # Test cases
    print(f"fib(0) == {fib(0)}")  # Base case, should return 0
    print(f"fib(1) == {fib(1)}")  # Base case, should return 1
    print(f"fib(2) == {fib(2)}")  # Should return 1
    print(f"fib(3) == {fib(3)}")  # Should return 2
    print(f"fib(5) == {fib(5)}")  # Should return 5
    print(f"fib(10) == {fib(10)}")  # Should return 55
    print(f"fib(15) == {fib(15)}")  # Should return 610

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def reverse_linked(node:ListNode) -> ListNode:
    """
    Reverse linked list
    """
    curr = node
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# test cases
def test_reverse_linked():
    """
    Test Reverse Linked List
    """
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(reverse_linked(ll1))

def delete_target_linked(node:ListNode, target:int) -> ListNode:
    """
    Delete target in linked list
    Target: 3
    1 -> 2 -> 3 -> None
    """
    # create a sentinel node
    sentinel = ListNode('x')
    # assign sentinel node next to head
    sentinel.next = node
    # set current as sentinel
    curr = sentinel
    # loop while curr.next is not None
    while curr.next is not None:
        # if currents next value is target
        if curr.next.value == target:
            # set currents next to currents next next
            curr.next = curr.next.next
            # break early if only removing one item
        else:
            # else regular iteration to next
            curr = curr.next   
    # return sentinels next, which is head
    return sentinel.next

def test_delete_target_linked():
    """
    Test Delete target in linked list
    """
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(delete_target_linked(ll1, 3))
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(delete_target_linked(ll1, 2))
    ll1 = None 
    print(delete_target_linked(ll1, 3))

def count_elements_in_linked_list(node:ListNode):
    curr = node
    count = 0
    while curr:
        curr = curr.next
        count += 1
    return count

def test_count_elements_in_linked_list():
    test_input = ListNode(1)
    out = count_elements_in_linked_list(test_input)
    print(f"1 == {out}, {1 == out}")

    test_input = None
    out = count_elements_in_linked_list(test_input)
    print(f"0 == {out}, {0 == out}")

    test_input = ListNode(1, ListNode(2, ListNode(3)))
    out = count_elements_in_linked_list(test_input)
    print(f"3 == {out}, {3 == out}")

def sum_elements_in_linked_list(node):
    curr = node
    total = 0
    while curr:
        total += curr.value
        curr = curr.next
    return total

def test_sum_element_in_linked_list():
    test_input = ListNode(1)
    out = sum_elements_in_linked_list(test_input)
    print(f"1 == {out}, {1 == out}")

    test_input = None
    out = sum_elements_in_linked_list(test_input)
    print(f"0 == {out}, {0 == out}")

    test_input = ListNode(1, ListNode(2, ListNode(3)))
    out = sum_elements_in_linked_list(test_input)
    correct_output = 6
    print(f"{correct_output} == {out}, {correct_output == out}")

def fib2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def reverse_linked_list2(node):
    curr = node
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# test cases
def test_reverse_linked2():
    """
    Test Reverse Linked List
    """
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(reverse_linked_list2(ll1))

def remove_target_from_linked_list(node, target):
    sentinel = ListNode('x')
    sentinel.next = node
    curr = sentinel
    
    while curr.next is not None:
        if curr.next.value == target:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return sentinel.next

def test_remove_target_from_linked_list_2():
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(remove_target_from_linked_list(ll1, 3))
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(remove_target_from_linked_list(ll1, 2))
    ll1 = None 
    print(remove_target_from_linked_list(ll1, 3))

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # Recursive representation for full subtree
        left_repr = repr(self.left) if self.left else 'None'
        right_repr = repr(self.right) if self.right else 'None'
        return f"{self.value} -> (Left: {left_repr}, Right: {right_repr})"

def count_elements_in_binary_tree(node):
    if node is None:
        return 0
    
    left_total = count_elements_in_binary_tree(node.left)
    right_total = count_elements_in_binary_tree(node.right)

    return left_total + right_total + 1 

def test_count_elements_in_binary_tree():
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    print(count_elements_in_binary_tree(tree) == 3)
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    print(count_elements_in_binary_tree(tree) == 4)
    tree = None 
    print(count_elements_in_binary_tree(tree) == 0)

def find_max_element_in_tree(node):
    if node is None:
        return float('-inf')

    left_result = find_max_element_in_tree(node.left)
    right_result = find_max_element_in_tree(node.right)

    return max(left_result, right_result, node.value)
def test_find_max_element_in_tree():
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    print(find_max_element_in_tree(tree) == 3)
    tree = None 
    print(find_max_element_in_tree(tree) == float('-inf'))
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    print(find_max_element_in_tree(tree) == float('-inf'))



if __name__ == "__main__":
    test_count_elements_in_binary_tree()
