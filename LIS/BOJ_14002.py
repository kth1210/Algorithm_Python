import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    LIS = [[] for _ in range(N)]

    for i in range(N):
        LIS[i] = [numbers[i]]
        for j in range(i):
            if numbers[i] > numbers[j]:
                if len(LIS[i]) <= len(LIS[j]):
                    LIS[i] = LIS[j] + [numbers[i]]

    answer_count = 0
    answer_LIS = []
    for idx in range(N):
        if len(LIS[idx]) > answer_count:
            answer_count = len(LIS[idx])
            answer_LIS = LIS[idx]
    
    print(answer_count)
    print(*answer_LIS)

solution()