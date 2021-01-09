#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    v = 1
    sho = 0
    amari = 0
    for i in range(N):
        if sho > M:
            sho = sho % M
        v *= 10
        sho *= 10
        if v < M:
            continue
        sho = sho + v // M
        amari = v % M
        print((v, M, sho, amari))
        v = amari
    if sho > M:
        sho = sho % M
    print(sho)


main()
