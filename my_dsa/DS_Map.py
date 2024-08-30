class HashTable_linear_probing:
    def __init__(self):
        self._size = 11
        self._slots = [None] * self._size
        self._data = [None] * self._size

    def put(self, key, data):
        hash_value = self.hash_function(key, self._size)

        if self._slots[hash_value] is None:
            self._slots[hash_value] = key
            self._data[hash_value] = data
        else:
            if self._slots[hash_value] == key:
                self._data[hash_value] = data   # replace
            else:
                next_slot = self.rehash(hash_value, self._size)
                while self._slots[next_slot] is not None and self._slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, self._size)
                
                if self._slots[next_slot] is None:
                    self._slots[next_slot] = key
                    self._data[next_slot] = data
                else:
                    self._data[next_slot] = data

    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def get(self, key):
        start_slot = self.hash_function(key, self._size)

        position = start_slot
        while self._slots[position] is not None:
            if 