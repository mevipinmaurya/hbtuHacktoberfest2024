from collections import defaultdict

# Graph class for DFS-based Topological Sort
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Default dictionary to store the graph
        self.V = vertices               # Number of vertices

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Recursive helper function for DFS
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        # Push the current vertex to the stack which stores the topological sort
        stack.append(v)

    # Main function to perform Topological Sort
    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        # Call the helper function for all vertices not yet visited
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Return the reverse of the stack to get the topological ordering
        print(stack[::-1])

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
