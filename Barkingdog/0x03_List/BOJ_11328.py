import sys

def solution():
    N = int(sys.stdin.readline().rstrip())

    for _ in range(N):
        first, second = sys.stdin.readline().split()
        if sorted(first) == sorted(second):
            print("Possible")
        else:
            print("Impossible")

solution()