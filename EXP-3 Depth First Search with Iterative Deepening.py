def dfs_iterative_deepening(graph, start, goal):
    def dfs_limited(node, goal, depth):
        if depth == 0 and node == goal:
            return [node]
        if depth > 0:
            for neighbor in graph.get(node, []):
                path = dfs_limited(neighbor, goal, depth - 1)
                if path:
                    return [node] + path
        return None

    for depth in range(len(graph)):
        result = dfs_limited(start, goal, depth)
        if result:
            return result
    return None

# Different example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H', 'I'],
    'G': [],
    'H': [],
    'I': []
}

print(dfs_iterative_deepening(graph, 'A', 'I'))
