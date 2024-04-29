# Comparing Traditional Floyd-Warshall Algorithm with Recursive Adaptation

This repository investigates the performance of the Floyd-Warshall algorithm. This is used to find the shortest route between nodes in a graph. We have made adaptations to the original algorithm to use recursive methods. We compare the performance of the two algorithms on graphs of different sizes. 

## Repository Contents

- `.flake8`: Used to ensure code adheres to PEP standards.
- `FloydAlgo_Recursion.py`: Our adapted algorithm, using recursive methods.
- `FloydAlgo_gfg.py`: The original algorithm, found at https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/.
- `requirements.txt`: Packages required to run the algorithm tests.
- `unit_test.py`: Tests to ensure that functions are performing as they should be.
- `performance_test.py`: Tests to compare the two algorithms on graphs of different sizes.

## Installation

Below is an explanation of how to install and run the algorithms.

1. Repository Clone:
   ```bash
   git clone https://github.com/EwanGray1/Floyd_Warshall.git
   ```

2. Move to Repository Directory:
   ```bash
   cd floyd-warshall-algorithm
   ```
   
3. Install Packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Floyd-Warshall algorithm, you can import the `floyd_warshall` function from the `floyd_warshall.py` file and pass an adjacency matrix representation of the graph to it. Here's an example:

To use the recursive algorithm on a graph of your own, you can import `floyd_warshall` function from the `floyd_warshall.py` file in the repository and pass a graph into it, in  matrix form. An example of how to do this is shown below:

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


We run unit tests to ensure that the algorithm is functioning as expected, we have covered several potential scenarios in our unit tests:
- Small graphs which are both dense and sparse, to ensure correct handling of intermediate nodes.
- Graphs which are completely connected, but have a variety of weights, to ensire consistent calculation of different node pairs.
- Graphs which are large in size, to ensure the algorithm is scalable.

To improve unit tests, we could have included tests for more edge cases, such as:
- Graphs with negative weights.
- Graphs with no weights.
- Graphs with disconnected nodes.
- Graphs with only one / two vertices.

You can run the following command to run the unit tests:

```bash
python -m unittest unit_test
```

## Performance Insights

We compare the performance of the traditional algorithm with our recursive adaptation of the algorithm. 
Our measures of performance can be seen by running the following command:


```bash
python performance_test.py
```

The performance metrics suggest that there is no efficiency improvement with recursive methods, efficiency is competitive in smaller graphs, but the traditional method is far superior as graph size increases. 

## Code Quality Checks

We have implemented code quality checks, to ensure that PEP standards are adhered to, run `flake8`:

```bash
flake8
```
