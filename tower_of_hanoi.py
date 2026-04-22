import random
from copy import deepcopy


def valid_move(src, dst):
    if not src:
        return False
    if not dst:
        return True
    return src[-1] < dst[-1]


def get_neighbors(state):
    rods = [list(state[0]), list(state[1]), list(state[2])]
    neighbors = []

    for i in range(3):
        for j in range(3):
            if i != j and valid_move(rods[i], rods[j]):
                temp = deepcopy(rods)
                disk = temp[i].pop()
                temp[j].append(disk)
                neighbors.append(((tuple(temp[0]), tuple(temp[1]), tuple(temp[2])), i, j))

    return neighbors


def heuristic(state, n):
    goal = list(range(n, 0, -1))
    c = list(state[2])
    count = 0

    for i in range(min(len(c), n)):
        if c[i] == goal[i]:
            count += 1
        else:
            break

    return count


def goal(state, n):
    return state[2] == tuple(range(n, 0, -1))


def hill_climb(start, n, sideways_limit=50, max_steps=1000):
    current = start
    path = [(current, "Start")]
    visited = set()
    visited.add(current)
    sideways = 0

    rods = ['A', 'B', 'C']

    for _ in range(max_steps):

        if goal(current, n):
            return path, True

        current_h = heuristic(current, n)
        states = get_neighbors(current)

        scored = []
        for s, i, j in states:
            if s not in visited:
                scored.append((heuristic(s, n), s, i, j))

        if not scored:
            return path, False

        best_h = max(x[0] for x in scored)
        best_states = [x for x in scored if x[0] == best_h]

        if best_h > current_h:
            chosen = random.choice(best_states)
            sideways = 0

        elif best_h == current_h and sideways < sideways_limit:
            chosen = random.choice(best_states)
            sideways += 1

        else:
            return path, False

        current = chosen[1]
        move_text = rods[chosen[2]] + " -> " + rods[chosen[3]]

        visited.add(current)
        path.append((current, move_text))

    return path, False


def show(state):
    print("A:", list(state[0]), " B:", list(state[1]), " C:", list(state[2]))


n = int(input("Enter number of disks: "))

start = (tuple(range(n, 0, -1)), tuple(), tuple())

path, success = hill_climb(start, n)

print("\nSteps:\n")

for i, (state, move) in enumerate(path):
    print("Step", i)
    print("Move:", move)
    show(state)
    print("-" * 25)

if success:
    print("Goal Reached")
else:
    print("Stuck in Local Optimum")