from my_dsa.DS_Node import Node
class OrderedList:
    def __init__(self, lst=None):
        self._head = None
        if lst is not None and isinstance(lst, list):
            for item in lst:
                self.add(item)


    def __contains__(self, item):
        current = self._head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False

    def add(self, item):
        current = self._head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self._head
            self._head = temp
        else:
            temp.next = current
            previous.next = temp
        
    def is_empty(self):
        return self._head is None
    
    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count
    
    def to_list(self):
        lst = []
        current = self._head
        while current is not None:
            lst.append(current.data)
            current = current.next
        
        return lst
    
    
