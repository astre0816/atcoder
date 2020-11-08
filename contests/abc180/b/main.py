#!/usr/bin/env python3
import math

N = int(input())
X = [abs(int(x)) for x in input().split()]

print(sum(X))
print(math.sqrt(sum(x ** 2 for x in X)))
print(max(X))
