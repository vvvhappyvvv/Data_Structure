class Stack:
    '''LIFO Stack implementation using a singly linked list for storage.'''
    class _Node(object):
        ''' a no public class to realize the node '''
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''an empty stack'''
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
         self._head = self._Node(e, self._head)
        self._size = self.size + 1

    def top(self):
        if self.is_empty():
            raise Empty('The stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('The stack is empty')
        ele = self._head._element
        self._head = self._head._next
        self._size = self._size -1
        return ele

class Queue:
    ''' FIFO queue class using the linked list'''

    class _Node(object):
        ''' a no public class to realize the node '''
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''an empty stack'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        '''return the first element in the queue'''
        if self.is_empty():
            raise Empty('The stack is empty')
        return self._head._element

    def dequeue(self):
        '''remove and return the first element of the queue'''
        if self.is_empty():
            raise Empty('The stack is empty')
        ele = self._head._element
        self._head = self._head._next
        self._size = self._size - 1
        if self.is_empty():
            self._tail = None
        return ele

    def enqueue(self, e):
        ''' add an element to the bottom of the queue '''
        new_node = self._Node(e, None) # add to the bottom so the None
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node # connect the present one to the new one
        self._tail = new_node
        self._size = self._size + 1

