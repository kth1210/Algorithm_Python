import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0 for _ in range(n + 1)]

    for idx in range(1, n + 1):
        prefix_sum[idx] = prefix_sum[idx - 1] + numbers[idx - 1]

    total = 0
    for idx in range(n):
        total += numbers[idx] * (prefix_sum[n] - prefix_sum[idx + 1])

    print(total)

solution()


'''
숫자들 중 2개를 뽑아서 곱한 것의 합?
x1 x2 x3 x4
x1 * x2 + x1 * x3 + x1 * x4 + x2 * x3 + x2 * x4 + x3 * x4

x1 * (x2 + x3 + x4)
x2 * (x3 + x4)
x3 * (x4)
'''