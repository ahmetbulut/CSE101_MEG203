class Queue:
    """"
    This is a simple queue.
    It has a simple queueing policy.
    First In, First Out!
    """

    # Initialize a new empty queue.
    def __init__(self):
        self.items = []

    # Add a new item to the queue.
    def add_item(self, item):
        self.items.append(item)

    # Remove and return an item from the queue.
    # The item that is returned is the first one that was added.
    def remove_item(self):
        self.items.pop(0)

    # Check whether the queue is empty.
    def is_empty(self):
        return len(self.items) == 0