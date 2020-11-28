#!/usr/bin/env python3

a, b, x, y = map(int, input().split())

result = 0
if (a == b or a - 1 == b):
    result = x
elif(a < b):
    if x * 2 < y:
        result = (b - a) * 2 * x + x
    else:
        result = (b - a) * y + x
else:
    if x * 2 < y:
        result = (a - b) * 2 * x - x
    else:
        result = (a - b - 1) * y + x
print(result)
