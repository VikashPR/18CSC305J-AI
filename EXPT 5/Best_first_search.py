from queue import PriorityQueue

class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = []

    def __lt__(self, other):
        return False  # Required to make PriorityQueue work with custom objects

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def successors(self, capacities):
        successors = []
        # Empty x
        successors.append(State(0, self.y))
        # Empty y
        successors.append(State(self.x, 0))
        # Fill x
        successors.append(State(capacities[0], self.y))
        # Fill y
        successors.append(State(self.x, capacities[1]))
        # Pour x into y
        y = self.x + self.y
        x = 0
        if y > capacities[1]:
            x = y - capacities[1]
            y = capacities[1]
        successors.append(State(x, y))
        # Pour y into x
        x = self.x + self.y
        y = 0
        if x > capacities[0]:
            y = x - capacities[0]
            x = capacities[0]
        successors.append(State(x, y))
        return successors

def best_first_search(start, goal, capacities):
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()
    while not queue.empty():
        cost, state = queue.get()
        if state == goal:
            return state.path
        visited.add(state)
        for succ in state.successors(capacities):
            if succ not in visited:
                succ.path = state.path + [succ]
                queue.put((heuristic(succ, goal), succ))
    return None

def heuristic(state, goal):
    # A heuristic function that estimates the number of steps to reach the goal
    # The maximum amount of water that can be poured is the sum of the two jug capacities
    return abs(state.x - goal.x) + abs(state.y - goal.y)

# Example usage:
start = State(0, 0)
goal = State(4, 0)
capacities = [5, 3]
path = best_first_search(start, goal, capacities)
if path is not None:
    print("Steps to reach the goal:")
    for state in path:
        print(state.x, state.y)
else:
    print("Goal is unreachable.")
