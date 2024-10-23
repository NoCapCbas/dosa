Use the Engineering method to solve all problems.

## Problem 1:
Given two parameters x and y, which are integers. Genderate a 
linked list with x nodes of value y

### Example 1:

Input: 3,2 
Output: 2 -> 2 -> 2 -> None 

### Example 2:

Input: 6,3 
Output: 3 -> 3 -> 3 -> 3 -> 3 -> 3 -> None 



## Problem 2:
Create a linked list cycle, this should cause a recursion error when done correctly.

### Example 1:
input: 1 -> 2 -> 3 -> None
output:
1 -> 2
^   
  \  |
    3
Verify:
    The test should check for RecursionError

## Problem 3:
Multiply the value in each node by the value in the next node. 
The tail node has no next node so multiply it by itself

### Example 1:
input: 1 -> 2 -> 3 -> 4 -> None 
output: 2 -> 6 -> 12 -> 16 -> None 

## Problem 4:
Given a linked list, return the number of values that occur twice.

### Example 1:
head = 1 -> 2 -> 2 -> 3 -> 3 -> None
numPairs(head) == 1


