import sys

def min_key(key, mst_set, V):
    min_val = sys.maxsize
    min_index = -1
    for v in range(V):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v
    return min_index

def print_mst(parent, graph, V):
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

def prim_mst(graph, V):
    parent = [-1] * V  
    key = [sys.maxsize] * V
    mst_set = [False] * V

    key[0] = 0  # Start from the first vertex

    for _ in range(V):
        u = min_key(key, mst_set, V)  # Pick the minimum key vertex from the set of vertices not yet included in MST
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mst_set[v] and key[v] > graph[u][v]:
                parent[v] = u
                key[v] = graph[u][v]

    print_mst(parent, graph, V)

# Dynamic input from the user for array length
V = int(input("Enter the number of vertices: "))

# Dynamic input for the adjacency matrix representing the graph
print("Enter the adjacency matrix (space-separated elements row-wise):")
graph = []
for _ in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph, V)
