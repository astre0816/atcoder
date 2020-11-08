#!/usr/bin/env python3

N = int(input())
P = [input().split() for _ in range(N)]

costs = [N][N]
for i in range(N):
    for j in range(N):
        costs[i][j] == abs(p[j][0] - p[i][0]) + abs(p[j][1] - p[i][1])
        + max([0, p[j][2] - p[i][2])
