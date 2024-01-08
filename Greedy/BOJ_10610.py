import sys

def solution():
    N = sorted(list(map(int, sys.stdin.readline().rstrip())), reverse = True)

    if 0 in N:
        if sum(N) % 3 != 0:
            print(-1)
        else:
            print(''.join(map(str, N)))
    else:
        print(-1)

solution()