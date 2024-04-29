import unittest
from FloydAlgo_Recursion import floyd_warshall


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        # Test case 1: Small graph
        graph1 = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        expected1 = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(floyd_warshall(graph1), expected1)

        # Test case 2: Large graph
        graph2 = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        expected2 = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(floyd_warshall(graph2), expected2)

        # Test case 3: Graph with loops (self-edges)
        graph3 = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        expected3 = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(floyd_warshall(graph3), expected3)

        # Test case 5: Empty graph
        graph5 = []
        expected5 = []
        self.assertEqual(floyd_warshall(graph5), expected5)

if __name__ == '__main__':
    unittest.main()

