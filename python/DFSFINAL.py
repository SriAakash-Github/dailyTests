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
import time

# Define the graph
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

# Create a directed graph in NetworkX
G = nx.DiGraph()

# Add edges to the graph
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

# Define layout for better spacing
pos = nx.spring_layout(G, seed=42)

def dfs_visual(graph, start):
    visited = set()
    stack = [start]

    plt.figure(figsize=(8, 6))

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            # Clear and redraw graph
            plt.clf()
            nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray",
                    node_size=2500, font_size=14, font_weight="bold", arrows=True, width=2)

            # Highlight visited nodes in DFS order
            nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color="lightblue", node_size=2500)

            # Update plot
            plt.title(f"DFS Traversal: {' → '.join(visited)}", fontsize=14)
            plt.pause(1)  # Pause to visualize each step

            # Push neighbors onto stack (in reverse order for correct DFS order)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    plt.show()

# Run DFS Visualization
dfs_visual(graph, 'A')