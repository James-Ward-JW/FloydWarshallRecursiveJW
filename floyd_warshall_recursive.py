import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]


def shortest_path(s, e, i, d):
    """
    Function to calculate the shortest paths between nodes in a recursive fashion:
    param s = start node,
    param e = end node,
    param i = intermediate node,
    param d = distance
    """
    # Conditional to exit recursion once all intermediate nodes have been checked
    if i < 0:
        return d[s][e]

    # Check all possible paths
    return min(shortest_path(s, e, i - 1, d), shortest_path(s, i, i - 1, d) + shortest_path(i, e, i - 1, d))


def floyd_warshall(distance):

    # Allows for inputs of differing length to be used without having to specify globally
    max_length = len(graph[0])

    # Calculate the various path combinations
    for start_node, end_node in itertools.product(range(max_length), range(max_length)):

        # If start node is the same as the end node, the path between them is zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # Calls shortest_path function to work out shortest distance between start and end nodes
        distance[start_node][end_node] = shortest_path(start_node, end_node, max_length - 1, distance)

    # Function output
    return distance


print(floyd_warshall(graph))

import pkg_resources; installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
print(installed_packages)
