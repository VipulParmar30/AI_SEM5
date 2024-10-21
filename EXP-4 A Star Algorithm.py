from queue import PriorityQueue

def a_star(graph, start, goal, h):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current, None)
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + h[neighbor]
                open_list.put((priority, neighbor))
                came_from[neighbor] = current
    return None

# Different example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

# Heuristic function for the different graph
h = {
    'A': 7, 'B': 6, 'C': 3, 'D': 4, 
    'E': 2, 'F': 1, 'G': 0
}

print(a_star(graph, 'A', 'G', h))
