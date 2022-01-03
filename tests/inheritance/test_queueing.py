import unittest
from inheritance.queueing import Queue, PriorityQueue, Item


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

    def test_priority_queue(self):
        # priorities: 0 to 5, 0 the lowest, 5 the highest.
        queue = PriorityQueue()

        item1 = Item("Word Application", 1)
        queue.add_item(item1)

        item2 = Item("Mission Critical Application", 5)
        queue.add_item(item2)

        item3 = Item("Scientific Computing - Matlab", 3)
        queue.add_item(item3)

        item = queue.remove_item()
        self.assertEqual(item.name, item2.name)

        item = queue.remove_item()
        self.assertEqual(item.name, item3.name)


if __name__ == '__main__':
    unittest.main()
