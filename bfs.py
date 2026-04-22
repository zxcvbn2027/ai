from collections import deque
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['E']
}
def bfs(graph, start, goal):
    Q1 = deque()        
    Q2 = []             
    parent = {}          
    Q1.append(start)
    parent[start] = None
    print(f"{'Step':<5}{'Removed':<10}{'Q1 (To be processed)':<30}{'Q2 (Processed)'}")
    print("-" * 80)
    step = 0
    while Q1:
        current = Q1.popleft() 
        Q2.append(current)     
        print(f"{step:<5}{current:<10}{str(list(Q1)):<30}{Q2}")
        step += 1
        if current == goal:
            print("\nGoal node found!")
            break
        for neighbor in graph[current]:
            if neighbor not in Q1 and neighbor not in Q2:
                Q1.append(neighbor)
                parent[neighbor] = current
    path = []
    if goal in Q2:
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
    return path
path = bfs(graph, 'A', 'E')
print("\nBFS Path from A to E:")
print(" → ".join(path))
