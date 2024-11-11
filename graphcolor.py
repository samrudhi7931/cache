class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.V = len(graph)
        self.num_colors = num_colors
        self.colors = [-1] * self.V

    def is_safe(self, v, color):
        # Check if the current color can be assigned to vertex v
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.colors[i] == color:
                return False
        return True

    def solve_graph_coloring(self, v):
        # If all vertices are assigned a color
        if v == self.V:
            return True

        # Try different colors for vertex v
        for color in range(self.num_colors):
            if self.is_safe(v, color):
                self.colors[v] = color
                # Recur to assign colors to the rest of the vertices
                if self.solve_graph_coloring(v + 1):
                    return True
                # Backtrack
                self.colors[v] = -1

        return False

    def get_coloring(self):
        # Start solving from the first vertex
        if self.solve_graph_coloring(0):
            return self.colors
        else:
            return None


# Define the graph as an adjacency matrix
graph = [[0, 1, 1, 1],  # Vertex 0 connected to 1, 2, 3
         [1, 0, 0, 1],  # Vertex 1 connected to 0 and 3
         [1, 0, 0, 1],  # Vertex 2 connected to 0 and 3
         [1, 1, 1, 0]]  # Vertex 3 connected to 0, 1, 2
num_colors = 3

# Create an instance of the GraphColoring class
coloring = GraphColoring(graph, num_colors)
result = coloring.get_coloring()

# Display the results with vertex numbers using backtracking
if result:
    print("Coloring of graph:")
    for vertex in range(len(result)):
        print(f"Vertex {vertex}: Color {result[vertex]}")
else:
    print("No solution exists.")


