import sys

def min_distance(dist, visited, V):
    min_dist = sys.maxsize
    min_index = -1
    for v in range(V):
        if dist[v] < min_dist and not visited[v]:
            min_dist = dist[v]
            min_index = v
    return min_index

def print_solution(dist, V):
    print("Vertex \tDistance from Source")
    for i in range(V):
        print(i, "\t", dist[i])

def dijkstra(graph, src, V):
    dist = [sys.maxsize] * V
    visited = [False] * V
    dist[src] = 0

    for _ in range(V):
        u = min_distance(dist, visited, V)
        visited[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist, V)

# Dynamic input from the user for array length
V = int(input("Enter the number of vertices: "))

# Dynamic input for the adjacency matrix representing the graph
print("Enter the adjacency matrix (space-separated elements row-wise, use -1 for infinity):")
graph = []
for _ in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

# Source vertex input
src = int(input("Enter the source vertex: "))

dijkstra(graph, src, V)
