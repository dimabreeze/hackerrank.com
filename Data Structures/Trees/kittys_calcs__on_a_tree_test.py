from kittys_calcs__on_a_tree import toAdjacencyList, solveMultipleSets


def test_sample_input_0():
    edges = [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7]]
    sets = [[2, 4], [5], [2, 4, 5]]

    adj = toAdjacencyList(len(edges)+1, edges)
    result = list(solveMultipleSets(adj, sets))
    assert result == [16, 0, 106]
