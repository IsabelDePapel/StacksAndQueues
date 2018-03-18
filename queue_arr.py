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
        self._back = (self._back + 1) % MAX_SIZE

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
        if self.empty():
            return None

        current_min = self._lst[self._front]

        # check if need to iterate over end of queue and start at beginning
        if self._front < self._back:
            for idx in range(self._front + 1, self._back):
                current_min = self.__update_min(idx, current_min)
        else:
            # iterate from front to end, then idx 0 to back
            for idx in range(self._front + 1, MAX_SIZE):
                current_min = self.__update_min(idx, current_min)
            for idx in range(0, self._back):
                current_min = self.__update_min(idx, current_min)

        return current_min

    def __update_min(self, idx, current_min):
        """
        Private function to update current min if value at given index is less
        than current_min.

        Returns current_min.
        """
        if self._lst[idx] < current_min:
            current_min = self._lst[idx]

        return current_min

    def max(self):
        if self.empty():
            return None

        current_max = self._lst[self._front]

        # check if need to cycle through queue or not
        if self._front < self._back:
            for idx in range(self._front, self._back):
                current_max = self.__update_max(idx, current_max)
        else:
            # iterate front to end, 0 to back
            for idx in range(self._front, MAX_SIZE):
                current_max = self.__update_max(idx, current_max)
            for idx in range(0, self._back):
                current_max = self.__update_max(idx, current_max)

        return current_max

    def __update_max(self, idx, current_max):
        """
        Private function to update current_max if value at given index is less
        than current_max.

        Returns current_max.
        """
        if self._lst[idx] > current_max:
            current_max = self._lst[idx]

        return current_max
