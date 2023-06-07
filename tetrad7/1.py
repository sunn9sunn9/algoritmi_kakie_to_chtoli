import sys


def dijkstra(graph, src):
    num_vertices = len(graph)
    dist = [sys.maxsize] * num_vertices
    dist[src] = 0
    shortest_path_set = [False] * num_vertices

    for _ in range(num_vertices):
        u = min_distance(dist, shortest_path_set)
        shortest_path_set[u] = True

        for v in range(num_vertices):
            if (graph[u][v] > 0 and
                    shortest_path_set[v] == False and
                    dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]

    return dist


def min_distance(dist, shortest_path_set):
    min_val = sys.maxsize
    for v in range(len(dist)):
        if dist[v] < min_val and shortest_path_set[v] == False:
            min_val = dist[v]
            min_index = v

    return min_index


def print_solution(dist):
    print("Vertex \t\t Distance from Source")
    for i in range(len(dist)):
        print(f"{i} \t\t {dist[i]}")


graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

dist = dijkstra(graph, 0)
print_solution(dist)
