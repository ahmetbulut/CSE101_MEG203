class Node:
    """
    This represents the individual nodes of a tree.
    """
    def __init__(self, name, left_child, right_child):
        self.name = name
        self.left = left_child
        self.right = right_child

    # pre-order tree traversal
    def __str__(self):
        representation = ""

        representation += "\n" + self.name

        if (self.left):
            representation += "\n" + str(self.left)

        if (self.right):
            representation += "\n" + str(self.right)

        return representation


class Tree:
    """
    Represents the Tree structure, as in File Systems, Object Relationships.
    The tree has a root, the root may have children.
    Those children may have their own children.
    """
    def __init__(self, root_node):
        self.root = root_node

    def __str__(self):
        return str(self.root)

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