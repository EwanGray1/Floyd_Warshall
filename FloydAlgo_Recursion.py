
def floyd_warshall(graph):
    """
    Applies Floyd-Warshall algorithm to find the shortest paths in a graph.

    Args:
    - graph: Adjacency matrix representation of the graph

    Returns:
    - dist: Matrix of shortest distances between every pair of vertices
    """

    # Number of vertices in the graph
    V = len(graph)
    # Initialize the distance matrix with the input graph
    dist = [[float('inf')] * V for _ in range(V)]

    # Initialize diagonal elements as 0 since distance from a vertex to itself is 0
    for i in range(V):
        dist[i][i] = 0

    # Update the distance matrix with the input graph's edges
    for u in range(V):
        for v in range(V):
            if graph[u][v] != float('inf'):
                dist[u][v] = graph[u][v]

    # Apply Floyd-Warshall algorithm to find the shortest paths
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def main():
    # Example usage
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    shortest_distances = floyd_warshall(graph)
    print("Shortest Distances:")
    for row in shortest_distances:
        print(row)


if __name__ == "__main__":
    main()
