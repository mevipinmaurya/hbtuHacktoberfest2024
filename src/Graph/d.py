from collections import defaultdict, deque

# Graph class for Kahn's Algorithm (BFS-based Topological Sort)
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Default dictionary to store the graph
        self.V = vertices               # Number of vertices

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to perform Topological Sort using Kahn's Algorithm
    def topological_sort(self):
        # Create a list to store the in-degree of all vertices
        in_degree = [0] * self.V

        # Fill the in-degree list
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Queue to store all vertices with in-degree 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])

        # List to store the topological order
        topo_sort = []

        # Process vertices with in-degree 0
        while queue:
            u = queue.popleft()
            topo_sort.append(u)

            # Decrease the in-degree of all neighbors of the dequeued vertex
            for neighbor in self.graph[u]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If topological sort includes all vertices, return the result
        if len(topo_sort) == self.V:
            print(topo_sort)
        else:
            print("The graph has a cycle and topological sort is not possible.")

# Example usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort of the given graph:")
g.topological_sort()
