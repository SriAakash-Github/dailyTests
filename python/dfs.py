def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            # Reverse the neighbors before adding to stack for correct order
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)


# Example usage
graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['F','H','I'],
    'E': ['F'],
    'F': ['G'],
    'G': ['I','L'],
    'H': ['J','L'],
    'I': ['J'],
    'J': ['L'],
    'L': []
}

print("DFS Traversal:")
dfs(graph, 'A')
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['F', 'H', 'I'],
    'E': ['F'],
    'F': ['G'],
    'G': ['I', 'L'],
    'H': ['J', 'L'],
    'I': ['J'],
    'J': ['L'],
    'L': []
}

# Create a directed graph
G = nx.DiGraph()

#Add edges to the graph
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

#Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Positioning nodes

nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=2000, font_size=12, font_weight="bold", arrowsize=20)
plt.title("Graph Visualization using NetworkX")
plt.show()
