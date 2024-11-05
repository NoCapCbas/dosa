Use the Engineering method to solve all problems.

## Problem 1: Design a Simple Printer Queue
The printer can only handle one operation at a time and processes print jobs in the order they were added to the queue (FIFO: First-In-First-Out).

You are given an actions list, where each element is a tuple representing a command. The commands are as follows:

Add a document to the queue:
("add", "document_name")
Example: ("add", "doc1") adds "doc1" to the print queue.
Print the next document in the queue:
("print",)
This removes and prints the first document in the queue.
Cancel a document in the queue:
("cancel", "document_name")
If the specified document exists, remove it from the queue. If it’s not present, do nothing.
Function Requirements
The function should return a list of strings representing the documents in the order they were printed.

Example Input and Output
Input:

```python
actions = [
    ("add", "doc1"),    # Add 'doc1' to the queue
    ("add", "doc2"),    # Add 'doc2' to the queue
    ("print",),         # Print 'doc1'
    ("cancel", "doc1"), # Attempt to cancel 'doc1' (already printed, so no effect)
    ("add", "doc3"),    # Add 'doc3' to the queue
    ("print",),         # Print 'doc2'
    ("print",)          # Print 'doc3'
]
```
Output:
```python
['doc1', 'doc2', 'doc3']
```
Hint:
Why use a Queue?
A queue follows the First-In-First-Out (FIFO) principle, which ensures that documents are printed in the same order they were added.
In contrast, a stack follows the Last-In-First-Out (LIFO) principle, which would result in documents being printed in reverse order.
This problem uses a queue because documents should be processed in the order they were submitted.

## Problem 2: Valid Parentheses
Given a string containg the only the following characters:
'{}[]()'
Determine if the input string is valid.
Open brackets must be closed and in the correct order.
### Example 1:
input: "()" 
output: True
### Example 2:
input: "()[]{}"
output: True
### Example 3:
input: "(]" 
output: False
### Example 4:
input: "([)]"
output: False

## Problem 3: Remove outermost Parentheses
Given a string remove the outermost Parentheses
### Example 1:
input: "(()())"
output: "()()"
### Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"

## Problem 4: Backspace String Compare
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.


### Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

### Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

### Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

 
