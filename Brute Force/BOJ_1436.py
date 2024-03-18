import sys

def solution(N: int):
    number = 666
    while N > 0:
        if "666" in str(number):
            N -= 1
        number += 1
    print(number - 1)

'''
input
'''
N = int(sys.stdin.readline().rstrip())
solution(N)