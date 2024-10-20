"""
Dynamic Array implementation
Note: Python lists are dynamic arrays by default,
but this is an example of what's going on under the hood.
"""
class DynamicArray:

    def __init__(self, capacity:int):
        
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity
    
    def get(self, i:int) -> int:
        """
        Gets value at i-th index, O(1)
        """
        return self.arr[i]

    def set(self, i:int, n:int) -> None:
        """
        Set n at i-th index, O(1)
        """
        self.arr[i] = n

    def pushback(self, n:int) -> None:
        """
        Insert n in the last position of the array, O(n)
        """
        if self.length == self.capacity:
            self.resize()
        # insert at next empty postition
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        """
        Remove the last element in the array, O(1)
        """
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
        """
        create a new array of double capacity, O(n)

        """
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        # copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
    
    def getSize(self) -> int:
        """
        get size of array, O(1)
        """
        return self.length

    def getCapacity(self) -> int:
        """
        get capacity, O(1)
        """
        return self.capacity


