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
    # this is where we implement the specific queueing policy.
    def remove_item(self):
        return self.items.pop(0)

    # Check whether the queue is empty.
    def is_empty(self):
        return len(self.items) == 0


class Item:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return "Name: %s, Priority: %d" % (self.name, self.priority)

class PriorityQueue(Queue):
    # Implements the priority-based queueing policy
    # remove the item that has the highest priority!
    # - to do this, you need to first find the item of highest priority.
    def remove_item(self):
        # sort the items in descending priority order.
        self.items.sort(key=lambda item: item.priority, reverse=True)
        return self.items.pop(0)
