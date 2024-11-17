"""
Insertion Sort
"""

def insertion_sort(arr:list):
    # iterate through the list, starting from the second element
    for i in range(1, len(arr)):
        # the current element to be inserted
        item = arr[i]
        # initialiaze the index of the previous element
        j = i - 1
        # shift element of the sorted that are greater than the key,        # to one position, ahead of their postion
        while j >= 0 and item < arr[j]:
            arr[j+1] = arr[j] 

tests = [
    [1,6,4,2]
    [],
    [1],
    [3,7,1,8]
]

for test in tests:
    print(insertion_sort(test))


