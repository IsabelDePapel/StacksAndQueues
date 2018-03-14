class Node_SLL:
    """Node class for singly linked list."""

    def __init__(self, value):
        self._value = value
        self._next_node = None

    def __str__(self):
        s = "Node: val " + str(self._value)
        return s

    @property
    def value(self):
        return self._value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class Node_DLL:
    """Node class for doubly linked list."""

    def __init__(self, value):
        self._value = value
        self._next_node = None
        self._prev_node = None

    @property
    def value(self):
        return self._value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, node):
        self._prev_node = node
