#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    s = 0
    for i in range(N - 1):
        ai = A[i]
        for j in range(i, N):
            aj = A[j]
            s += abs(aj - ai)
    print(s)


main()
