import heapq

# Define the example graph
graph = {
    'A': {'heuristic': 10, 'neighbors': {'B': 6, 'F': 3}},
    'B': {'heuristic': 8, 'neighbors': {'A': 6, 'D': 2, 'C': 3}},
    'C': {'heuristic': 5, 'neighbors': {'B': 3, 'D': 1, 'E': 5}},
    'D': {'heuristic': 7, 'neighbors': {'B': 2, 'C': 1, 'E': 8}},
    'E': {'heuristic': 3, 'neighbors': {'C': 5, 'D': 8, 'I': 5, 'J': 5}},
    'F': {'heuristic': 6, 'neighbors': {'A': 3, 'H': 7}},
    'G': {'heuristic': 5, 'neighbors': {'F': 1, 'I': 3}},
    'H': {'heuristic': 3, 'neighbors': {'F': 7, 'I': 2}},
    'I': {'heuristic': 1, 'neighbors': {'G': 3, 'E': 5, 'H': 2, 'J': 3}},
    'J': {'heuristic': 0, 'neighbors': {'E': 5, 'I': 3}}
}


def greedy_bfs(graph, start, goal):
    visited = set()
    heap = [(graph[start]['heuristic'], start, [start])]
    while heap:
        (h, current_node, path) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return path
        for neighbor, distance in graph[current_node]['neighbors'].items():
            if neighbor not in visited:
                heapq.heappush(
                    heap, (graph[neighbor]['heuristic'], neighbor, path + [neighbor]))
    return None


def astar_search(graph, start, goal):
    for node in graph:
        graph[node]['g'] = float('inf')
        graph[node]['parent'] = None
    graph[start]['g'] = 0

    visited = set()
    heap = [(0, start, [start])]
    while heap:
        (f, current_node, path) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return path
        for neighbor, distance in graph[current_node]['neighbors'].items():
            g = graph[current_node]['g'] + distance
            h = graph[neighbor]['heuristic']
            f = g + h
            if g < graph[neighbor]['g']:
                graph[neighbor]['g'] = g
                graph[neighbor]['parent'] = current_node
                heapq.heappush(heap, (f, neighbor, path + [neighbor]))
    return None


# Test the functions on the example graph
start = 'A'
goal = 'J'

greedy_path = greedy_bfs(graph, start, goal)
if greedy_path:
    print("Greedy Best-First Search path:", greedy_path)


astar_path = astar_search(graph, start, goal)
if astar_path:
    print("A* Search path:", astar_path)
