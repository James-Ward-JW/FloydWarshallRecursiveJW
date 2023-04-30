from timeit import default_timer as timer
import sys
import floyd_warshall_recursive

NO_PATH = sys.maxsize


def test_performance_recursive():
    #
    graph = [[0, 7, NO_PATH, 8],
             [NO_PATH, 0, 5, NO_PATH],
             [NO_PATH, NO_PATH, 0, 2],
             [NO_PATH, NO_PATH, NO_PATH, 0]]

    start_rec = timer()
    for _ in range(2 ** 12):
        floyd_warshall_recursive.floyd_warshall(graph)
    end_rec = timer()
    return end_rec - start_rec


if __name__ == '__main__':
    print('Recursive version: {}s'.format(round(test_performance_recursive(), 2)))
