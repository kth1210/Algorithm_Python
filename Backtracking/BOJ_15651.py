import sys

def print_sequence(limit, length):
    current_sequence = []
    backtracking(current_sequence, limit, length)

def backtracking(current_sequence, limit, length):
    if len(current_sequence) == length:
        print(*current_sequence)
        return
    
    for number in range(1, limit+1):
        current_sequence.append(number)
        backtracking(current_sequence, limit, length)
        current_sequence.pop()

def solution():
    N, M = map(int, sys.stdin.readline().split())
    print_sequence(N, M)

solution()