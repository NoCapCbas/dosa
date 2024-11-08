"""
Merge Sort


 Time Complexity:
    o(nlogn)

 Space Complexity:
    o(n)

"""

def merge_sort(arr:list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[:mid]


    left_half = merge_sort(left_half) 
    right_half =  merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


