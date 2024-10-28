"""
## Problem 1: Design a Simple Printer Queue

"""
actions = [
    ("add", "doc1"),    # Add 'doc1' to the queue
    ("add", "doc2"),    # Add 'doc2' to the queue
    ("print",),         # Print 'doc1'
    ("cancel", "doc1"), # Attempt to cancel 'doc1' (already printed, so no effect)
    ("add", "doc3"),    # Add 'doc3' to the queue
    ("print",),         # Print 'doc2'
    ("print",)          # Print 'doc3'
]

def printer_queue(actions:list):
    import queue
    q = queue.Queue()
    printed = []
    for instruction in actions:
        if instruction[0] == "add":
            q.put(instruction[1])
        if instruction[0] == "cancel":
            pass
        if instruction[0] == "print":
            printed.append(q.get())
    return printed



result = printer_queue(actions)
# Verify
print(result == ['doc1', 'doc2', 'doc3'])

