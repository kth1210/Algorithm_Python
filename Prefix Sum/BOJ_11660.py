import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    matrix = []

    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    # 누적합 구하기
    prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + matrix[i-1][j-1] - prefix_sum[i-1][j-1]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        # 누적합에서 해당 구간 구해서 출력하기
        answer = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
        print(answer)

solution()