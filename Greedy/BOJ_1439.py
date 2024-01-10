import sys

def solution():
    S = sys.stdin.readline().rstrip()
    print(min(len(S.replace('0', ' ').split()), len(S.replace('1', ' ').split())))

solution()