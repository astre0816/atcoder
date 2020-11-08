#!/usr/bin/env python3

import itertools

S = input()
SI = list(map(int, S))

if (all(i % 2 == 1 for i in SI)):
    print('No')
    exit()

l = len(SI)
for s in itertools.permutations(SI):
    x = 0
    for i in range(l):
        x += s[i] * (10 ** i)
    if x % 8 == 0:
        print('Yes')
        exit()

print('No')
