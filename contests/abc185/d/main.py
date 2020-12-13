#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        exit()
    if M == N:
        print(0)
        exit()

    A = list(map(int, input().split()))
    A.append(0)
    A.append(N + 1)
    A.sort()
    B = [(A[i + 1] - A[i] - 1) for i in range(M + 1) if A[i + 1] - A[i] - 1 > 0]
    k = min(B)

    ans = sum((b // k + (1 if b % k > 0 else 0)) for b in B)
    print(ans)


main()
