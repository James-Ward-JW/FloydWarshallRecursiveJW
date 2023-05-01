# Aim of FloydWarshallRecursiveJW
This project is tasked with rewriting the Floyd-warshall algorithm from an imperative style to a recursive style. 

The code was written to PEP standards and tested for performance, comparing program speed between the imperative and recursive approaches.

# Documents
- [ImperativeVersion.py](docs/ImperativeVersion.py) - The imperative version of the algorithm
- [floyd_warshall_recursive.py](docs/floyd_warshall_recursive.py) - The recursive solution to the algorithm
- [requirements.txt](docs/requirements.txt) - The list of required packages to replicate this work
- [test_floyd-warshall.py](docs/test_floyd-warshall.py) - unittests of recursive solution
- [test_imperative_performance](docs/test_imperative_performance) - Speed check of imperative version
- [test_recursive_performance](docs/test_recursive_performance) - Speed check of recursive solution

# Summary
As predicted by the literature, the recursive solution ran slightly slower than the imperative version, likely due to the need to call the shortest_path function multiple times.

However as also outlined in the code report, the program run time difference is in the millisecond range, so both versions are fit for the current purpose.

Recursive written code is thought by many to be the more elegant approach, so when run time is not an issue it may be the better solution.

If run time does become an issue, e.g. if a much larger input graph is run in floyd_warshall_recursive.py, then a new discussion on which approach would be best used should be had.
