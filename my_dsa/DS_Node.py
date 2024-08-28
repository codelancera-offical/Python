class Node:
    """A node of a Linked List"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

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

    def __str__(self):
        return str(self._data)