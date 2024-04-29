# Floyd-Warshall Algorithm Implementations

This repository contains two Python implementations of the Floyd-Warshall algorithm, which is used to find the shortest paths between all pairs of nodes in a given weighted graph. The implementations include a traditional approach and a variant using recursive techniques.

## Repository Contents

- `FloydAlgo_Recursion.py`: An implementation of the Floyd-Warshall algorithm emphasizing a recursive approach.
- `FloydAlgo_gfg.py`: A traditional implementation of the algorithm adapted from GeeksforGeeks.
- `requirements.txt`: Lists dependencies required to run the code in this repository.
- `unit_test.py`: Contains unit tests for verifying the correctness of both implementations.
- `performance_test.py`: Scripts to measure the performance of the algorithms with different graph sizes.

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

Unit tests for the Floyd-Warshall algorithm are included in the `test_floyd_warshall.py` file. You can run the tests using the following command:

```bash
python -m unittest unit_test
```

## Performance Testing
Performance tests for the algorithm are included in the performance_test.py file. Run the performance tests to evaluate the algorithm's efficiency.

## Version Control
This project uses Git for version control. You can initialize a Git repository for your own use and track changes to the codebase. Here's how to set it up:

1.Initialize a new Git repository:
```bash
git init
```
2.Add the project files to Git:
```bash
git add .
```
3.Commit the initial changes:
```bash
git commit -m "Initial commit: Added Floyd-Warshall algorithm using recursion implementation"
```
4.Push the changes:
```bash
git push origin <branch>
```
