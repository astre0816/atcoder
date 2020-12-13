#!/usr/bin/env python3

def main():
    N, M, T = map(int, input().split())
    time = 0
    n = N
    for i in range(M):
        A, B = map(int, input().split())
        n = n - (A - time)
        if n <= 0:
            print('No')
            exit()
        n = n + B - A
        n = N if n > N else n
        time = B
    if n - (T - time) > 0:
        print('Yes')
    else:
        print('No')


main()
