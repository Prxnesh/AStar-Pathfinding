# A* Pathfinding Algorithm with Visualization

## Overview

This repository contains two implementations of the **A* (A-star) pathfinding algorithm** in Python, with real-time visualization using **Matplotlib**. The A* algorithm is widely used for pathfinding in AI, robotics, and game development due to its efficiency in finding the shortest path in a weighted grid.

Both implementations allow users to specify a grid size and obstacle density, then visualize the algorithm's progress in real-time.

---

## Features

- **A* Algorithm Implementation**: Finds the shortest path in a randomly generated grid.
- **Visualization**: Uses Matplotlib to visualize the search process dynamically.
- **Customizable Grid**: Users can specify grid size and obstacle density.
- **Optimized Version**: The second implementation improves efficiency by using a dictionary (`closed_dict`) for faster lookups.

---

## Installation

### Prerequisites

Ensure you have Python installed along with the following dependencies:

```bash
pip install numpy matplotlib
```

---

## Usage

Run the script in a Python environment:

```bash
python astar.py
```

During execution, you will be prompted to enter:

- **Grid Size** (default: `25x25`)
- **Obstacle Probability** (default: `0.25`, range: `0.0 - 1.0`)

The algorithm will generate a grid, execute A*, and visualize the process.

---

## Algorithm Explanation

A* is a pathfinding algorithm that finds the shortest path between a start and a goal node using the formula:

```plaintext
f(n) = g(n) + h(n)
```

Where:

- `g(n)`: Cost from the start node to the current node.
- `h(n)`: Heuristic estimate from the current node to the goal (Manhattan distance in this implementation).
- `f(n)`: Total estimated cost of the path.

The algorithm uses a priority queue (min-heap) to always expand the node with the lowest `f(n)` value.

---

## Visualization

- **Start Node**: 🟣 (Purple)
- **Goal Node**: 🟡 (Gold)
- **Visited Nodes**: 🟠 (Orange)
- **Final Path**: 🔵 (Blue with white outline)

---

## Differences Between Implementations

| Feature            | Basic Implementation | Optimized Implementation |
|--------------------|----------------------|--------------------------|
| **Data Structures**   | Uses `set` for closed nodes | Uses `dict` for faster lookups |
| **Performance**       | Slower due to redundant checks | Faster with optimized storage |
| **Visualization**     | Updates frequently | Skips frames for better performance |

---

## Example Output

```plaintext
Enter grid size (default 25): 30
Enter obstacle probability (0 to 1, default 0.25): 0.2
Shortest Path: [(0,0), (1,0), (2,0), ..., (29,29)]
```

A visualization of the search process will be displayed.

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by Pranesh D. Contributions are welcome!
