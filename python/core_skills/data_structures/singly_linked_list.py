"""
Singly Linked List implementation
"""

class Node: 
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        # dummy node, always remains head
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index:int) -> int: 
        """
        Gets value based on index passed
        """
        counter = 0
        current_node = self.head.next
        while current_node:
            if counter == index:
                return current_node.value

            current_node = current_node.next 
            counter += 1
        return -1 # index out of bounds
     
    def insertHead(self, value:int) -> None:
        """
        Inserts value into first position index or head
        """
        # update head node
        new_node = Node(value, self.head.next)
        self.head.next = new_node
        # update tail node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, value:int) -> None:
        # points current tail to new node
        self.tail.next = Node(value)
        # set new tail 
        self.tail = self.tail.next

    def remove(self, index:int) -> bool:
        counter = 0
        current_node = self.head
        while counter < index and current_node:

            current_node = current_node.next 
            counter += 1
        if current_node and current_node.next:
            if current_node.next == self.tail:
                self.tail == current_node
            current_node.next = current_node.next.next
            return True
        return False

    def getValues(self) -> List[int]:

        current_node = self.head.next
        result = []
        while current_node:
            result.append(current_node)
            current_node = current_node.next
        return result
