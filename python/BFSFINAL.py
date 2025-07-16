from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()  # Remove from the front (FIFO)
        if vertex not in visited:
            print(vertex, end=" ")  # Visit the node
            visited.add(vertex)

            # Enqueue unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
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

print("BFS Traversal:")
bfs(graph, 'A')

import networkx as nx
import matplotlib.pyplot as plt
import time
from collections import deque

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

# Define layout for better clarity
pos = nx.spring_layout(G, seed=42)  # Force-directed layout for spacing

def bfs_visual(graph, start):
    visited = set()
    queue = deque([start])
    
    plt.figure(figsize=(8, 6))
    
    while queue:
        vertex = queue.popleft()  # FIFO: Remove first element
        if vertex not in visited:
            visited.add(vertex)

            # Draw the entire graph
            plt.clf()
            nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", 
                    node_size=2500, font_size=14, font_weight="bold", arrows=True, width=2)

            # Highlight visited nodes in BFS order
            nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color="lightcoral", node_size=2500)
            
            # Update plot
            plt.title(f"BFS Traversal: {' → '.join(visited)}", fontsize=14)
            plt.pause(1)  # Pause to visualize each step

            # Add unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    plt.show()

# Run BFS Visualization
bfs_visual(graph, 'A')