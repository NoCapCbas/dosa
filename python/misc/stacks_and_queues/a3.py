"""
Remove outermost parentheses


Explore:
    - similar to problem 2, valid parentheses
    - probably Time:O(n), loop through string
    and Space:O(n)


Brainstorm:
    Approach 1:
        - use map to store bracket key value mapping
        - loop through string indexes
        - store value of index 
        - if bracket in map add to queue
        - you know it is the outermost when queue is empty
        - keep track of outermost index, to remove them
        - loop through and remove stored indexes
"""

def remove_outermost_parentheses(chrs:str) -> str:
    import queue
    bracket_map = {
        "(":")",
        "[":"]",
        "{":"}",
    }
    remove_q = queue.Queue()
    q = queue.Queue() 
    for idx in range(len(chrs)):
        bracket = chrs[idx]

        if bracket in bracket_map:
            if q.empty():
                remove_q.put(idx)
            q.put(bracket_map[bracket])
        else:
            bracket_match = q.get()
            if q.empty():
                remove_q.put(idx)
    chrs_list = list(chrs)
    while not remove_q.empty():
        remove_idx = remove_q.get()
        print(remove_idx)
        chrs_list.pop(remove_idx)
    result = chrs_list.join('')
            
    return result


print(remove_outermost_parentheses("(()())") == "()()")
print(remove_outermost_parentheses("(()())(())(()(()))") == "()()()()(())")
