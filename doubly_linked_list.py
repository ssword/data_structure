class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoublyLinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            value = self.current.data
            self.current = self.current.next
            return value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        traversal_point = self.head
        while traversal_point is not None:
            next_point = traversal_point.next
            traversal_point.prev = traversal_point.next = None
            traversal_point.data = None
            traversal_point = next_point
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, value):
        self.add_last(value)

    def add_first(self, value):
        if self.is_empty():
            self.head = self.tail = Node(data=value)
        else:
            self.head.prev = Node(data=value, next=self.head)
            self.head = self.head.prev

        self.size += 1

    def add_last(self, value):
        if self.is_empty():
            self.head = self.tail = Node(data=value)
        else:
            self.tail.next = Node(data=value, prev=self.tail)
            self.tail = self.tail.next

        self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.tail.data

    def remove_last(self):
        if self.is_empty():
            raise Exception("Empty list")

        last_data = self.tail.data

        self.tail = self.tail.prev
        self.size -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None

        return last_data

    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty list")

        first_data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None

        return first_data

    def remove_node(self, node):
        if not node.prev:
            self.remove_first()
        if not node.next:
            self.remove_last()

        node_data = node.data
        node.data = None

        node.prev.next = node.next
        node.next.prev = node.prev
        node = node.next = node.prev = None

        self.size -= 1

        return node_data

    def remove_at(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range.")

        if index < (self.size / 2):
            travel_node = self.head
            for i in range(index):
                travel_node = travel_node.next
        else:
            travel_node = self.tail
            for i in range(self.size-index-1):
                travel_node = travel_node.prev

        return self.remove_node(travel_node)

    def remove(self, value):
        travel_node = self.head
        while travel_node:
            if travel_node.data == value:
                self.remove(travel_node)
                return True
            travel_node = travel_node.next

        return False

    def find_index(self, value):
        index = 0
        travel_node = self.head
        while travel_node:
            if travel_node.data == value:
                return index
            travel_node = travel_node.next
            index += 1
        return -1

    def contains(self, value):
        return self.find_index(value) != -1

    def __iter__(self):
        return DoublyLinkedListIterator(self.head)

    def to_string(self):
        string_list = list()
        travel_node = self.head
        while travel_node:
            string_list.append(travel_node.data)
            travel_node = travel_node.next
        return str(string_list)
