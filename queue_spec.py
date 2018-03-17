import unittest
import queue_arr as qa
import queue_ll as ql


class TestQueueSLLClass(unittest.TestCase):
    """Test singly linked list queue class functionality."""

    def setUp(self):
        self.empty_q = ql.QueueSLL()

        self.small_q = ql.QueueSLL()
        self.small_q.enqueue(2)

        self.medium_q = ql.QueueSLL()
        self.medium_q.enqueue(2)
        self.medium_q.enqueue(4)
        self.medium_q.enqueue(6)

    def test_enqueue(self):
        self.assertEqual(str(self.small_q), '2')

        self.assertEqual(str(self.medium_q), '2 -> 4 -> 6')

        self.medium_q.enqueue(8)
        self.assertEqual(str(self.medium_q), '2 -> 4 -> 6 -> 8')

    def test_dequeue(self):
        self.assertIsNone(self.empty_q.dequeue())

        self.assertEqual(self.medium_q.dequeue(), 2)
        self.assertEqual(self.medium_q._head.value, 4)
        self.assertEqual(self.medium_q._tail.value, 6)
        self.assertEqual(self.medium_q.dequeue(), 4)
        self.assertEqual(self.medium_q._head.value, 6)
        self.assertEqual(self.medium_q._tail.value, 6)

        self.assertEqual(self.medium_q.dequeue(), 6)
        self.assertIsNone(self.medium_q.dequeue())
        self.assertIsNone(self.medium_q._head)
        self.assertIsNone(self.medium_q._tail)

    def test_empty(self):
        self.assertTrue(self.empty_q.empty())
        self.assertFalse(self.small_q.empty())

        self.small_q.dequeue()
        self.assertTrue(self.small_q.empty())

    def test_size(self):
        self.assertEqual(self.empty_q.size(), 0)
        self.assertEqual(self.small_q.size(), 1)
        self.assertEqual(self.medium_q.size(), 3)

    def test_front(self):
        self.assertIsNone(self.empty_q.front())
        self.assertEqual(self.small_q.front(), 2)
        self.assertEqual(self.medium_q.front(), 2)

        self.medium_q.dequeue()
        self.assertEqual(self.medium_q.front(), 4)

    def test_min(self):
        self.assertIsNone(self.empty_q.min())
        self.assertEqual(self.small_q.min(), 2)
        self.assertEqual(self.medium_q.min(), 2)

        self.medium_q.dequeue()
        self.assertEqual(self.medium_q.min(), 4)

    def test_max(self):
        self.assertIsNone(self.empty_q.max())
        self.assertEqual(self.small_q.max(), 2)
        self.assertEqual(self.medium_q.max(), 6)

        self.medium_q.enqueue(8)
        self.assertEqual(self.medium_q.max(), 8)


class TestQueueDLLClass(unittest.TestCase):
    """Test doubly linked list queue class functionality."""

    def setUp(self):
        self.empty_q = ql.QueueDLL()

        self.small_q = ql.QueueDLL()
        self.small_q.enqueue(2)

        self.medium_q = ql.QueueDLL()
        self.medium_q.enqueue(2)
        self.medium_q.enqueue(4)
        self.medium_q.enqueue(6)

    def test_enqueue(self):
        self.assertEqual(str(self.small_q), '2')

        self.assertEqual(str(self.medium_q), '2 -> 4 -> 6')
        self.assertEqual(self.medium_q._head.value, 2)
        self.assertEqual(self.medium_q._tail.value, 6)

        self.medium_q.enqueue(8)
        self.assertEqual(str(self.medium_q), '2 -> 4 -> 6 -> 8')
        self.assertEqual(self.medium_q._head.value, 2)
        self.assertEqual(self.medium_q._tail.value, 8)

    def test_dequeue(self):
        self.assertEqual(self.medium_q.dequeue(), 2)
        # check head and its node ref
        self.assertEqual(self.medium_q._head.value, 4)
        self.assertEqual(self.medium_q._head.next_node.value, 6)
        # check tail and its node ref
        self.assertEqual(self.medium_q._tail.value, 6)
        self.assertEqual(self.medium_q._tail.prev_node.value, 4)

        self.assertEqual(self.medium_q.dequeue(), 4)
        self.assertEqual(self.medium_q._head.value, 6)
        self.assertEqual(self.medium_q._tail.value, 6)

        self.assertEqual(self.medium_q.dequeue(), 6)
        self.assertIsNone(self.medium_q._head)
        self.assertIsNone(self.medium_q._tail)


class TestQueueArrayClass(unittest.TestCase):
    """
    Test functionality of queue class implemented using list of fixed size.
    """

    def setUp(self):
        self.empty_q = qa.QueueArray()

        self.small_q = qa.QueueArray()
        self.small_q.enqueue(2)

        self.medium_q = qa.QueueArray()
        self.medium_q.enqueue(2)
        self.medium_q.enqueue(4)
        self.medium_q.enqueue(6)

    def test_empty(self):
        self.assertTrue(self.empty_q.empty())
        self.assertFalse(self.small_q.empty())

        self.small_q.dequeue()
        self.assertTrue(self.small_q.empty())

    def test_full(self):
        self.assertFalse(self.medium_q.full())

        self.medium_q.enqueue(8)
        self.medium_q.enqueue(10)

        self.assertTrue(self.medium_q.full())

        self.medium_q.dequeue()
        self.assertFalse(self.medium_q.full())

    def test_enqueue(self):
        self.assertEqual(str(self.empty_q), "empty")
        self.assertEqual(str(self.small_q), "2")

        self.assertEqual(str(self.medium_q), "2 -> 4 -> 6")
        self.assertEqual(self.medium_q._front, 0)
        self.assertEqual(self.medium_q._back, 3)

        self.medium_q.enqueue(8)
        self.assertEqual(str(self.medium_q), "2 -> 4 -> 6 -> 8")
        self.assertEqual(self.medium_q._back, 4)

        self.medium_q.enqueue(10)
        with self.assertRaises(IndexError):
            self.medium_q.enqueue(12)

    def test_dequeue(self):
        with self.assertRaises(IndexError):
            self.empty_q.dequeue()

        self.assertEqual(self.medium_q.dequeue(), 2)
        # check front and back refs
        self.assertEqual(self.medium_q._front, 1)
        self.assertEqual(self.medium_q._back, 3)

        self.assertEqual(self.medium_q.dequeue(), 4)
        self.assertEqual(self.medium_q._front, 2)
        self.assertEqual(self.medium_q._back, 3)

        self.assertEqual(self.medium_q.dequeue(), 6)
        self.assertEqual(self.medium_q._front, self.medium_q._back)

    def test_size(self):
        self.assertEqual(self.empty_q.size(), 0)
        self.assertEqual(self.medium_q.size(), 3)

        self.medium_q.enqueue(8)
        self.medium_q.enqueue(10)
        self.assertEqual(self.medium_q.size(), 5)

        self.medium_q.dequeue()
        self.assertEqual(self.medium_q.size(), 4)

    def test_front(self):
        self.assertIsNone(self.empty_q.front())
        self.assertEqual(self.small_q.front(), 2)
        self.assertEqual(self.medium_q.front(), 2)

        self.medium_q.dequeue()
        self.assertEqual(self.medium_q.front(), 4)


if __name__ == '__main__':
    unittest.main()
