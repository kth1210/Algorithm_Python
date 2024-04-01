import sys
from itertools import permutations

def calc_gap(numbers):
    gap = 0
    for idx in range(len(numbers) - 1):
        gap += abs(numbers[idx] - numbers[idx + 1])
    return gap

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))

    all_cases = permutations(numbers)
    max_gap = 0
    for cur_numbers in all_cases:
        gap = calc_gap(cur_numbers)
        max_gap = max(max_gap, gap)
    
    print(max_gap)

solution()