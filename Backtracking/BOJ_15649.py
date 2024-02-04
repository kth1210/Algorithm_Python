import sys

def print_sequence(N, M):
    current_sequence = []
    visited = [False] * (N+1)
    backtracking(current_sequence, visited, N, M)

def backtracking(current_sequence, visited, N, M):
    if len(current_sequence) == M:
        print(*current_sequence)
        return

    for next_number in range(1, N+1):
        if not visited[next_number]:
            visited[next_number] = True
            current_sequence.append(next_number)
            backtracking(current_sequence, visited, N, M)
            current_sequence.pop()
            visited[next_number] = False

def solution():
    N, M = map(int, sys.stdin.readline().split())
    print_sequence(N, M)

solution()