import sys

def mul(a, b, c):
    if b == 1:
        return a % c

    value = mul(a, b//2, c)
    
    if b % 2 == 0:
        return value * value % c
    else:
        return value * value * a % c

def solution():
    A, B, C = map(int, sys.stdin.readline().split())
    print(mul(A, B, C))

solution()