"""Queue implementations using list/array instead of linked list."""

MAX_SIZE = 6  # num items queue will hold + 1 (for placeholder)


class QueueArray(object):
    """Queue class implemented using an array. Doesn't allow overwriting."""

    def __init__(self):
        self._lst = [None] * (MAX_SIZE)
        self._front = 0
        self._back = 0

    def __str__(self):
        str_lst = ""

        if self._front == self._back:
            return "empty"
        elif self._front < self._back:
            for idx in range(self._front, self._back):
                str_lst += str(self._lst[idx])
                str_lst += " -> "
        else:
            # iterate from front to end of queue
            for idx in range(self._front, MAX_SIZE):
                str_lst += str(self._lst[idx])
                str_lst += " -> "
            # iterate from front of queue to back
            for idx in range(0, self._back):
                str_lst += str(self._lst[idx])
                str_lst += " -> "

        return str_lst[:-4]

    def enqueue(self, value):
        """Add item to the queue. Raise error if queue is full."""
        # check if queue is full
        if self.full():
            raise IndexError("enqueue to full queue")

        self._lst[self._back] = value
        self._back += 1

    def dequeue(self):
        """Remove item from the queue. Raise error if queue is empty."""
        # check if queue is empty
        if self.empty():
            raise IndexError("dequeue from empty queue")

        # get val at front and update front to point to next val
        val = self._lst[self._front]
        self._front = (self._front + 1) % MAX_SIZE

        return val

    def empty(self):
        """Return whether queue is empty."""
        return self._front == self._back

    def full(self):
        """Return whether queue is full."""
        return self._front == (self._back + 1) % MAX_SIZE

    def size(self):
        return ((self._back - self._front) % MAX_SIZE)

    def front(self):
        if self.empty():
            return None

        return self._lst[self._front]

    def min(self):
        pass

    def max(self):
        pass
