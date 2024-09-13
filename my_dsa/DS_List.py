from my_math.Probability import *


class List():

    # magic methods to cooperate with python inner functions and operators
    def __init__(self, lst=None, random=False, **kwargs):
        if lst == None:
            if random == False:
                self.lst = []
            elif random == True:
                self.lst = []
                low = kwargs.get('low', 0)
                high = kwargs.get('high', 10)
                n = kwargs.get('n', 10)
                for i in range(n):
                    self.lst.append(generate_random_int(low=low, high=high))
        elif isinstance(lst, list):
            self.lst = lst.copy()
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
    def max_index(lst): # OK
        max_index = 0
        max_item = lst[0]

        for i in range(1, len(lst)):
            if max_item < lst[i]:
                max_index = i
                max_item = lst[i]

        return max_index
        
    @staticmethod
    def min_index(lst): # OK
        min_index = 0
        min_item = lst[0]

        for i in range(1, len(lst)):
            if min_item > lst[i]:
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

    def flip(self, k):  # OK
        return self.lst[:k][::-1] + self.lst[k:]
    
    def reverse(self):
        self.lst = self.lst.reverse()

    def copy(self):
        return List(self.lst)
    # search algorithm
    def binary_search(lst, item, rec=False):    # Modifying

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
    
    def ternary_search(lst, item, rec=False):   # Modifying

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
    def frisbee_sort(self, desc=False) -> None: # OK
        if desc == False:
            n = len(self.lst)
            for size in range(n, 1, -1):
                max_index = self.lst.index(max(self.lst[:size]))

                if max_index != size - 1:
                    if max_index != 0:
                        self.lst = List.flip(self, max_index + 1)
                    
                    self.lst = List.flip(self, size)
        elif desc == True:
            n = len(self.lst)
            for size in range(n, 1, -1):
                min_index = self.min_index(self.lst[:size])

                if min_index != size - 1:
                    if min_index != 0:
                        self.lst = List.flip(self, min_index + 1)

                    self.lst = List.flip(self, size)

    def select_sort(self, desc=False):  # OK
        if desc == False:
            n = len(self.lst)
            for size in range(n, 1, -1):
                max_index = self.max_index(self.lst[:size])
                
                temp = self.lst[size-1]
                self.lst[size-1] = self.lst[max_index]
                self.lst[max_index] = temp
        elif desc == True:
            n = len(self.lst)
            for size in range(n, 1, -1):
                min_index = self.min_index(self.lst[:size])

                temp = self.lst[size - 1]
                self.lst[size - 1] = self.lst[min_index]
                self.lst[min_index] = temp

    def bubble_sort(self, desc=False) -> None:  # OK
        if desc == False:
            n = len(self.lst)
            for i in range(n-1, 0, -1):
                for j in range(i):
                    if self.lst[j] > self.lst[j + 1]:
                        temp = self.lst[j]
                        self.lst[j] = self.lst[j+1]
                        self.lst[j+1] = temp

        elif desc == True:
            n = len(self.lst)
            for i in range(n-1):
                for j in range(n-1, i, -1):
                    if self.lst[j] > self.lst[j - 1]:
                        temp = self.lst[j]
                        self.lst[j] = self.lst[j - 1]
                        self.lst[j-1] = temp

    def insert_sort(self, desc=False) -> None:  # OK
        n = len(self.lst)

        if desc == False:
            for i in range(1, n):
                cur_val = self.lst[i]
                cur_pos = i

                while cur_pos > 0 and self.lst[cur_pos - 1] > cur_val:
                    self.lst[cur_pos] = self.lst[cur_pos - 1]
                    cur_pos -= 1
                self.lst[cur_pos] = cur_val

        elif desc == True:
            for i in range(1, n):
                cur_val = self.lst[i]
                cur_pos = i

                while cur_pos > 0 and self.lst[cur_pos - 1] < cur_val:
                    self.lst[cur_pos] = self.lst[cur_pos - 1]
                    cur_pos -= 1
                self.lst[cur_pos] = cur_val

    ## Faster algorithm (usually O(nlogn) or less than O(n^2)) 
    def merge_sort(self):   # OK
        def mergeSort(lst):
            if len(lst) > 1:
                mid = len(lst) // 2
                left_half = lst[:mid]
                right_half = lst[mid:]

                mergeSort(left_half)
                mergeSort(right_half)

                i, j, k = 0, 0, 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] <= right_half[j]:
                        lst[k] = left_half[i]
                        i += 1
                    else:
                        lst[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    lst[k] = left_half[i]
                    i += 1
                    k += 1
                
                while j < len(right_half):
                    lst[k] = right_half[j]
                    j += 1
                    k += 1

        mergeSort(self.lst)

    def quick_sort(self):
        def quickSort(lst):
            def partition(lst, first, last):
                pivot_val = lst[first]
                left_mark = first + 1
                right_mark = last
                done = False

                while not done:
                    while left_mark <= right_mark and lst[left_mark] <= pivot_val:
                        left_mark += 1

                    while left_mark <= right_mark and lst[right_mark] >= pivot_val:
                        right_mark -= right_mark

                    if right_mark < left_mark:
                        done = True
                    
                    else:
                        lst[left_mark], a
            def quickSort_helper(lst, first, last):
                if first < last:
                    split = partition(lst, )

        
    def shell_sort(self, desc=False):   # modifying
        """
        improvement of insert_sort
        using the advantage of insert_sort that the more order the list is, the faster the algorithm will be.
        best: O(n)
        worst: O(n^2)
        average: O(n^1.3)
        """
        def gap_insertion_sort(lst, start, gap, desc):
            if desc == False:
                for i in range(start + gap, len(lst), gap):
                    cur_val = lst[i]
                    cur_pos = i
                    while cur_pos >= gap and lst[cur_pos - gap] > cur_val:
                        lst[cur_pos] = lst[cur_pos - gap]
                        cur_pos = cur_pos - gap
                    lst[cur_pos] = cur_val
            elif desc == True:
                for i in range(start + gap, len(lst), gap):
                    cur_val = lst[i]
                    cur_pos = i
                    while cur_pos >= gap and lst[cur_pos - gap] < cur_val:
                        lst[cur_pos] = lst[cur_pos - gap]
                        cur_pos = cur_pos - gap
                    lst[cur_pos] = cur_val
 
        sublist_count = len(self.lst) // 2
        while sublist_count > 0:
            for pos_start in range(sublist_count):
                gap_insertion_sort(self.lst, pos_start, sublist_count, desc)
            # print("After increments of size", sublist_count, "the list is ", self.lst)
            sublist_count = sublist_count // 2
        
        print(self.lst)





