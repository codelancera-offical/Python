from my_dsa.DS_Node import Node

class Queue:
    """
    Queue implementation as a list
    0 as rear
    """

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def peek_rear(self):
        return self._items[0]

    def peek_front(self):
        return self._items[-1]


class QueueX:
    """
    end as the rear
    """

    def __init__(self):
        self._items = []
        self._frontIndex = 0
        self._rearIndex = 0

    def is_empty(self):
        return self._frontIndex != self._rearIndex
    
    def enqueue(self, item):
        self._items.append(item)
        self._rearIndex += 1

    def dequeue(self):
        try:
            data = self._items[self._frontIndex]
            self._frontIndex += 1
            return data
        except IndexError:
            return 'No item in queue.'

    def size(self):
        return self._rearIndex - self._frontIndex
    

class QueueL:
    """0 as front, end as rear"""
    def __init__(self):
        self._rear = None
        self._size = 0
    
    def is_empty(self):
        return self._head == None
    
    def enqueue(self, item):
        temp = Node(item)
        temp.next = self._rear
        self._rear = temp
        self._size += 1

    def dequeue(self):
        current = self._head
        previous = None

        if current == None:
            return 'The Stack is empty'

        while current.next != None:
            previous = current
            current = current.next

        data = current.data

        if previous == None:
            self._rear = None
            self._size -= 1
            return data
        
        previous.next = None
        self._size -= 1
        return data
    
    def size(self):
        return self._size
        

        
        
