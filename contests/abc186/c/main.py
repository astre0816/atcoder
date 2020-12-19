#!/usr/bin/env python3

def main():
    N = int(input())
    s = 0
    for i in range(1, N + 1):
        if '7' in str(i) or '7' in oct(i):
            s += 1
    print(N - s)


main()
