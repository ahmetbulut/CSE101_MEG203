import unittest
from inheritance.queueing import Queue


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        queue = Queue()
        # there are no additions in between the time of creation, and the time of spot check!
        self.assertEqual(True, queue.is_empty())

    def test_functionality(self):
        queue = Queue()
        first_in = 77
        queue.add_item(first_in)
        queue.add_item(101)
        queue.add_item(1)

        # first in first out?
        self.assertEqual(first_in, queue.remove_item())

if __name__ == '__main__':
    unittest.main()
