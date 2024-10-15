# Class to represent an edge in the graph
class Edge:
    def __init__(self, source, destination, weight):
        self.source = source  # Starting vertex of the edge
        self.destination = destination  # Ending vertex of the edge
        self.weight = weight  # Weight of the edge

# Function to execute the Bellman-Ford algorithm
def bellman_ford(edges, vertices, source):
    # Initialize distance array with infinity for all vertices
    distance = [float("inf")] * vertices
    # Set the distance to the source vertex to 0
    distance[source] = 0

    # Relax all edges (vertices - 1) times to find the shortest path
    for _ in range(vertices - 1):
        # Loop over each edge in the graph
        for edge in edges:
            u = edge.source
            v = edge.destination
            weight = edge.weight

            # If the current edge can relax the distance to vertex v, update the distance
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    # Check for negative weight cycles
    for edge in edges:
        u = edge.source
        v = edge.destination
        weight = edge.weight

        # If we can still relax an edge, then a negative weight cycle exists
        if distance[u] != float("inf") and distance[u] + weight < distance[v]:
            print("Graph contains a negative weight cycle")
            return

    # Print the final shortest distances from the source vertex to each vertex
    print_solution(distance)

# Function to print the distances from the source to all vertices
def print_solution(distance):
    print("Vertex   Distance from Source")
    for i, d in enumerate(distance):
        # Print distance; if unreachable, display infinity symbol
        print(f"{i} \t\t {d if d != float('inf') else '∞'}")

# Main function to take user input and run the algorithm
def main():
    # Take input for number of vertices and edges in the graph
    vertices = int(input("Enter number of vertices: "))
    edges_count = int(input("Enter number of edges: "))

    # List to store all edges of the graph
    edges = []

    # Take input for each edge: source, destination, and weight
    print("Enter edges (source destination weight):")
    for _ in range(edges_count):
        source, destination, weight = map(int, input().split())
        edges.append(Edge(source, destination, weight))

    # Take input for the source vertex from which to calculate distances
    source = int(input("Enter the source vertex: "))

    # Run the Bellman-Ford algorithm on the input data
    bellman_ford(edges, vertices, source)

# Entry point of the program
if __name__ == "__main__":
    main()
