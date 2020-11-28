#!/usr/bin/env python3

n, k = map(int, input().split())
s = input()


def battle(me, you):
    if me == you:
        return 0
    elif ((me == 'R' and you == 'S')
            or (me == 'S' and you == 'P')
            or (me == 'P' and you == 'R')):
        return 1
    else:
        return -1


def te(l, r):
    if r - l == 1:
        return s[l % n]
    else:
        lte = te(l, (l + r) // 2)
        rte = te((l + r) // 2, r)
        return lte if battle(lte, rte) >= 0 else rte


print(te(0, 2 ** k))
