# Number of vertices in the graph
V = 4

# Define a large number for representing infinity
INF = float('inf')

# Floyd-Warshall algorithm
def floyd_warshall(graph):
    # Initialize the solution matrix same as input graph matrix
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Adding vertices individually to the set of intermediate vertices
    for k in range(V):
        # Pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above-picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Print the shortest distance matrix
    print_solution(dist)

# A utility function to print the solution
def print_solution(dist):
    print("Shortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end="  ")
        print("")

# Example graph (Adjacency matrix representation)
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]

# Running the algorithm
floyd_warshall(graph)
