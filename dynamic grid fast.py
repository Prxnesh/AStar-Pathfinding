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
    """Optimized A* Algorithm with faster execution."""
    open_list = []
    open_set = set()  # For O(1) lookup of nodes in open_list
    closed_dict = {}  # Dictionary to store best g-value for each visited node

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    open_set.add(start)

    visited_nodes = []
    current_path = []

    if visualize:
        plt.figure(figsize=(10, 10))
        draw_grid(grid, start, goal, path=[], visited=[])
        plt.pause(0.5)

    while open_list:
        current = heapq.heappop(open_list)
        open_set.remove(current.position)

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

        closed_dict[current.position] = current.g
        visited_nodes.append(current.position)

        # Track current path for visualization
        temp = current
        current_path = []
        while temp:
            current_path.append(temp.position)
            temp = temp.parent
        current_path.reverse()

        # Speed up visualization (skip frames)
        if visualize and len(visited_nodes) % 5 == 0:
            draw_grid(grid, start, goal, path=current_path, visited=visited_nodes)
            plt.pause(0.001)  # Reduced delay

        x, y = current.position

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            new_pos = (x + dx, y + dy)

            if not (0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0])):  
                continue  # Skip out-of-bounds positions

            if grid[new_pos[0]][new_pos[1]] == 1:  
                continue  # Skip obstacles

            new_g = current.g + 1  # Cost to move to new position

            # If we've visited this position with a lower cost, skip it
            if new_pos in closed_dict and closed_dict[new_pos] <= new_g:
                continue  

            new_node = Node(new_pos, current, new_g, heuristic(new_pos, goal))

            # Add to open_list if it's a better path or not visited yet
            if new_pos not in open_set:
                heapq.heappush(open_list, new_node)
                open_set.add(new_pos)

    return None 

def draw_grid(grid, start, goal, path, visited):
    """Efficient grid drawing for real-time visualization."""
    plt.clf()
    plt.imshow(grid, cmap="gray_r")  

    plt.scatter(start[1], start[0], c="purple", marker="o", label="Start", edgecolors="black", s=120)  
    plt.scatter(goal[1], goal[0], c="gold", marker="o", label="Goal", edgecolors="black", s=120)  

    # Use a single scatter for visited nodes to improve performance
    if visited:
        visited_x, visited_y = zip(*visited)
        plt.scatter(visited_y, visited_x, c="orange", s=15, alpha=0.6)  

    # Use a single scatter for path nodes to improve performance
    if path:
        path_x, path_y = zip(*path)
        plt.scatter(path_y, path_x, c="blue", s=50, edgecolors="white", linewidth=1)  

    plt.legend()
    plt.xticks(range(0, len(grid[0]), max(1, len(grid[0]) // 10)))
    plt.yticks(range(0, len(grid), max(1, len(grid) // 10)))
    plt.grid(True)
    plt.pause(0.001)  # Reduce visualization delay

# ✅ User-defined grid size and obstacle density
grid_size = int(input("Enter grid size (default 25): ") or 25)
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
