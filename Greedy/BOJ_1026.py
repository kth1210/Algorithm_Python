import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    A = map(int, sys.stdin.readline().split())
    B = map(int, sys.stdin.readline().split())

    sorted_A = sorted(A, reverse = True)
    sorted_B = sorted(B)

    result = 0
    for a_number, b_number in zip(sorted_A, sorted_B):
        result += a_number * b_number
    
    print(result)

solution()