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

## Depth First Search (DFS)

A depth-first search (DFS) is an algorithm to traverse a graph. It starts at a root node and explores as far as poible along each branch before backtracking and starting down the next branch.

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

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

    def depth_first_search(self, start_vertex):
        visited = set()
        result = []
        self.depth_first_search_r(visited, start_vertex, result)
        return result

    def depth_first_search_r(self, visited, current_vertex, result):
        if current_vertex not in visited:
            visited.add(current_vertex)
            result.append(current_vertex)
            for neighbor in sorted(self.graph.get(current_vertex, [])):
                self.depth_first_search_r(visited, neighbor, result)

```

## Breadth First Search (BFS)

The breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at a root and explores all of the neighbour nodes at the present depth bfore going on to the nodes at the next level.

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

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

    def breadth_first_search(self, v):
        visited = set()         # To keep track of visited nodes
        queue = [v]             # Queue for BFS traversal
        result = []             # List to store BFS traversal order

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                result.append(current)
                # Add unvisited neighbors to the queue
                if current in self.graph:
                    for neighbor in sorted(self.graph[current]):
                        if neighbor not in visited:
                            queue.append(neighbor)
        return result
```
