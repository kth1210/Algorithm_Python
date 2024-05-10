import sys

def solution():
    N, K = map(int, sys.stdin.readline().split())
    students = [[0 for _ in range(2)] for _ in range(7)]
    count = 0

    for _ in range(N):
        S, Y = map(int, sys.stdin.readline().split())
        students[Y][S] += 1

    for year in students:
        for student in year:
            count += student // K
            if student % K != 0:
                count += 1

    print(count)


solution()