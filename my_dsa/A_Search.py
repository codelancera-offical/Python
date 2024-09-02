from my_dsa.DS_Node import Node

# List Search

def list_search(lst, item, ordered=False):
    """
    if item exist in lst, return its pos
    else return false
    equal to if item in list:
    """
    if ordered == False:
        pos = 0

        while pos < len(lst):
            if lst[pos] == item:
                return pos
            pos += 1
        
        return False
    
    elif ordered == True:
        pos = 0
        while pos < len(lst) and lst[pos] <= item:
            if lst[pos] == item:
                return pos
            else:
                pos += 1

        return False
    
def list_max(lst):
    """
    equal to list.max()
    """
    # base 1
    if len(lst) == 1:
        return lst[0]
    # base 2
    elif len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    # Recursion
    else:
        return lst[0] if lst[0] > list_max(lst[1:]) else list_max(lst[1:])
    
def list_binarySearch(lst, item, rec=False):

    if rec == True:
        if len(lst) == 0:
            return False
        midpoint = len(lst) // 2
        if lst[midpoint] == item:
            return midpoint
        elif item < lst[midpoint]:
            return list_binarySearch(lst[:midpoint], item, rec=True)
        else:
            return list_binarySearch(lst[midpoint+1:], item, rec=True)
        
    elif rec == False:
        first = 0
        last = len(lst) - 1

        while first <= last:
            midpoint = (first + last) // 2
            if lst[midpoint] == item:
                return True
            else:
                if item < lst[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
    
        return False

def list_ternarySearch(lst, item, rec=False):

    if rec == True:
        if len(lst) == 0:
            return False
        
        midpoint1 = len(lst) // 3
        midpoint2 = 2 * midpoint1

        if lst[midpoint1] == item:
            return True
        elif lst[midpoint2] == item:
            return True
        elif item < lst[midpoint1]:
            return list_ternarySearch(lst[:midpoint1], item, rec=True)
        elif item > lst[midpoint2]:
            return list_ternarySearch(lst[midpoint2+1:], item, rec=True)
        else:
            return list_ternarySearch(lst[midpoint2+1:midpoint2], item)
        
        



# LinkList Search
def linklist_search(item, node):
    # base
    if item == node.data():
        return True 
    # recursion
    else:
        return linklist_search(item, node.next)
    
def linklist_max(item, node):
    if node is None:
        return None
    else:
        max = node.data
        node = node.next

        current = node
        while current is not None:
            if current.data > max:
                max = current.data

        return max
    
def linklist_lastData(node):
    if node.next != None:
        return linklist_lastData(node.next)
    else:
        return node.data







