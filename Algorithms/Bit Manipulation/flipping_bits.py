#!/bin/python3
import os

# https://www.hackerrank.com/challenges/flipping-bits/submissions/code/140346706
def flippingBits(n):
    for offset in range(32):
        mask = 1 << offset
        n ^= mask
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
