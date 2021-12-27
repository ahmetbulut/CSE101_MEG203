import unittest
from inheritance.queueing import Queue


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        queue = Queue()
        # there are no additions in between the time of creation, and the time of spot check!
        self.assertEqual(True, queue.is_empty())

if __name__ == '__main__':
    unittest.main()
