class Node:
    """
    Represents Nodes a Tree structure, as in File Systems, Object Relationships.
    The tree has a root node, the root may have children.
    Those children may have their own children.
    """
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    # in-order traversal of the tree
    def print_tree(self):
        if self.left and self.right:
            footprint = "(" + self.left.print_tree() + \
                        self.name + \
                        self.right.print_tree() + \
                        ")"
            return footprint
        else:
            return self.name