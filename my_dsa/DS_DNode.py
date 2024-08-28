class DNode:
    """A node for Doubly linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None
        self._prev = None

        if self.is_empty():
            return "Stack is Empty"
        
    def get_data(self):
        return self._data

    def set_data(self, node_data):
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, node_next):
        self._next = node_next

    next = property(get_next, set_next)

    def get_prev(self):
        return self._prev
    
    def set_prev(self, node_prev):
        self._prev = node_prev

    front = property(get_prev, set_prev)


    def __str__(self):
        return str(self._data)