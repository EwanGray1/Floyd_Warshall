import unittest
from FloydAlgo_Recursion import floyd_warshall as floyd_warshall_recursive
from FloydAlgo_gfg import floydWarshall as floyd_warshall_gfg

class TestFloydWarshall(unittest.TestCase):
    def test_small_graph(self):
        """
        Test both implementations on a small graph.
        This graph includes a mix of direct edges and paths that require intermediate vertices.
        Expected outcome: Both functions should compute identical shortest path matrices.
        """
        graph = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        expected = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result_recursive = floyd_warshall_recursive(graph)
        result_gfg = floyd_warshall_gfg(graph)
        self.assertEqual(result_recursive, expected)
        self.assertEqual(result_gfg, expected)
        self.assertEqual(result_recursive, result_gfg)

    def test_fully_connected_graph(self):
        """
        Test both implementations on a fully connected graph with varied edge weights.
        Expected outcome: Both functions should compute identical shortest path matrices.
        """
        graph = [
            [0, 1, 2, 3],
            [1, 0, 4, 2],
            [2, 4, 0, 1],
            [3, 2, 1, 0]
        ]
        expected = [
            [0, 1, 2, 3],
            [1, 0, 3, 2],
            [2, 3, 0, 1],
            [3, 2, 1, 0]
        ]
        result_recursive = floyd_warshall_recursive(graph)
        result_gfg = floyd_warshall_gfg(graph)
        self.assertEqual(result_recursive, expected)
        self.assertEqual(result_gfg, expected)
        self.assertEqual(result_recursive, result_gfg)

    def test_large_graph(self):
        """
        Test both implementations on a large graph to check for efficiency and correctness.
        Expected outcome: Both functions should handle large graphs, but efficiency might differ.
        """
        graph = [[float('inf')] * 50 for _ in range(50)]
        for i in range(50):
            for j in range(50):
                if i != j:
                    graph[i][j] = i + j
        
        result_recursive = floyd_warshall_recursive(graph)
        result_gfg = floyd_warshall_gfg(graph)
        self.assertEqual(result_recursive, result_gfg)

if __name__ == '__main__':
    unittest.main()
