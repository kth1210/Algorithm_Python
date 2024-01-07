import sys

def solution():
    A, B = map(int, sys.stdin.readline().split())
    count = 0

    while A < B:
        count += 1
        if str(B)[-1] == '1':
            B //= 10
        elif B % 2 == 0:
            B //= 2
        else:
            print(-1)
            return
    
    if A != B:
        print(-1)
        return
    
    print(count + 1)

solution()