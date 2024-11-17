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
def test_fib()

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




if __name__ == "__main__":
    test_delete_target_linked()
