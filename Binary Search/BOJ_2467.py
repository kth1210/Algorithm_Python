import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    values = list(map(int, sys.stdin.readline().split()))

    answer = []
    answer_value = float('inf')
    for idx, first_value in enumerate(values):
        start = idx + 1
        end = N - 1

        while start <= end:
            mid = (start + end) // 2
            value = first_value + values[mid]

            if abs(value) < answer_value:
                answer = [first_value, values[mid]]
                answer_value = abs(value)

            if value == 0:
                print(first_value, values[mid])
                return
            elif value > 0:
                end = mid - 1
            else:
                start = mid + 1

    print(*answer)

solution()