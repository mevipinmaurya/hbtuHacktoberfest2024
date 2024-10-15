import heapq

# Dijkstra's algorithm
def dijkstra(graph, src):
    # Number of vertices in the graph
    V = len(graph)
    
    # Distances array, initialized to infinity
    dist = [float('inf')] * V
    dist[src] = 0  # Distance to the source itself is 0

    # Priority queue (min-heap) for exploring the next vertex with the shortest known distance
    pq = [(0, src)]  # (distance, vertex)
    
    while pq:
        # Get the vertex with the smallest distance
        current_dist, u = heapq.heappop(pq)
        
        # If the current distance is greater than the known shortest distance, skip
        if current_dist > dist[u]:
            continue
        
        # Explore the neighbors of the current vertex
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            # If a shorter path to the vertex v is found
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))
    
    # Print the shortest distances from the source
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t\t{dist[i]}")

# Example graph represented as an adjacency list
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

# Running the algorithm
src_vertex = 0  # Starting from vertex 0
dijkstra(graph, src_vertex)
