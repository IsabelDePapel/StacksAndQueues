MAX_SIZE = 5


class StackArray(object):
    """Stack class implemented as an array."""

    def __init__(self):
        self._lst = [None] * MAX_SIZE
        self._back = 0  # to track where list ends

    def __str__(self):
        if self._back == 0:
            return "empty"

        str_lst = ""
        idx = self._back - 1

        while idx >= 0:
            str_lst += " <- "
            str_lst += str(self._lst[idx])
            idx -= 1

        return str_lst[4:]

    def push(self, value):
        """
        Add value to stack.

        Uses self._back to track where last item in stack is.
        Self._back gives index + 1 (this avoids checking for None).
        """
        # check if stack is full
        if self._back == MAX_SIZE:
            raise IndexError('push to full stack')

        self._lst[self._back] = value
        self._back += 1  # this is index of element added + 1

    def pop(self):
        if self._back == 0:
            return None

        self._back -= 1

        val = self._lst[self._back]
        self._lst[self._back] = None  # reassign to blank placeholder

        return val

    def empty(self):
        return self._back == 0

    def size(self):
        return self._back

    def top(self):
        """
        Return next value to be popped.

        Returns none if stack is empty.
        """
        return self._lst[self._back - 1]

    def min(self):
        if self.empty():
            return None

        idx = self._back - 1
        curr_min = self._lst[idx]

        while idx - 1 >= 0:
            if self._lst[idx - 1] < curr_min:
                curr_min = self._lst[idx - 1]
            idx -= 1

        return curr_min

    def max(self):
        if self.empty():
            return None

        idx = self._back - 1
        curr_max = self._lst[idx]

        while idx - 1 >= 0:
            if self._lst[idx - 1] > curr_max:
                curr_max = self._lst[idx - 1]
            idx -= 1

        return curr_max


class StackList(object):
    """Stack class implemented with list (using list methods)."""

    def __init__(self):
        self._lst = []
        self._back = 0  # track where list ends

    def __str__(self):
        if self._back == 0:
            return "empty"

        # iterate backwards through lst and add to string
        str_lst = ""
        for i in range(self._back - 1, -1, -1):
            str_lst += str(self._lst[i])
            str_lst += " <- "

        return str_lst[:-4]

    def push(self, value):
        self._lst.append(value)
        self._back += 1

    def pop(self):
        self._back -= 1
        return self._lst.pop()  # will throw error if list is empty

    def empty(self):
        return self._back == 0

    def size(self):
        return self._back

    def top(self):
        if self._back == 0:
            return None

        return self._lst[self._back - 1]

    def min(self):
        if self._back == 0:
            return None

        # set min to first value
        curr_min = self._lst[0]

        for idx in range(1, self._back):
            if self._lst[idx] < curr_min:
                curr_min = self._lst[idx]

        return curr_min

    def max(self):
        if self._back == 0:
            return None

        # set max to first value
        curr_max = self._lst[0]

        for idx in range(1, self._back):
            if self._lst[idx] > curr_max:
                curr_max = self._lst[idx]

        return curr_max
