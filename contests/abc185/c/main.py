#!/usr/bin/env python3
import math

def main():
    L = int(input()) - 1
    a = math.factorial(L) // (math.factorial(L - 11) * math.factorial(11))
    print(a)


main()
