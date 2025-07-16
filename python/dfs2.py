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

# Add edges to the graph
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

# Define layout (Try 'shell_layout' or 'kamada_kaway_layout' for better aesthetics)
pos = nx.shell_layout(G)  # Circular shell layout for clear levels
pos = nx.kamada_kawai_layout(G)  # Alternative: Neat force-directed layout
# Draw the graph with styling
plt.figure(figsize=(10, 7))
nx.draw(
    G, pos, with_labels=True, node_color="lightcoral", edge_color="black", 
    node_size=2500, font_size=14, font_weight="bold", linewidths=2, 
    edgecolors="black", arrowsize=25, width=2
)
plt.title("Improved Graph Visualization", fontsize=15, fontweight="bold")
plt.show()