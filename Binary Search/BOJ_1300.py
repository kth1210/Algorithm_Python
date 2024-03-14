import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())

    start = 1
    end = N * N
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        count = 0
        for div in range(1, N + 1):
            count += min(mid // div, N)
        
        # 더 작은 수가 답일 수도, 현재 mid가 답일 수도 있음
        if count + 1 > K:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)

solution()