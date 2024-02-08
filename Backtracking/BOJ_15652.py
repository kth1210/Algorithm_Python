import sys

def print_sequence(limit, length):
    current_sequence = []
    backtracking(current_sequence, limit, length)

def backtracking(current_sequence, limit, length):
    if len(current_sequence) == length:
        print(*current_sequence)
        return

    minimum_value = current_sequence[-1] if len(current_sequence) > 0 else 1

    for number in range(minimum_value, limit+1):
        current_sequence.append(number)
        backtracking(current_sequence, limit, length)
        current_sequence.pop()

def solution():
    N, M = map(int, sys.stdin.readline().split())
    print_sequence(N, M)

solution()