import sys

def solution():
    X = int(sys.stdin.readline().rstrip())
    print(format(X, 'b').count("1"))

solution()