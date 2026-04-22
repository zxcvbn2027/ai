def dfs_path(graph, start, goal):
    stack = [start]
    processed = []
    parent = {start: None}
    step = 0

    print(f"{'Step':<5}{'Popped':<8}{'Stack (STK)':<25}{'Processed'}")
    print("-" * 65)

    while stack:
        node = stack.pop()

        if node not in processed:
            processed.append(node)

            print(f"{step:<5}{node:<8}{str(stack):<25}{processed}")
            step += 1

            if node == goal:
                print("\nGoal node found!")
                break

            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in processed and neighbor not in stack:
                    stack.append(neighbor)
                    parent[neighbor] = node

    path = []

    if goal in processed:
        curr = goal
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

    return path


graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['E']
}

path = dfs_path(graph, 'A', 'G')

print("\nDFS Path from A to G:")
print(" → ".join(path))