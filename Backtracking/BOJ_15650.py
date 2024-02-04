import sys

def print_sequence(limit, length):
    current_sequence = []
    visited = [False] * (limit+1)
    backtracking(current_sequence, visited, limit, length)

def backtracking(current_sequence, visited, limit, length):
    if len(current_sequence) == length:
        print(*current_sequence)
        return
    
    low_limit = 1
    if len(current_sequence) > 0:
        low_limit = current_sequence[-1]
    
    for next_number in range(low_limit, limit+1):
        if not visited[next_number]:
            visited[next_number] = True
            current_sequence.append(next_number)
            backtracking(current_sequence, visited, limit, length)
            current_sequence.pop()
            visited[next_number] = False

def solution():
    N, M = map(int, sys.stdin.readline().split())
    print_sequence(N, M)

solution()