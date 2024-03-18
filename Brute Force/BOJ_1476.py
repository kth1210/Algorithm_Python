import sys

def solution(E, S, M):
    year = 1
    current_E, current_S, current_M = 1, 1, 1

    while current_E != E or current_S != S or current_M != M:
        year += 1
        current_E += 1
        current_S += 1
        current_M += 1

        if current_E > 15:
            current_E = 1
        if current_S > 28:
            current_S = 1
        if current_M > 19:
            current_M = 1
    
    print(year)


'''
input
'''
E, S, M = map(int, sys.stdin.readline().split())
solution(E, S, M)