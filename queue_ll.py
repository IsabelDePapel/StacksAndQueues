import nodes
from stack_ll import StackDLL as Stack


class QueueSLL:
    """Queue class implemented as singly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None

    def __str__(self):
        s = ""
        current = self._head

        while current is not None:
            s += str(current.value)
            s += " -> "
            current = current.next_node

        # omit last arrow
        return s[:-4]

    # O(1) time and space
    def enqueue(self, value):
        new_node = nodes.Node_SLL(value)

        # if list is empty
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next_node = new_node
        self._tail = new_node

    # O(1) time and space
    def dequeue(self):
        if self._head is None:
            return None

        current_head = self._head
        self._head = current_head.next_node

        # update tail if list is empty
        if current_head == self._tail:
            self._tail = None

        return current_head.value

    # O(1) time and space
    def empty(self):
        """Returns whether queue is empty."""
        return self._head is None

    # O(n) time, O(1) space
    def size(self):
        """Returns number of items in the queue."""
        current = self._head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    # O(1) time and space
    def front(self):
        """Returns the value that will be dequeued next."""
        if self._head is None:
            return None

        return self._head.value

    # O(n) time, O(1) space; if track min and max as attrs can get O(1) time
    def min(self):
        """Returns minimum value in the queue (None if empty)."""
        if self._head is None:  # if list is empty
            return None

        curr_min = self._head.value  # init min to first value
        current = self._head.next_node  # start at next node

        while current is not None:
            if current.value < curr_min:
                curr_min = current.value
            current = current.next_node

        return curr_min

    # O(n) time, O(1) space
    def max(self):
        """Returns maximum value in the queue (None if empty)."""
        if self._head is None:
            return None

        curr_max = self._head.value  # init min to first value
        current = self._head.next_node  # start at next node

        while current is not None:
            if current.value > curr_max:
                curr_max = current.value
            current = current.next_node

        return curr_max


class QueueDLL:
    """Queue class implemented as doubly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None

    def __str__(self):
        s = ""
        current = self._head

        while current is not None:
            s += str(current.value)
            s += " -> "
            current = current.next_node

        return s[:-4]

    def enqueue(self, value):
        new_node = nodes.Node_DLL(value)

        if self._head is None:
            self._head = new_node
        else:
            self._tail.next_node = new_node
            new_node.prev_node = self._tail
        self._tail = new_node

    def dequeue(self):
        if self._head is None:
            return None

        current_head = self._head
        self._head = current_head.next_node

        # check node exists
        if self._head is not None:
            self._head.prev_node = None

        # update tail if list is empty
        if current_head == self._tail:
            self._tail = None

        return current_head.value

    def empty(self):
        """Returns whether queue is empty."""
        return self._head is None

    def size(self):
        """Returns number of items in the queue."""
        current = self._head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def front(self):
        """Returns the value that will be dequeued next."""
        if self._head is None:
            return None

        return self._head.value

    def min(self):
        """Returns minimum value in the queue (None if empty)."""
        if self._head is None:  # if list is empty
            return None

        curr_min = self._head.value  # init min to first value
        current = self._head.next_node  # start at next node

        while current is not None:
            if current.value < curr_min:
                curr_min = current.value
            current = current.next_node

        return curr_min

    def max(self):
        """Returns maximum value in the queue (None if empty)."""
        if self._head is None:
            return None

        curr_max = self._head.value  # init min to first value
        current = self._head.next_node  # start at next node

        while current is not None:
            if current.value > curr_max:
                curr_max = current.value
            current = current.next_node

        return curr_max


class QueueUsingStacks:
    """
    Queue implemented using 2 stacks. NOT O(1) time for en/dequeue.
    
    One stack will always be empty.
    """

    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()  # this stack will always be empty

    def __str__(self):
        return str(self._stack1)

    # time: O(2n)
    # space: O(n) because there are two stacks, but only one of them will be
    # full at a given time (or both will be half full) and the stack is using
    # a linked list. If implemented as an array, then O(2n)
    def enqueue(self, value):
        """Add value to end of queue. NOT O(1) time."""
        if self.empty():
            self._stack1.push(value)
            return

        # reverse values in stack
        while not self._stack1.empty():
            self._stack2.push(self._stack1.pop())

        # push value to empty stack and push vals from 2nd stack
        self._stack1.push(value)

        while not self._stack2.empty():
            self._stack1.push(self._stack2.pop())

    def dequeue(self):
        """
        Return value from front of queue.

        Raise error if queue is already empty.
        """
        if self.empty():
            raise IndexError('dequeue from empty queue')

        return self._stack1.pop()

    # time: O(1)
    def empty(self):
        """Return whether queue is empty."""
        return self._stack1.empty()

    # time: O(n)
    def size(self):
        return self._stack1.size()

    # time: O(1)
    def front(self):
        if self.empty():
            return None

        val = self._stack1.pop()
        self._stack1.push(val)

        return val

    def min(self):
        return self._stack1.min()

    def max(self):
        return self._stack1.max()
