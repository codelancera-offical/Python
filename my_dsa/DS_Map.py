class HashTable:
    def __init__(self, size = 31, collision_solution="linear"):
        self._size = size   # 11, 17, 31
        self._slots = [None] * self._size   # store the key
        self._data = [None] * self._size
        self._collision_solution = "linear"

    def put(self, key, data):
        hash_value = self.hash_function(key, self._size)

        if self._slots[hash_value] is None:
            self._slots[hash_value] = key
            self._data[hash_value] = data
        else:
            if self._slots[hash_value] == key:
                self._data[hash_value] = data   # replace
            else:
                rehash_times = 1
                next_slot = self.rehash(hash_value, self._size, self._collision_solution, rehash_times)

                while self._slots[next_slot] is not None and self._slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, self._size, self._collision_solution)
                    rehash_times += 1
                
                if self._slots[next_slot] is None:
                    self._slots[next_slot] = key
                    self._data[next_slot] = data
                else:
                    self._data[next_slot] = data

    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, old_hash, size:int, collision_solution:str, rehash_times:int):
        if collision_solution == "linear":
            return (old_hash + 1) % size
        elif collision_solution == "quadratic":
            return (old_hash + rehash_times**2) % size 
            
    
    def get(self, key):
        start_slot = self.hash_function(key, self._size)

        position = start_slot
        while self._slots[position] is not None:
            if self._slots[position] == key:
                return self._data[position]
            else:
                position = self.rehash(position, self._size, self._collision_solution)
                if position == start_slot:
                    return None

        return None
                
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        # h[key] = data
        self.put(key, data)

    def __repr__(self):
        return f"Slot:({self._slots})\nData:({self._data})"
