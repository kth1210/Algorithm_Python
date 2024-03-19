import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    minutes = list(map(int, sys.stdin.readline().split()))

    start = max(minutes)
    end = 10 ** 9
    answer_size = float('inf')

    while start <= end:
        mid = (start + end) // 2
        count = 1
        value = 0

        for minute in minutes:
            if value + minute <= mid:
                value += minute
            else:
                value = minute
                count += 1
        
        if count <= M:
            answer_size = min(answer_size, mid)
            end = mid - 1
        else:
            start = mid + 1

    print(answer_size)

solution()