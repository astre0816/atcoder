#!/usr/bin/env python3

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            pi = P[i]
            pj = P[j]
            pk = P[k]
            if pi[0] == pj[0] == pk[0]:
                print('Yes')
                exit()
            elif pi[0] == pj[0] or pj[0] == pk[0] or pk[0] == pi[0]:
                continue
            dij = abs(pi[1] - pj[1]) / abs(pi[0] - pj[0])
            djk = abs(pj[1] - pk[1]) / abs(pj[0] - pk[0])
            dki = abs(pk[1] - pi[1]) / abs(pk[0] - pi[0])
            if dij == djk == dki:
                print('Yes')
                exit()
print('No')
