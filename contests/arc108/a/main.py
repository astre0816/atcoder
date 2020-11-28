#!/usr/bin/env python3

S, P = map(int, input().split())

x = P if P < S // 2 else S // 2 + (S + 1) % 2
for i in range(1, x + 1):
    if i * (S - i) == P:
        print('Yes')
        exit()
print('No')
