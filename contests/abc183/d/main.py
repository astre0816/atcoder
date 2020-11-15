#!/usr/bin/env python3

N, W = map(int, input().split())

m = {}
tmax = 0
for n in range(N):
    S, T, P = input().split()
    P = int(P)
    m[S] = m[S] + P if S in m else P
    m[T] = m[T] - P if T in m else -P

keys = sorted(map(int, m.keys()))
w = 0
for k in keys:
    w += m[str(k)]
    if W < w:
        print('No')
        exit()
print('Yes')
