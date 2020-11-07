#!/usr/bin/env python3

N = int(input())

t, x, y = 0, 0, 0

for i in range(N):
    nt, nx, ny = map(int, input().split())
    dt, dx, dy = nt - t, nx - x, ny - y
    if not (abs(dx) + abs(dy) <= dt and nt % 2 == (nx + ny) % 2):
        print('No')
        exit()
    t, x, y = nt, nx, ny
print('Yes')
