from my_dsa.DS_Node import Node

class Stack:
    """
    Inplement by list:
        - Top is at the end of the list
    """
    def __init__(self):
        self._items = []


    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def peek(self):
        try:
            return self._items[-1]
        except:
            return 'The stack is empty'

    def pop(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


class StackL:
    """
    Stack by LinkList
    """
    def __init__(self):
        self._head = None
        self._size = 0
    
    def is_empty(self):
        return self._head == None
    
    def push(self, item):
        temp = Node(item)
        temp.next = self._head
        self._head = temp
        self._size += 1

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            return self._head.data
        
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            data = self._head.data
            self._head = self._head.next
            self._size -= 1
            return data
        
    def size(self):
        return self._size




