# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else: 
        max = find_max(lst[1:])
        return max if max > lst[0] else lst[0]
    pass


print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45