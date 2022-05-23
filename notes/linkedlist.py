
class Empty(Exception):
    pass

class SingleLinkedList:
    class _Node:
        __slots__ = '_value', '_next'
        def __init__(self, value, next):
            self._value = value
            self._next = next
        
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def __getitem__(self, i):
        current = self._head
        count = 0
        while current:
            if count == i:
                return current._value
            count += 1
            current = current._next
        assert(False)
        return 0

    def prepend(self, value):
        newest = self._Node(value, self._head)
        newest._next = self._head
        self._head = newest
        self._size += 1

    def pop_front(self):
        if self._head is None:
            raise Empty('Linked List is empty')
        answer = self._head._value
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def append(self, value):
        newest = self._Node(value, None)
        if self._head is None:
            self._head = newest
            return
        last = self._head
        while last._next:
            last = last._next
        last._next = newest

    # def pop_back(self):
    #     if self.is_empty():
    #         raise Empty('Linked List is empty')
    #     answer = self._tail._value
    #     self._tail = self._head._next
    #     self._size -= 1
    #     return answer

    def front(self):
        if self.is_empty():
            raise Empty('Linked List is empty')
        return self._head._value

    # def back(self):
    #     if self.is_empty():
    #         raise Empty('Linked List is empty')
        

    def insert(self, i, value):
        current = self._head
        count = 0
        while current:
            if count == i:
                newest = self._Node(value, current._next)
                current._next = newest
        assert(False)
        


    # def delete(self, i):
    #     pass

    def reverse(self):
        pass

    def remove(self, value):
        pass