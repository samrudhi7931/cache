def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}  # Store distance from starting node
    parents = {}  # Map of parents for path reconstruction

    # Distance of starting node from itself is zero
    g[start_node] = 0 #start_node to zero (since the cost to reach itself is zero).
    parents[start_node] = start_node

    while open_set: #The while loop continues until there are no nodes left to explore in open_set
        n = None
        # Node with lowest f() is found
        for v in open_set:#A for loop iterates through all nodes in open_set, choosing the node with the lowest f(n) value.
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node:
            path = []
            while parents[n] != n:#A path list is constructed by tracing the parent nodes from stop_node back to start_node
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path #The path is reversed to show the order from start to goal and returned

        for (m, weight) in get_neighbors(n):#The neighbors of n are evaluated using get_neighbors, which returns adjacent nodes and their edge weights
            if m not in open_set and m not in closed_set:#If a neighbor m is neither in open_set nor closed_set, it’s added to open_set, and the cost and parent values are updated
                open_set.add(m) #If m is already in one of the sets, it checks if a shorter path to m has been found. If so, it updates g[m] and the parent of m, then moves m back to open_set
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n) #After processing all neighbors, n is moved from open_set to closed_set, marking it as fully evaluated

    print('Path does not exist!')
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, []) #get_neighbors retrieves the neighbors of a given node from a predefined graph dictionary, Graph_nodes

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist.get(n, float('inf'))

# Define the graph
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Run the A* algorithm
aStarAlgo('A', 'G')
#output:
#Path found: ['A', 'E', 'D', 'G']
