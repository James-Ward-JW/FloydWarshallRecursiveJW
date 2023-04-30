from timeit import default_timer as timer
import sys
import ImperativeVersion

NO_PATH = sys.maxsize


def test_performance_imperative():
    #
    graph = [[0, 7, NO_PATH, 8],
             [NO_PATH, 0, 5, NO_PATH],
             [NO_PATH, NO_PATH, 0, 2],
             [NO_PATH, NO_PATH, NO_PATH, 0]]

    start_imp = timer()
    for _ in range(2 ** 12):
        ImperativeVersion.floyd(graph)
    end_imp = timer()
    return end_imp - start_imp


if __name__ == '__main__':
    print('Imperative version: {}s'.format(round(test_performance_imperative(), 2)))
