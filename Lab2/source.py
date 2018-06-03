GRAPH = {
    "A": {"C": 1, "D": 2},
    "B": {"C": 2, "F": 3},
    "C": {"A": 1, "B": 2, "D": 1, "E": 3},
    "D": {"A": 2, "C": 1, "G": 1},
    "E": {"C": 3, "F": 2},
    "F": {"B": 3, "E": 2, "G": 1},
    "G": {"D": 1, "F": 1}}


def dijkstra(graph, source, destination):
    unvisited = {vertex: float('inf') for vertex in graph.keys()}
    visited = {}
    previous = {}
    unvisited[source] = 0

    while unvisited:
        unvisited_neighbors = [vertex for vertex in unvisited.items() if vertex[1] < float('inf')]
        current_vertex, current_distance = min(unvisited_neighbors, key=lambda x: x[1])
        for neighbor, distance in graph[current_vertex].items():
            if neighbor in unvisited:
                if current_distance + distance < unvisited[neighbor]:
                    unvisited[neighbor] = current_distance + distance
                    previous[neighbor] = current_vertex
        visited[current_vertex] = current_distance
        del unvisited[current_vertex]

    path = [destination]
    while path[-1] != source:
        path.append(previous[path[-1]])

    return path[::-1], visited[destination]


print('Najkrótsza trasa: %s, koszt: %s' % dijkstra(GRAPH, 'A', 'F'))
