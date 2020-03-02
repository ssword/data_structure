from doubly_linked_list import DoublyLinkedList, DoublyLinkedListIterator


class Stack:
    def __init__(self):
        self.stack_list = DoublyLinkedList()

    @property
    def size(self):
        return self.stack_list.size

    @property
    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.stack_list.add_last(element)

    def pop(self):
        if self.is_empty:
            raise Exception("Empty Stack")
        return self.stack_list.remove_last()

    def peek(self):
        if self.is_empty:
            raise Exception("Empty Stack")
        return self.stack_list.peek_first()

    def __iter__(self):
        return DoublyLinkedListIterator(self.stack_list.head)
