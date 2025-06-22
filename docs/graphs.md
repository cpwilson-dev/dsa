# Graphs

A graph is a set of vertices and the edges that connect those vertices. All trees are graphs, but not all graphs are trees.

## Properties

- Graphs can have any number of vertices
- An undirected graph can have up to `n(n-1)/2` ediges for `n` vertices.
- Vertices can exits without edges but may be disconnected.
- Typically graphs can only have a single edge between twp verticies.
- Weighted graphs assigned values (costs) to edges.

## Common Use Cases
- Social Networks
- Road Maps
- Networks
- AI Decision

## Adjacency Matrix

|       | A | B | C | D |
| ----- | - | - | - | - |
| **A** | 0 | 1 | 1 | 0 |
| **B** | 0 | 0 | 0 | 1 |
| **C** | 0 | 0 | 0 | 1 |
| **D** | 0 | 0 | 0 | 0 |


```python
class Graph:
    def __init__(self, num_vertices):
        self.graph = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self.graph.append(row)

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
```
## Adjacency List

A → B, C  
B → D  
C → D  
D → (none)

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
```
