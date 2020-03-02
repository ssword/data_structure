
class DynamicArray:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.array_list = [None] * self.capacity
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _validate_index(self, index):
        if index >= self.size or index < 0:
            raise Exception("Illegal Index")

    def get(self, index):
        self._validate_index(index)

        return self.array_list[index]

    def set(self, index, value):
        # assume set will not increase the capacity of the array
        self._validate_index(index)

        self.array_list[index] = value

    def clear(self):
        for i in range(self.capacity):
            self.array_list[i] = None
        self.size = 0

    def _increase_array_size(self):
        new_capacity = self.capacity * 2
        new_array_list = [None] * new_capacity
        for i in range(self.capacity):
            new_array_list[i] = self.array_list[i]
        self.capacity = new_capacity
        self.array_list = new_array_list

    def add(self, value):
        if self.size >= self.capacity:
            self._increase_array_size()
        self.array_list[self.size] = value
        self.size += 1

    def delete(self, index):
        self._validate_index()
        for i in range(index, self.size):
            self.array_list[i] = self.array_list[i+1]
        self.size -= 1

    def remove(self, value):
        for i in range(self.size):
            if self.array_list[i] == value:
                self.delete(i)
                return None

        raise ValueError

    def index(self, value, start, end):
        if not start:
            start = 0
        if not end:
            end = self.size

        for i in range(start, end):
            if self.array_list[i] == value:
                return i
        raise ValueError
