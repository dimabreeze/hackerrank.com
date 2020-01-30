# import sys
from collections import deque
from itertools import combinations
from functools import reduce

MOD = 10**9+7


# function for finding minimum
# no. of edge using BFS
def minEdgeBFS(edges: list, u: int, v: int):
    n = len(edges)

    # visited[n] for keeping track
    # of visited node in BFS
    visited = [0] * n
    # Initialize distances as 0
    distance = [0] * n
    # queue to do BFS.
    deq = deque()
    distance[u] = 0

    # deq.put(u)
    deq.append(u)

    visited[u] = True
    while deq:
        x = deq.pop()
        for i in range(len(edges[x])):
            if visited[edges[x][i]]:
                continue
            # update distance for i
            distance[edges[x][i]] = distance[x] + 1
            deq.append(edges[x][i])
            visited[edges[x][i]] = 1
    return distance[v]

"""class __Mock_STDIN(object):
    def __init__(self, response_list):
        self.std_in_list = response_list
        self.std_in_length = len(response_list)
        self.index = 0

    def readline(self):
        value = self.std_in_list[self.index]
        # print(value)
        if self.index < self.std_in_length-1:
            self.index += 1
        else:
            self.index = 0
        return value

predetermined_stdin_responses = [
    '7 3\r',
    '1 2\r',
    '1 3\r',
    '1 4\r',
    '3 5\r',
    '3 6\r',
    '3 7\r',
    '2\r',
    '2 4\r',
    '1\r',
    '5\r',
    '3\r',
    '2 4 5\r'
]
sys.stdin = __Mock_STDIN(predetermined_stdin_responses)"""


def toAdjacencyList(n: int, edges):
    adj = [[] for i in range(n)]
    for edge in edges:
        u = edge[0]-1
        v = edge[1]-1
        adj[u].append(v)
        adj[v].append(u)
    return adj


def solveSingle(adj: list, u: int, v: int):
    dist = minEdgeBFS(adj, u-1, v-1)
    global MOD
    return dist * u * v % MOD


def solveMultiple(adj: list, iterable):
    c = combinations(iterable, 2)
    r = reduce(lambda total, x: total + solveSingle(adj, x[0], x[1]), c, 0)
    global MOD
    return r % MOD


def solveMultipleSets(adj: list, s):
    for q in s:
        yield solveMultiple(adj, q)


if __name__ == '__main__':
    nq = list(map(int, input().split()))
    n = nq[0]
    q = nq[1]

    edges = []
    for idx in range(n-1):
        edges.append(list(map(int, input().split())))

    sets = []
    for idx in range(q):
        _ = input()
        sets.append(set(map(int, input().split())))

    adj = toAdjacencyList(n, edges)
    for s in solveMultipleSets(adj, sets):
        print(s)