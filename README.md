# Floyd-Warshall Algorithm with Recursive Methods

This is an adaptation of the Floyd-Warshall algorithm, using recursive methods to find the shortest path between two nodes in a graph.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EwanGray1/Floyd_Warshall.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Floyd_Warshall
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
