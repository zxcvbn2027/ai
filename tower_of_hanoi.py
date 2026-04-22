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
                neighbors.append((tuple(temp[0]), tuple(temp[1]), tuple(temp[2])))

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
    path = [current]
    visited = set()
    visited.add(current)
    sideways = 0

    for _ in range(max_steps):

        if goal(current, n):
            return path, True

        current_h = heuristic(current, n)
        states = get_neighbors(current)

        scored = []
        for s in states:
            if s not in visited:
                scored.append((heuristic(s, n), s))

        if not scored:
            return path, False

        best_h = max(h for h, s in scored)
        best_states = [s for h, s in scored if h == best_h]

        if best_h > current_h:
            current = random.choice(best_states)
            sideways = 0

        elif best_h == current_h and sideways < sideways_limit:
            current = random.choice(best_states)
            sideways += 1

        else:
            return path, False

        visited.add(current)
        path.append(current)

    return path, False


def show(state):
    print("A:", list(state[0]), " B:", list(state[1]), " C:", list(state[2]))


n = int(input("Enter number of disks: "))

start = (tuple(range(n, 0, -1)), tuple(), tuple())

path, success = hill_climb(start, n)

print("\nStart State:")
show(start)

print("\nSteps:\n")
for i, state in enumerate(path):
    print("Step", i)
    show(state)

if success:
    print("\nGoal Reached")
else:
    print("\nStuck in Local Optimum")