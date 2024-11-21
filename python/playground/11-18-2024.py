
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

def reverse_ll(node):
    curr = node
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def test_reverse_ll():
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    print(f"{ll1}, {reverse_ll(ll1)}")

def remove_target_in_ll(node, target):
    sentinel = ListNode('x')
    sentinel.next = node
    prev, curr = sentinel, node
    while curr:
        if curr.value == target:
            prev.next = curr.next
        prev = curr
        curr = curr.next
    return sentinel.next

# def remove_target_in_ll(head, target):
#     # Create a sentinel node that points to the head
#     sentinel = ListNode(0)
#     sentinel.next = head
#
#     # Initialize previous and current pointers
#     prev, current = sentinel, head
#
#     while current:
#         if current.value == target:
#             # Remove the current node by updating the next pointer of the previous node
#             prev.next = current.next
#             break  # Remove only the first occurrence. Remove this line to delete all occurrences.
#         prev = current
#         current = current.next
#
#     # Return the new head (which might be different if the original head was removed)
#     return sentinel.next



def test_remove_target_in_ll():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    new_head = remove_target_in_ll(head, 3)
    print(new_head)  # Output: [1, 2, 4]

# Test case 2: Remove the head node
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    new_head = remove_target_in_ll(head, 1)
    print(new_head)  # Output: [2, 3, 4]

# Test case 3: Remove a non-existent node
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    new_head = remove_target_in_ll(head, 5)
    print(new_head)  # Output: [1, 2, 3, 4]

# Test case 4: Remove the only node in the list
    head = ListNode(1)
    new_head = remove_target_in_ll(head, 1)
    print(new_head)  # Output: []

# Test case 5: Empty list
    head = None
    new_head = remove_target_in_ll(head, 1)
    print(new_head)  # Output: []

def bubble_sort(arr):
    """
    1,2,3
    0,1,2
    i
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

if __name__ == "__main__":
    test_remove_target_in_ll()
