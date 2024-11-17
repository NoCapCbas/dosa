"""
Bunny Ear Pairs


"""

def bunnyEars(num:int):
    if num == 0:
        return 0

    result = bunnyEars(num-1)
    return result + 2


print(bunnyEars(3) == 6)
print(bunnyEars(5) == 10)
