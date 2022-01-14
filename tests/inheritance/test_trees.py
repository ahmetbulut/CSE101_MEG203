import unittest

from inheritance.trees import Node

class MyTestCase(unittest.TestCase):
    def test_construction(self):
        # ll and lr are leaf nodes
        ll = Node("2", None, None)
        lr = Node("4", None, None)

        # rl and rr are leaf nodes
        rl = Node("5", None, None)
        rr = Node("15", None, None)

        # l and r are internal nodes
        l = Node("+", ll, lr)
        r = Node("*", rl, rr)

        # root node, which has l & r as its children.
        root = Node("/", l, r)

        print(root.print_tree())


if __name__ == '__main__':
    unittest.main()
