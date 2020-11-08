#!/usr/bin/env python3

X, Y, A, B = map(int, input().split())

x, p = X, 0
while x * A < Y and x * A < x + B:
    x *= A
    p += 1
dx = Y - 1 - x
p += dx // B
print(p)
