import heapq
goal_state = (1, 2, 3,
              8, 0, 4,
              7, 6, 5)
moves = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}
def manhattan(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal_state.index(state[i])
            h += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return h
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    for move, shift in moves.items():
        new_pos = zero + shift
        if move == 'Left' and zero % 3 == 0:
            continue
        if move == 'Right' and zero % 3 == 2:
            continue
        if 0 <= new_pos < 9:
            new_state = list(state)
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
            neighbors.append((tuple(new_state), move))
    return neighbors
def a_star(start):
    pq = []
    h0 = manhattan(start)
    heapq.heappush(pq, (h0, 0, start, [("Start", start, 0, h0, h0)]))
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [("Goal", state, g, 0, g)]
        if state in visited:
            continue
        visited.add(state)
        for next_state, move in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_h = manhattan(next_state)
                new_f = new_g + new_h
                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state,
                     path + [(move, next_state, new_g, new_h, new_f)])
                )
    return None
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
def main():
    start_state = (2, 8, 3,
                   1, 6, 4,
                   7, 0, 5)
    result = a_star(start_state)
    if result:
        step = 0
        for move, state, g, h, f in result:
            print(f"Step {step}")
            print("Move:", move)
            print_state(state)
            print(f"g = {g}, h = {h}, f = {f}")
            print("-" * 25)
            step += 1
    else:
        print("No solution found")
main()
