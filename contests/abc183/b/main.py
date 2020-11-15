#!/usr/bin/env python3

Sx, Sy, Gx, Gy = map(int, input().split())

a = ((-Gy - Sy) / (Gx - Sx)) if Gx - Sx != 0 else -Gy - Sy

b = Sy - a * Sx

x = -b / a

print(x)
