class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start):
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)

    def dfs_recursive(self, start):
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)

    

# Example usage:
g = Graph()
# Dynamically input edges
while True:
    edge = input("Enter an edge (format: 'u v'), or enter 'done' to finish: ")
    if edge == "done":
        break
    u, v = map(int, edge.split())
    g.add_edge(u, v)

print("BFS traversal:")
g.bfs(0)  # Starting BFS from node 0

print("\nDFS traversal:")
g.dfs(0)  # Starting DFS from node 0

print("\nDFS recursive traversal:")
g.dfs_recursive(0)  # Starting DFS recursive from node 0

