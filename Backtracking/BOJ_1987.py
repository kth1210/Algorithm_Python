import sys
answer = 1

def backtracking(board, cur_location, history, count):
    global answer
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cur_row, cur_col = cur_location

    if cur_row < 0 or cur_row >= len(board) or cur_col < 0 or cur_col >= len(board[0]):
        return

    cur_alpha = board[cur_row][cur_col]
    if history[ord(cur_alpha) - 65]:
        answer = max(answer, count)
        return

    history[ord(cur_alpha) - 65] = True
    for idx in range(4):
        next_row = cur_row + dr[idx]
        next_col = cur_col + dc[idx]
        backtracking(board, (next_row, next_col), history, count + 1)        
    history[ord(cur_alpha) - 65] = False

def solution():
    R, C = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(R):
        input_row = list(sys.stdin.readline().rstrip())
        board.append(input_row)
    
    history = [False] * 26
    backtracking(board, (0, 0), history, 0)

    print(answer)

solution()