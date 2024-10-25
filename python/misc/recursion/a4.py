"""
Remove all target elements from an array, recusively
"""


def remove_target_recusively(arr:list, target:int) -> list:
    
    if len(arr) == 0:
        return arr

    value = arr.pop(0)
    if target != value:
        return [value] + remove_target_recusively(arr, target)
    return remove_target_recusively(arr, target)

assert remove_target_recusively([3,1,2,3,1], 2) [3,1,3,1]
