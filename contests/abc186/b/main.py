#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    A = []
    for j in range(H):
        A.append(list(map(int, input().split())))
    m = min(min(a) for a in A)
    s = 0
    for a in A:
        s += sum(aa - m for aa in a)
    print(s)


main()
