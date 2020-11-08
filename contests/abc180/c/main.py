#!/usr/bin/env python3

N = int(input())

low, hight = [], []
i = 1
while i * i <= N:
    if N % i == 0:
        low.append(i)
        if i != N // i:
            hight.append(N // i)
    i += 1

for x in low:
    print(x)
for x in reversed(hight):
    print(x)
