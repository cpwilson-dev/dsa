# Hashmap

A hash map or hash table is a data structure that maps keys to values.

The lookup, insertion, and deletion of operations in a hashmap have an average computational cost of `0(1)`. Assuming you know the key, nothing beats a hashmap.

Hashmaps are built on top of arrays. They use a hash function to covert a "hashable key" into an index i the arrya. From a high-level, all that matters to us is that the hash function:

1. Takes a key and returns an integer.
2. Always returns the same integer for the same key.
3. Always returns a valid index in the array.

Ideally the hash function hashes each eky to a unique index, but most hash table designs employe an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions are typically accommodated for and are not a problem in practice.

```python Hashmap
class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")
        

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
```
