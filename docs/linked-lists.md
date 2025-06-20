# Linked Lists

A linked list is where elements are not stored next ot each other in memory, instead, each item references the next in a chain. Linked lists have a faster time complexity than regular lists when it comes to inserting or deleting items in the middle of the list as you can simplye update two references.

## Nodes

Our nodes will be represented by a simple class with two fields:

- `val` - The raw string value that the node holds
- `next` - A reference to the next node in the list

```python Node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
```

```python LinkedList
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

```
```python LLQueue

from node import Node

class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None  

        removed_node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        removed_node.next = None 
        return removed_node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

```

