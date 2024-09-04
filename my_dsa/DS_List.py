
class List():

    # magic methods to cooperate with python inner functions and operators
    def __init__(self, lst=None):
        if lst == None:
            self.lst = []
        elif isinstance(lst, list):
            self.lst = lst
        else:
            raise TypeError("init error: please input a python list to init.")


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
    
    def min(self, fastest=True):
        if fastest == True:
            return min(self.lst) if self.lst else None
        else:
            # self-made --recursion
            if len(self.lst) == 1:
                return self.lst[0]
            elif len(self.lst) == 2:
                return self.lst[0] if self.lst[0] < self.lst[1] else self.lst[1]
            else:
                return self.lst[0] if self.lst[0] < min(self.lst[1:]) else min(self.lst[1:])
    
    def index(self, value):
        return self.lst.index(value)
    
    @staticmethod
    def max_index(lst):
        max_index = 0
        max_item = lst[0]

        for i in range(1, len(lst)):
            if max_item < lst[i]:
                max_index = i
                max_item = lst[i]

        return max_index
        
    @staticmethod
    def min_index(lst):
        min_index = 0
        min_item = lst[0]

        for i in range(1, len(lst)):
            if min_item < lst[i]:
                min_index = i
                min_item = lst[i]

        return min_index    
    
    # element operator
    def append(self, value):
        self.lst.append(value)

    def pop(self, index = -1):
        return self.lst.pop(index) if self.lst else None
    
    def insert(self, index, value):
        self.lst.insert(index, value)

    def clear(self):
        self.lst.clear()

    def flip(self, k):
        return self.lst[:k][::-1] + self.lst[k:]
    
    def reverse(self):
        self.lst = self.lst.reverse()

    # search algorithm
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
        else:
            first = 0
            last = len(lst) - 1
            while first <= last:
                midpoint1 = first + (last - first) // 3
                midpoint2 = last - (last - first) // 3

                if lst[midpoint1] == item or lst[midpoint2] == item:
                    return True
                elif item < lst[midpoint1]:
                    last = midpoint1 - 1
                elif item > lst[midpoint2]:
                    first = midpoint2 + 1
                else:
                    first = midpoint1 + 1
                    last = midpoint2 - 1

            return False
        
    # sort algorithm

    ## O(n^2) sort aloritem
    def frisbee_sort(self):
        n = len(self.lst)
        for size in range(n, 1, -1):
            max_index = self.lst.index(max(self.lst[:size]))

            if max_index != size - 1:
                if max_index != 0:
                    self.lst = List.flip(self, max_index + 1)
                
                self.lst = List.flip(self, size)

    def select_sort(self):
        n = len(self.lst)
        for size in range(n, 1, -1):

            max_index = self.max_index(self.lst[:size])
            
            temp = self.lst[size-1]
            self.lst[size-1] = self.lst[max_index]
            self.lst[max_index] = temp

    def bubble_sort(self):
        for i in range(len(self.lst)-1, 0, -1):
            for j in range(i):
                if self.lst[j] > self.lst[j + 1]:
                    temp = self.lst[j]
                    self.lst[j] = self.lst[j+1]
                    self.lst[j+1] = temp
                
    def insert_sort():
        pass

    ## Faster algorithm(usually O(nlogn)
    def merge_sort():
        pass

    def quick_sort():
        pass
        
    def shell_sort():
        pass



