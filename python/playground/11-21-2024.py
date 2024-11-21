
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n+2)

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)


def reverse_linked_list(node):
    curr = node
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

ll = ListNode(1, ListNode(2, ListNode(3)))
# print(reverse_linked_list(ll))

def remove_target_in_linked_list(node, target):
    sentinel = ListNode('x')
    sentinel.next = node
    prev, curr = sentinel, node

    while curr:
        if curr.value == target:
            prev.next = curr.next

        prev = curr
        curr = curr.next

    return sentinel.next

# print(remove_target_in_linked_list(ll, 1))






