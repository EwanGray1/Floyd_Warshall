import timeit
from FloydAlgo_refactored import FloydWarshallRecursive, FloydWarshallGfG


def test_performance(algorithm, graph, number_of executions=10):
    """
    Helper function to measure the execution time of a given Floyd-Warshall implementation.
    """
    algo_instance = algorithm(graph)
    return timeit.timeit(lambda: algo_instance.compute(), number=number_of_executions)


def main():
    # Graph definitions
    small_graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]

    large_graph = [[float('inf')] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if i != j:
                large_graph[i][j] = i + j

    # Number of executions
    num_executions_small = 1000
    num_executions_large = 10

    # Performance testing on small graph
    time_small_recursive = test_performance(FloydWarshallRecursive, small_graph, num_executions_small)
    time_small_gfg = test_performance(FloydWarshallGfG, small_graph, num_executions_small)

    # Performance testing on large graph
    time_large_recursive = test_performance(FloydWarshallRecursive, large_graph, num_executions_large)
    time_large_gfg = test_performance(FloydWarshallGfG, large_graph, num_executions_large)

    # Print results
    print(f"Execution time for small graph (Recursive): {time_small_recursive} seconds")
    print(f"Execution time for small graph (Traditional): {time_small_gfg} seconds")
    print(f"Execution time for large graph (Recursive): {time_large_recursive} seconds")
    print(f"Execution time for large graph (Traditional): {time_large_gfg} seconds")


if __name__ == "__main__":
    main()
