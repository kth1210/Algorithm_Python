import sys

def binary_search(A, number):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start+end) // 2

        if A[mid] == number:
            return True
        elif A[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
        
    return False


def solution():
    N = int(sys.stdin.readline().rstrip())
    sorted_A = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline().rstrip())
    C = list(map(int, sys.stdin.readline().split()))

    for number in C:
        if binary_search(sorted_A, number):
            print(1)
        else:
            print(0)

solution()