import unittest

from inheritance.trees import Tree, Node

class MyTestCase(unittest.TestCase):
    def test_construction(self):
        # ll and lr are leaf nodes
        ll = Node("LL child", None, None)
        lr = Node("LR child", None, None)

        # rl and rr are leaf nodes
        rl = Node("RL child", None, None)
        rr = Node("RR child", None, None)

        # l and r are internal nodes
        l = Node("L child", ll, lr)
        r = Node("R child", rl, rr)

        # root node, which has l & r as its children.
        root = Node("Root", l, r)

        tree = Tree(root)

        print(tree)


if __name__ == '__main__':
    unittest.main()
