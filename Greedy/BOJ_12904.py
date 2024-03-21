import sys

def solution():
    S = sys.stdin.readline().rstrip()
    T = sys.stdin.readline().rstrip()
    S_length = len(S)

    while len(T) > S_length:
        if T[-1] == 'A':
            T = T[:-1]
        elif T[-1] == 'B':
            T = T[:-1]
            T = T[::-1]
    
    answer = int(S == T)
    print(answer)

solution()