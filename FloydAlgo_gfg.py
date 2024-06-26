# Python3 Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as a large enough value. This value will be used for vertices not connected to each other
INF = 99999


def floydWarshall(graph):
    """dist[][] will be the output matrix that will finally have the shortest distances
    between every pair of vertices"""
    """initializing the solution matrix same as input graph matrix
    OR we can say that the initial values of shortest distances are
    based on shortest paths considering no intermediate vertices
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))"""

    # Add all vertices one by one to the set of intermediate vertices.
    for k in range(V):
        # Pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()
