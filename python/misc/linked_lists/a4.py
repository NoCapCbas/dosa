""" 
Problem 4:
Given a linked list, return the number of values that occur twice.

### Example 1:
head = 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> None
numPairs(head) == 1

Brainstorm
while loop through list using freq map to count


"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def numPairs(head:Node):
    count_map = {}
    current = head
    values_with_two_count = 0
    while current:
        if current.value not in count_map:
            count_map[current.value] = 0
        count_map[current.value] += 1
       
        if count_map[current.value] == 2:
            values_with_two_count += 1
        if count_map[current.value] == 3:
            values_with_two_count -= 1

        current = current.next
    return values_with_two_count

LL1 = Node(1, Node(2, Node(2, Node(3, Node(3, Node(3))))))
print(numPairs(LL1) == 1)
LL2 = Node(1, Node(2, Node(2, Node(3, Node(3)))))
print(numPairs(LL2) == 2)


