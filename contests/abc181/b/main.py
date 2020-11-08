#!/usr/bin/env python3

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

print(sum((a + b) * (b - a + 1) // 2 for a, b in AB))
