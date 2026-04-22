import heapq

class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost


def a_star(graph, h, start, goal):
    n = len(graph)
    INF = float('inf')

    g = [INF] * n
    parent = [-1] * n
    pq = []

    g[start] = 0
    heapq.heappush(pq, (h[start], start))

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current != -1:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for edge in graph[current]:
            nxt = edge.to
            cost = g[current] + edge.cost

            if cost < g[nxt]:
                g[nxt] = cost
                parent[nxt] = current
                heapq.heappush(pq, (cost + h[nxt], nxt))

    return []


n = 12
graph = [[] for _ in range(n)]

graph[0] = [Edge(1, 4), Edge(2, 10), Edge(3, 11)]
graph[1] = [Edge(2, 8), Edge(4, 5)]
graph[2] = [Edge(4, 15)]
graph[3] = [Edge(4, 8), Edge(5, 20), Edge(6, 2)]
graph[4] = [Edge(6, 1), Edge(8, 16), Edge(9, 20)]
graph[5] = [Edge(7, 19)]
graph[6] = [Edge(7, 13)]
graph[8] = [Edge(9, 1), Edge(10, 2)]
graph[9] = [Edge(7, 5), Edge(10, 5), Edge(11, 13)]
graph[10] = [Edge(11, 7)]
graph[11] = [Edge(7, 16)]

h = [7, 8, 6, 5, 5, 3, 3, 0, 7, 4, 5, 3]

start = 0
goal = 7

path = a_star(graph, h, start, goal)

labels = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

print("Path found:")
for i, node in enumerate(path):
    print(labels[node], end="")
    if i != len(path) - 1:
        print(" -> ", end="")
print()