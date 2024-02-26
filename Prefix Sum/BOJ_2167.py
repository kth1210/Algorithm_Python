import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    matrix = []
    prefix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

    K = int(sys.stdin.readline().rstrip())
    for _ in range(K):
        i, j, x, y = map(int, sys.stdin.readline().split())
        answer = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
        print(answer)

solution()