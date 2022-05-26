
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
        if not 0 <= i < self._size:
            raise IndexError('invalid index')
        while current:
            if count == i:
                return current._value
            count += 1
            current = current._next

    def prepend(self, value):
        newest = self._Node(value, self._head)
        newest._next = self._head
        self._head = newest
        if self._tail is None:
            self._tail = newest
        self._size += 1

    def pop_front(self):
        if self._head is None:
            raise Empty('Linked List is empty')
        answer = self._head._value
        if self._head == self._tail:
            self._head = None
            self._tail = None
            return answer
        self._head = self._head._next
        self._size -= 1
        return answer
    
    def append(self, value):
        newest = self._Node(value, None)
        if self._head is None:
            self._head = newest
            self._tail = newest
            return
        current = self._tail
        current._next = newest
        self._tail = newest
        self._size += 1
        # current = self._head
        # while current._next:
        #     current = current._next
        # current._next = newest
        # self._tail = newest
        # self._size += 1

    def pop_back(self):
        if self.is_empty():
            raise Empty('Linked List is empty')
        answer = self._tail._value
        if self._head == self._tail:
            self._head = None
            self._tail = None
            return answer
        current = self._head
        while current._next._next:
            current = current._next
        current._next = None
        self._tail = current
        self._size -= 1
        return answer

    def front(self):
        if self._head is None:
            raise Empty('Linked List is empty')
        return self._head._value

    def back(self):
        if self._tail is None:
            raise Empty('Linked List is empty')
        return self._tail._value

    def insert(self, i, value):
        current = self._head
        count = 0
        while current:
            if count == i:
                newest = self._Node(value, current._next)
                current._next = newest
                self._size += 1
                break
            current = current._next
            count += 1

    def delete(self, i):
        if self._head is None:
            raise Empty('Linked List is empty')
        if self._head == self._tail:
            answer = self._head
            self._head = None
            self._tail = None
            return answer
        current = self._head
        prev = self._head
        temp = self._head
        count = 0
        while current:
            if count == i:
                temp = current._next
                break
            prev = current
            current = current._next
            count += 1
        prev._next = temp
        self._size -= 1
        return prev
            
    def value_n_from_end(self, n):
        if n > self._size:
            raise IndexError('n is outside LinkedList size')
        current = self._head
        for i in range(0, self._size - n):
            current = current._next
        return current._value

    def reverse(self):
        current = self._head
        prev = None
        while current:
            self._next = current._next
            current._next = prev
            prev = current
            current = self._next
        self._head = prev

    def remove(self, value):
        if self._head is None:
            raise Empty('Linked List is empty')
        current = self._head
        if current is not None:
            if current._value == value:
                self._head = current._next
                current = None
                self._size -= 1
                return
        temp = self._head
        while current:
            if current._value == value:
                break
            temp = current
            current = current._next
        if current is None:
            return 'Linked List does not have value'
        temp._next = current._next
        current = None
        self._size -= 1