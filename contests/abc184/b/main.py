#!/usr/bin/env python3

N, X = map(int, input().split())
S = input()

for s in S:
    if s == "o":
        X += 1
    else:
        X -= 1 if X > 0 else 0

print(X)
