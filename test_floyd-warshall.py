import sys
import unittest

from floyd_warshall_recursive import shortest_path
from floyd_warshall_recursive import floyd_warshall

NO_PATH = sys.maxsize


class ShortestPathClass(unittest.TestCase):

    def test_shortest_path(self):
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
# Usual shortest_path function call:
# distance[start_node][end_node] = shortest_path(start_node, end_node, MAX_LENGTH - 1, distance)
        example_one = shortest_path(0, 3, 3, graph)
        example_two = shortest_path(2, 3, 3, graph)
        self.assertEqual(example_one, 8)
        self.assertEqual(example_two, 2)


class TestFloydWarshall(unittest.TestCase):

    def test_floyd_output(self):
        # Comparison of shortest_path output above:
        # [[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2],
        # [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]] with floyd_warshall() output
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        output_test_shortest_path = [[0, 7, 12, 8],
                                     [NO_PATH, 0, 5, 7],
                                     [NO_PATH, NO_PATH, 0, 2],
                                     [NO_PATH, NO_PATH, NO_PATH, 0]]
        output_floyd_warshall = floyd_warshall(graph)
        self.assertEqual(output_test_shortest_path, output_floyd_warshall)

    def test_incorrect_input_type(self):
        # Floyd function is expecting number inputs, or the pre-established variable NO_PATH (equal to sys.maxsize)
        graph = [[0, 7, 'NO_PATH', 8],
                 [NO_PATH, 0, 5],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        with self.assertRaises(TypeError):
            shortest_path(1, 2, 3, graph)

# import pkg_resources; installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
# print(installed_packages)
