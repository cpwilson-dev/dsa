# Queues

A queue is a data structure that stores ordered items. It's like a list, but its design is more restrictive, It only allows items to be added to the tail and removes from the head of the stack.

```python
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

```
