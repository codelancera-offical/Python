from my_dsa.DS_Node import Node

class UnorderedList:

    def __init__(self, lst=None):
        self._head = None
        if lst is not None and isinstance(lst, list):
            for item in lst:
                self.add(item)

    def is_empty(self):
        return self._head == None
    
    def add(self, item):
        temp = Node(item)
        temp.next = self._head
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count
    
    def __contains__(self, item):
        current = self._head
        while current != None:
            if current.data == item:
                return True
        
        return False

    def remove(self, item):
        current = self._head
        previous = None

        item_exist = False
        item_delete_number = 0

        while current is not None:
            if current.data == item:
                item_exist = True
                item_delete_number += 1
                if previous is None:
                    self._head = current.next
                    current = self._head
                    continue
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next

        if item_exist == False:
            raise ValueError(f"{item} is not in the list. ")
        else:
            print(f"Successfully delete {item_delete_number} \"{item}s\".")

    def to_list(self):
        current = self._head
        new_list = []
        while current is not None:
            new_list.append(current.data)
            current = current.next

        return new_list

    def slice(self, start, stop):
        new_list = []
        index_now = 0
        current = self._head

        if stop > self.size():
            return 'stop_index out of bound'
        
        while index_now != start:
            current = current.next
            index_now += 1

        while index_now < stop:
            new_list.append(current.data)
            current = current.next
            index_now += 1

        return new_list
    



        
    