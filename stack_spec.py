import unittest
import stack_ll as ls
import stack_arr as ars


class TestStackLLClass(unittest.TestCase):
    """Test Stack class functionality."""

    def setUp(self):
        self.empty_stack = ls.Stack_DLL()

        self.small_stack = ls.Stack_DLL()
        self.small_stack.push(2)

        self.medium_stack = ls.Stack_DLL()
        self.medium_stack.push(2)
        self.medium_stack.push(4)
        self.medium_stack.push(6)

    def test_push(self):
        self.assertEqual(str(self.small_stack), '2')
        self.assertEqual(str(self.medium_stack), '6 <- 4 <- 2')

        self.medium_stack.push(8)
        self.assertEqual(str(self.medium_stack), '8 <- 6 <- 4 <- 2')
        self.assertEqual(self.medium_stack._tail.value, 8)
        self.assertEqual(self.medium_stack._tail.prev_node.value, 6)

    def test_pop(self):
        self.assertIsNone(self.empty_stack.pop())

        self.assertEqual(self.medium_stack.pop(), 6)
        self.assertEqual(self.medium_stack._tail.value, 4)
        self.assertEqual(self.medium_stack._tail.prev_node.value, 2)
        self.assertIsNone(self.medium_stack._tail.next_node)

        self.assertEqual(self.medium_stack.pop(), 4)
        self.assertEqual(self.medium_stack._tail.value, 2)
        self.assertIsNone(self.medium_stack._tail.prev_node)

    def test_empty(self):
        self.assertTrue(self.empty_stack.empty())
        self.assertFalse(self.small_stack.empty())

        self.small_stack.pop()
        self.assertTrue(self.small_stack.empty())

    def test_size(self):
        self.assertEqual(self.empty_stack.size(), 0)
        self.assertEqual(self.small_stack.size(), 1)
        self.assertEqual(self.medium_stack.size(), 3)

        self.medium_stack.push(8)
        self.assertEqual(self.medium_stack.size(), 4)

    def test_top(self):
        self.assertIsNone(self.empty_stack.top())
        self.assertEqual(self.small_stack.top(), 2)
        self.assertEqual(self.medium_stack.top(), 6)

        self.medium_stack.pop()
        self.assertEqual(self.medium_stack.top(), 4)

    def test_min(self):
        self.assertIsNone(self.empty_stack.min())
        self.assertEqual(self.small_stack.min(), 2)
        self.assertEqual(self.medium_stack.min(), 2)

        self.medium_stack.push(0)
        self.assertEqual(self.medium_stack.min(), 0)

    def test_max(self):
        self.assertIsNone(self.empty_stack.max())
        self.assertEqual(self.small_stack.max(), 2)
        self.assertEqual(self.medium_stack.max(), 6)

        self.medium_stack.push(10)
        self.medium_stack.push(9)
        self.assertEqual(self.medium_stack.max(), 10)


class TestStackArrClass(unittest.TestCase):
    """Test Stack class (array) functionality."""

    def setUp(self):
        self.empty_stack = ars.StackArray()

        self.small_stack = ars.StackArray()
        self.small_stack.push(2)

        self.medium_stack = ars.StackArray()
        self.medium_stack.push(2)
        self.medium_stack.push(4)
        self.medium_stack.push(6)

    def test_push(self):
        self.assertEqual(str(self.empty_stack), "empty")
        self.assertEqual(str(self.small_stack), "2")
        self.assertEqual(str(self.medium_stack), "6 <- 4 <- 2")

        self.medium_stack.push(8)
        self.medium_stack.push(10)

        with self.assertRaises(IndexError):
            self.medium_stack.push(12)

    def test_pop(self):
        self.assertIsNone(self.empty_stack.pop())
        self.assertEqual(self.medium_stack.pop(), 6)
        self.assertEqual(self.medium_stack.pop(), 4)

    def test_empty(self):
        self.assertTrue(self.empty_stack.empty())
        self.assertFalse(self.small_stack.empty())

        self.small_stack.pop()
        self.assertTrue(self.small_stack.empty())

    def test_size(self):
        self.assertEqual(self.empty_stack.size(), 0)
        self.assertEqual(self.small_stack.size(), 1)
        self.assertEqual(self.medium_stack.size(), 3)

        self.medium_stack.push(8)
        self.assertEqual(self.medium_stack.size(), 4)

    def test_top(self):
        self.assertIsNone(self.empty_stack.top())
        self.assertEqual(self.small_stack.top(), 2)
        self.assertEqual(self.medium_stack.top(), 6)

        self.medium_stack.push(8)
        self.assertEqual(self.medium_stack.top(), 8)

    def test_min(self):
        self.assertIsNone(self.empty_stack.min())
        self.assertEqual(self.small_stack.min(), 2)
        self.assertEqual(self.medium_stack.min(), 2)

        self.medium_stack.push(0)
        self.assertEqual(self.medium_stack.min(), 0)

    def test_max(self):
        self.assertIsNone(self.empty_stack.max())
        self.assertEqual(self.small_stack.max(), 2)
        self.assertEqual(self.medium_stack.max(), 6)


class TestStackListClass(unittest.TestCase):
    """Test stack functionality using list and list methods to implement."""

    def setUp(self):
        self.empty_stack = ars.StackList()

        self.small_stack = ars.StackList()
        self.small_stack.push(2)

        self.medium_stack = ars.StackList()
        self.medium_stack.push(2)
        self.medium_stack.push(4)
        self.medium_stack.push(6)

    def test_push(self):
        self.assertEqual(str(self.empty_stack), "empty")
        self.assertEqual(str(self.small_stack), "2")
        self.assertEqual(str(self.medium_stack), "6 <- 4 <- 2")

        self.medium_stack.push(8)
        self.medium_stack.push(10)

        # with self.assertRaises(IndexError):
        #     self.medium_stack.push(12)

    def test_pop(self):
        with self.assertRaises(IndexError):
            self.empty_stack.pop()

        self.assertEqual(self.medium_stack.pop(), 6)
        self.assertEqual(self.medium_stack.pop(), 4)

    def test_empty(self):
        self.assertTrue(self.empty_stack.empty())
        self.assertFalse(self.small_stack.empty())

        self.small_stack.pop()
        self.assertTrue(self.small_stack.empty())

    def test_size(self):
        self.assertEqual(self.empty_stack.size(), 0)
        self.assertEqual(self.small_stack.size(), 1)
        self.assertEqual(self.medium_stack.size(), 3)

        self.medium_stack.push(8)
        self.assertEqual(self.medium_stack.size(), 4)

    def test_top(self):
        self.assertIsNone(self.empty_stack.top())
        self.assertEqual(self.small_stack.top(), 2)
        self.assertEqual(self.medium_stack.top(), 6)

        self.medium_stack.push(8)
        self.assertEqual(self.medium_stack.top(), 8)

    def test_min(self):
        self.assertIsNone(self.empty_stack.min())
        self.assertEqual(self.small_stack.min(), 2)
        self.assertEqual(self.medium_stack.min(), 2)

        self.medium_stack.push(0)
        self.assertEqual(self.medium_stack.min(), 0)

    def test_max(self):
        self.assertIsNone(self.empty_stack.max())
        self.assertEqual(self.small_stack.max(), 2)
        self.assertEqual(self.medium_stack.max(), 6)


if __name__ == '__main__':
    unittest.main()
