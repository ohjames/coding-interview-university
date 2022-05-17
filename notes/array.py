import ctypes

class Empty(Exception):
    pass

class DynamicArrays:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def __getitem__(self, i):
        if not 0 <= i < self._n:
            raise IndexError('invalid index')
        return self._A[i]

    def append(self, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = value
        self._n += 1

    def insert(self, i, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, i, -1):
            self._A[j] = self._A[j - 1]
        self._A[i] = value
        self._n += 1
    
    def prepend(self, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, 0, -1):
            self._A[i] = self._A[i - 1]
        self._A[0] = value
        self._n += 1
        
    def pop(self):
        if self.is_empty():
            raise Empty('Array is empty')
        answer = self._A[self._n - 1]
        self._n -= 1
        if self._n == self._capacity / 4:
            self._resize(self._capacity / 2)
        return answer
    
    def delete(self, i):
        if self.is_empty():
            raise Empty('Array is empty')
        elif i not in range(self._n):
            raise IndexError('invalid index')
        for j in range(i, self._n - 1):
            self._A[j] = self._A[j + 1]
        self._A[self._n - 1] = None
        self._n -= 1
        if self._n == self._capacity / 4:
            self._resize(self._capacity / 2)
        
    def remove(self, value):
        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                if self._n == self._capacity / 4:
                    self._resize(self._capacity / 2)
                return
            raise ValueError('value not found')

    def find(self, value):
        if self.is_empty():
            raise Empty('Array is empty')
        for i in range(self._n):
            if self._A[i] == value:
                return i
            else:
                return 'value not found'
            
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object())