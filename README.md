# FLoyd-Warshall Adaptation With Recursion

This repository makes changes to the Floyd-Warshall algorithm, which is used to find the shortest path between two nodes in a graph. The changes utilise recursive methods. We compare the traditional approach to the recursive method.

## Repository Contents

- `.flake8`: Code quality check - ensuring PEP-8 standards are adhered to.
- `FloydAlgo_Recursion.py`: The recursive adaptation of the traditional algorithm.
- `FloydAlgo_gfg.py`: The original algorithm from https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/.
- `requirements.txt`: Required packages for the repository to run.
- `unit_test.py`: Tests to ensure that the recursive algorithm is correctly implemented.
- `performance_test.py`: Scripts to compare efficiency of the two algorithms on different graph sizes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EwanGray1/Floyd_Warshall.git
   ```

2. Navigate to the project directory:
   ```bash
   cd floyd-warshall-algorithm
   ```
   
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Floyd-Warshall algorithm, you can import the `floyd_warshall` function from the `floyd_warshall.py` file and pass an adjacency matrix representation of the graph to it. Here's an example:

```python
from FloydAlgo_Recursion import floyd_warshall

# Example graph
graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

# Compute shortest distances
shortest_distances = floyd_warshall(graph)
print("Shortest Distances:")
for row in shortest_distances:
    print(row)
```

## Testing

Unit tests cover various scenarios to ensure the Floyd-Warshall algorithm's correctness:
- Small graphs with direct paths and paths requiring intermediate vertices.
- Fully connected graphs with varied edge weights to test the algorithm's consistency across all node pairs.
- Large graphs to assess the algorithm's scalability and performance.

To run the tests, execute the following command:

```bash
python -m unittest unit_test
```

## Performance Insights

The performance tests compare the recursive and traditional implementations across different graph sizes:

Small Graphs: Performance metrics show how each implementation handles dense connectivity.

Large Graphs: Tests assess scalability and execution time as graph size approaches real-world complexity levels.

Performance results indicate that the recursive method may perform slower on very large graphs but offers competitive performance for small to medium-sized graphs.

Run the performance tests with:

```bash
python performance_test.py
```

## Code Quality Checks

To ensure that the code adheres to Python's PEP 8 style guide, run `flake8`:

```bash
flake8
```
