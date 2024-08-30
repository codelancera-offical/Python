
def sequential_search_unordered(lst, item):
    """
    if item exist in lst, return its pos
    else return false
    """
    pos = 0

    while pos < len(lst):
        if lst[pos] == item:
            return pos
        pos += 1
    
    return False

def sequential_search_ordered(lst, item):
    """
    search on a ordered list
    """
    pos = 0

    while pos < len(lst) and lst[pos] <= item:
        if lst[pos] == item:
            return pos
        else:
            pos += 1

    return False

def binary_search(lst, item):
    if len(lst) == 0:
        return False
    midpoint = len(lst) // 2
    if lst[midpoint] == item:
        return midpoint
    elif item < lst[midpoint]:
        return binary_search(lst[:midpoint], item)
    else:
        return binary_search(lst[midpoint+1:], item)







