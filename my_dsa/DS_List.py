
class List():

    # magic methods to cooperate with python inner functions and operators
    def __init__(self):
        self.lst = []

    def __len__(self):
        return len(self.lst)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.lst[index]
        else:
            return self.lst[index]
    
    def __setitem__(self, index, value):
        self.lst[index] = value
    
    def __delitem__(self, index):
        del self.lst[index]

    def __iter__(self):
        return iter(self.lst)
    
    def __contains__(self, value):
        return value in self.lst
    
    def __repr__(self):
        return f"List({self.lst})"
    
    def __str__(self):
        return str(self.lst)
    
    # max/min function
    def max(self, fastest=True):
        if fastest == True:
            return max(self.lst) if self.lst else None
        else:
            # self-made --recursion
            # base 1
            if len(self.lst) == 1:
                return self.lst[0]
            # base 2
            elif len(self.lst) == 2:
                return self.lst[0] if self.lst[0] > self.lst[1] else self.lst[1]
            # Recursion
            else:
                return self.lst[0] if self.lst[0] > max(self.lst[1:]) else max(self.lst[1:])
    
    def min(self):
        return min(self.lst) if self.lst else None
    
    def index(self, value):
        return self.lst.index(value)
    
    # element operator
    def append(self, value):
        self.lst.append(value)

    def pop(self, index = -1):
        return self.lst.pop(index) if self.lst else None
    
    def insert(self, index, value):
        self.lst.insert(index, value)

    def clear(self):
        self.lst.clear()

    # search algorithmbn
    def binary_search(lst, item, rec=False):

        if rec == True:
            if len(lst) == 0:
                return False
            midpoint = len(lst) // 2
            if lst[midpoint] == item:
                return midpoint
            elif item < lst[midpoint]:
                return binary_search(lst[:midpoint], item, rec=True)
            else:
                return binary_search(lst[midpoint+1:], item, rec=True)
            
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
    
    def ternary_search(lst, item, rec=False):

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
                return ternary_search(lst[:midpoint1], item, rec=True)
            elif item > lst[midpoint2]:
                return ternary_search(lst[midpoint2+1:], item, rec=True)
            else:
                return ternary_search(lst[midpoint2+1:midpoint2], item)