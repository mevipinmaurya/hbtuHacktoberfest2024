from collections import defaultdict

# Graph class to represent a directed graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Default dictionary to store the graph
        self.V = vertices               # Number of vertices in the graph

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Helper function to perform DFS and detect a cycle
    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        # Recur for all vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            # If the neighbor is not visited, do a DFS from that node
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            # If the neighbor is in the recursion stack, we found a cycle
            elif rec_stack[neighbor]:
                return True

        # Remove the vertex from recursion stack
        rec_stack[v] = False
        return False

    # Main function to detect a cycle in the graph
    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        # Call the helper function for every vertex to detect a cycle
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

# Example usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # Adding this edge creates a cycle
g.add_edge(2, 3)

if g.is_cyclic():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
