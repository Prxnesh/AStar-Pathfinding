import heapq
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  
        self.h = h  
        self.f = g + h  

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal, visualize=True):
    """A* Algorithm with real-time visualization."""
    open_list = []
    closed_set = set()
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    visited_nodes = []
    current_path = []

    if visualize:
        plt.figure(figsize=(10, 10))
        draw_grid(grid, start, goal, path=[], visited=[])
        plt.pause(1)

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            path.reverse()

            if visualize:
                draw_grid(grid, start, goal, path, visited_nodes)
                plt.show()

            return path

        closed_set.add(current.position)
        visited_nodes.append(current.position)

        # Track current path for visualization
        temp = current
        current_path = []
        while temp:
            current_path.append(temp.position)
            temp = temp.parent
        current_path.reverse()

        if visualize:
            draw_grid(grid, start, goal, path=current_path, visited=visited_nodes)
            plt.pause(0.05)  

        x, y = current.position

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            new_pos = (x + dx, y + dy)
            if new_pos in closed_set:
                continue

            if not (0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0])):  
                continue

            if grid[new_pos[0]][new_pos[1]] == 1:  
                continue

            new_node = Node(new_pos, current, current.g + 1, heuristic(new_pos, goal))
            heapq.heappush(open_list, new_node)

    return None 

def draw_grid(grid, start, goal, path, visited):
    """Draws the grid with updated colors for real-time visualization."""
    grid_copy = np.array(grid)

    plt.clf()
    plt.imshow(grid_copy, cmap="gray_r")  

    # Mark start and goal with distinct colors
    plt.scatter(start[1], start[0], c="purple", marker="o", label="Start", edgecolors="black", s=120)  
    plt.scatter(goal[1], goal[0], c="gold", marker="o", label="Goal", edgecolors="black", s=120)  

    # Change visited nodes to orange
    for v in visited:
        plt.scatter(v[1], v[0], c="orange", s=20, alpha=0.7)  

    # Change path nodes to blue with a white outline
    if path:
        for p in path:
            plt.scatter(p[1], p[0], c="blue", s=50, edgecolors="white", linewidth=1)  

    plt.legend()
    plt.xticks(range(0, len(grid[0]), max(1, len(grid[0]) // 10)))
    plt.yticks(range(0, len(grid), max(1, len(grid) // 10)))
    plt.grid(True)
    plt.pause(0.05)

# ✅ Allow user to set grid size
grid_size = int(input("Enter grid size (default 25): ") or 25)

# ✅ Allow user to set obstacle density
obstacle_density = float(input("Enter obstacle probability (0 to 1, default 0.25): ") or 0.25)

# Generate a random grid with user-defined size
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[1 - obstacle_density, obstacle_density])

# Ensure start and goal positions are open
grid[0][0] = 0  
grid[grid_size - 1][grid_size - 1] = 0  

start = (0, 0)  
goal = (grid_size - 1, grid_size - 1)  

path = astar(grid, start, goal, visualize=True)

if path:
    print("Shortest Path:", path)
else:
    print("No path found!")
