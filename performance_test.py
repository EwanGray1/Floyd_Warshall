import timeit
from FloydAlgo_gfg import floydWarshall

# Test with a small graph
graph_small = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]
time_small = timeit.timeit(lambda: floydWarshall(graph_small), number=1000)
print("Execution time (small graph):", time_small)

# Test with a large graph
graph_large = [[float('inf')] * 100 for _ in range(100)]
time_large = timeit.timeit(lambda: floydWarshall(graph_large), number=10)
print("Execution time (large graph):", time_large)
