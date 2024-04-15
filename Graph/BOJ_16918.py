import sys

def explosion(board: list) -> list:
    next_board = [["O" for _ in range(len(board[0]))] for _ in range(len(board))]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    bomb = "O"
    empty = "."

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == bomb:
                next_board[row][col] = empty
                for idx in range(4):
                    next_row = row + dr[idx]
                    next_col = col + dc[idx]

                    if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                        next_board[next_row][next_col] = empty
    
    return next_board


def solution():
    R, C, N = map(int, sys.stdin.readline().split())
    board = []

    for _ in range(R):
        board.append(list(sys.stdin.readline().rstrip()))
    
    # 짝수 초에는 항상 폭탄으로 꽉 참
    if N % 2 == 0:
        for _ in range(R):
            print("O" * C)
        return

    # 홀수 초에 폭발 결과
    for _ in range(N // 2):
        next_board = explosion(board)
        board = next_board
    
    for row in board:
        print(''.join(row))

solution()


# 문제 정리
"""
폭탄은 3초 후에 폭발함
폭탄 터지면 그 위치랑 상하좌우 다 파괴됨 -> 파괴되는 위치에 있는 폭탄은 그냥 파괴됨 (연쇄 반응 없음)

- 일부 칸에 폭탄 설치 (시간 같음)
- 1초 지남
- 1초동안 폭탄이 없는 모든 칸에 폭탄 설치 (이때 모든 칸이 폭탄을 가지게 됨)
- 1초 후에 3초 전에 먼저 설치했던 폭탄 폭발

초기 상태가 주어질 때 N초 이후의 격자판 상태 구하기
"""

# 풀이 과정
"""
짝수 초에는 항상 폭탄으로 꽉 참
홀수 초에는 O로 꽉 채운 다음에 폭탄 위치에 폭탄 터트리기
"""