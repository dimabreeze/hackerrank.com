#!/bin/python3
import os


# Complete the arrayManipulation function below.
def arrayManipulation(numElements, listQueries):
    arr = [0] * numElements
    for q in listQueries:
        begin = q[0]
        end = q[1]
        add = q[2]

        arr[begin - 1] += add
        if end < numElements:
            arr[end] -= add

    init = 0
    maxSum = 0
    for a in arr:
        init += a
        if init > maxSum:
            maxSum = init
    return maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
