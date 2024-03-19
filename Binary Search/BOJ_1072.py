import sys

def solution():
    X, Y = map(int, sys.stdin.readline().split())
    Z = int(Y * 100 / X)

    if Z >= 99:
        print(-1)
        return

    start = 0
    end = X
    answer = float('inf')
    while start <= end:
        mid = (start + end) // 2
        value = int((Y + mid) * 100 / (X + mid))

        if value != Z:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    print(answer)

solution()