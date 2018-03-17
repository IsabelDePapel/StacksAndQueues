import nodes


# can't do this with singly linked list, bc always need prev node
# to pop from the back. Lose O(1) time for popping.
class StackSLL:
    """Stack class implemented as singly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None

    def __str__(self):
        s = ""
        current = self._head

        while current is not None:
            s += " <- "
            s += str(current.value)
            current = current.next_node

        return s[4:]

    def push(self, value):
        new_node = nodes.Node_SLL(value)

        if self._tail is None:
            self._tail = new_node
            self._head = new_node

        else:
            self._tail.next_node = new_node

        self._tail = new_node

    def pop(self):
        pass


class StackDLL:
    """Stack class implemented as doubly linked list."""

    def __init__(self):
        self._tail = None

    def __str__(self):
        s = ""

        current = self._tail

        while current is not None:
            s += " <- "
            s += str(current.value)
            current = current.prev_node

        return s[4:]

    def push(self, value):
        new_node = nodes.Node_DLL(value)

        if self._tail is not None:  # list is not empty
            self.tail_next_node = new_node
            new_node.prev_node = self._tail

        self._tail = new_node  # update tail

    def pop(self):
        if self._tail is None:
            return None

        current_tail = self._tail
        self._tail = current_tail.prev_node

        if self._tail is not None:
            self._tail.next_node = None

        return current_tail.value

    def empty(self):
        return self._tail is None

    def size(self):
        count = 0
        current = self._tail

        while current is not None:
            count += 1
            current = current.prev_node

        return count

    def top(self):
        if self._tail is None:
            return None

        return self._tail.value

    def min(self):
        if self._tail is None:
            return None

        curr_min = self._tail.value  # init min to first val
        current = self._tail.prev_node  # start with next node

        while current is not None:
            if current.value < curr_min:
                curr_min = current.value
            current = current.prev_node

        return curr_min

    def max(self):
        if self._tail is None:
            return None

        curr_max = self._tail.value
        current = self._tail.prev_node

        while current is not None:
            if current.value > curr_max:
                curr_max = current.value
            current = current.prev_node

        return curr_max
