from kittys_calcs__on_a_tree import distances, toAdjacencyList, \
                                    solve, solveMultiple


"""def __validate_distances(distances):
    n = len(distances)
    assert all(map(lambda x: len(x) == n, distances))
    for i, d in enumerate(distances):
        for j, v in enumerate(d):
            assert v == 0 if i == j else v != 0


def test_distances():
    assert distances(0) == []
    assert distances(1) == [[0]]
    assert distances(2) == [[0, -1],
                            [-1, 0]]
    assert distances(5) == [[0, -1, -1, -1, -1],
                            [-1, 0, -1, -1, -1],
                            [-1, -1, 0, -1, -1],
                            [-1, -1, -1, 0, -1],
                            [-1, -1, -1, -1, 0]]

    __validate_distances(distances(2*(10**5)))"""


def test_sample_input_0():
    edges = [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7]]
    sets = [[2, 4], [5], [2, 4, 5], [4, 5]]
    n = len(edges) + 1

    adj = toAdjacencyList(n, edges)
    dist, visit = distances(n)

    def solveMultipleSets(adj, dist, visited, sets):
        for s in sets:
            yield solveMultiple(adj, dist, visited, s)

    result = list(solveMultipleSets(adj, dist, visit, sets))
    assert result == [16, 0, 106, 60]
