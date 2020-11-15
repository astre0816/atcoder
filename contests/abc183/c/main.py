#!/usr/bin/env python3
import itertools

N, K = map(int, input().split())

T = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    T[i] = [int(t) for t in input().split()]
count = 0

O = [i for i in range(1, N)]
for o in itertools.permutations(O):
    cost = 0
    cost += T[0][o[0]]
    for i in range(len(o)):
        cost += T[o[i]][o[i + 1]] if i != len(o) - 1 else T[o[i]][0]
    if cost == K:
        count += 1

print(count)
