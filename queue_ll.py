import nodes


class Queue_SLL:
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


class Queue_DLL:
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
