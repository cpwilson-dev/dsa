# Red-Black Trees

A red-black tree is a kind of binary search tree that solves the "balancing" problem. It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree meains relatively blanced.

Each node in an RB tree stores an extra bit, called the "color", either red or black. The "color" ensures that the tree remains approximately blanaced during insertions and deletions. When the tree is modified, the new tree is arranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

- Each node is either red or black.
- The root is black.
- All Nil leaf nodes are black.
- If a node is red, then both its children are black.
- All paths from a single node go through the same number of black nodes to reach any of its descendant Nil(black) nodes.

```python
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        node = new_node
        while node != self.root and node.parent.red:
            parent = node.parent
            grandparent = parent.parent

            if parent == grandparent.right:
                uncle = grandparent.left
                if uncle.red:
                    parent.red = False
                    uncle.red = False
                    grandparent.red = True
                    node = grandparent
                else:
                    if node == parent.left:
                        node = parent
                        self.rotate_right(node)
                    parent = node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
            else:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    node = grandparent
                else:
                    if node == parent.right:
                        node = parent
                        self.rotate_left(node)
                    parent = node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
```
