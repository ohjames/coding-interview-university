class Empty(Exception):
    pass

class QueueLinkedList:
    class _Node:
        __slots__ = '_value', '_next'
        def __init__(self, value, next):
            self._value = value
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        newest = self._Node(value, None)
        if self._head is None:
            self._head = newest
            self._tail = newest
            return
        current = self._tail
        current._next = newest
        self._tail = newest
        self._size += 1
    
    def dequeue(self):
        if self._head is None:
            raise Empty('Queue is empty')
        answer = self._head._value
        if self._head == self._tail:
            self._head = None
            self._tail = None
            return answer
        self._head = self._head._next
        self._size -= 1
        return answer

    def is_empty(self):
        return self._size == 0

class QueueArray:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * QueueArray.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def enqueue(self, value):
        if self._size == len(self._data):
            return "Queue is full"
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = value
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def empty(self):
        return self._size == 0

    def full(self):
        return self._size == len(self._data)