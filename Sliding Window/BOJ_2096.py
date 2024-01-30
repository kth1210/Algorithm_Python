import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    input_numbers = list(map(int, sys.stdin.readline().split()))

    comparison_range = [(0, 2), (0, 3), (1, 3)]
    minimum_dp = input_numbers[:]
    maximum_dp = input_numbers[:]

    for _ in range(1, N):
        input_numbers = list(map(int, sys.stdin.readline().split()))
        temp_minimum_dp = [0] * 3
        temp_maximum_dp = [0] * 3

        for col in range(3):
            left, right = comparison_range[col]
            temp_minimum_dp[col] = input_numbers[col] + min(minimum_dp[left:right])
            temp_maximum_dp[col] = input_numbers[col] + max(maximum_dp[left:right])
        
        minimum_dp = temp_minimum_dp[:]
        maximum_dp = temp_maximum_dp[:]

    print(max(maximum_dp), min(minimum_dp))

solution()