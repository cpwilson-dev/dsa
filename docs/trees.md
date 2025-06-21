# Trees

Trees are a widely used data structure that simulate a hierarchical tree structure. Trees are like linked lists in the sense that the root node simply holds references to ites child nodes, which in turn hyold references to thier children, but Tree's nodes can have multiple children instead of just one. 

A generic tree structure has the following rules:
- Each node hasa a value and may have a list of 'children'
- Children can only have a single 'parent'

``` Linked List
node -> node -> node
```

``` Tree
            > node
      > node
            > node
            > node
> node
            > node
            > node
            > node
      > node
            > node
```

## Binary Trees

One of the most common types of ordered tree is a Binary Search Tree or `BST`. A `BST` has some additional constraints:

1. Instead of an unbounded list of children, each node has at most 2 children.
2. The left child's value must be less than its parent's value.
3. The right child's value must be greater than its parent's value.
4. No two nodes in the `BST` can have the same value.

```python Binary Search Tree

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self,val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)

        if val > self.val:
            if self.right:
                self.right.insert(val)
                return
            self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self):
        if self.val is None:
            return None

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    def exists(self,val):
        if self.val is None:
            return False

        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if val > self.val:
            if self.right is None:
                return False
            return self.right.exists(val)

    def height(self):
        if self.val is None:
            return 0

        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)


```
