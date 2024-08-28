from my_dsa.DS_DNode import DNode

class Deque:
    """Deque implementation as a list"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)
    
    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()
    
    def remove_rear(self):
        return self._items.pop(0)
    
    def size(self):
        return len(self._items)
    
    def peek_rear(self):
        return self._items[0]
    
    def peek_front(self):
        return self._items[-1]
    

class DequeL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def add_front(self, item):
        new_node = DNode(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def add_rear(self, item):
        new_node = DNode(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self.tail = new_node
        self._size += 1

    def remove_front(self):
        if self._is_empty():
            raise IndexError("remove front from empty deque")
        removed_item = self.head.data
        self._head = self._head.next
        if self._head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return removed_item

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Remove rear from empty deque")
        removed_item = self._tail.data
        self.tail = self.tail.prev
        if self._tail is not None:
            self._tail.next = None:
        else:
            self.head = None