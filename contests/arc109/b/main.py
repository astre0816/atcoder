#!/usr/bin/env python3
import math

n = int(input())
k = int(math.sqrt(2 + 2 * n) - 1)
x = (k + 1) * k // 2
k = k if n + 1 - x <= k else k + 1
print(n + 1 - k)
