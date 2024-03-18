import sys

def calc_redraw_count(boards, start_row, start_col):
    black_start_count = 0
    white_start_count = 0
    for row in range(start_row, start_row + 8):
        for col in range(start_col, start_col + 8):
            if (row + col) % 2 == 0:
                if boards[row][col] == "B":
                    white_start_count += 1
                else:
                    black_start_count += 1            
            else:
                if boards[row][col] == "W":
                    white_start_count += 1
                else:
                    black_start_count += 1
    
    return min(black_start_count, white_start_count)

def solution(row, col, boards):
    count = row * col

    for start_row in range(row - 7):
        for start_col in range(col - 7):
            current_count = calc_redraw_count(boards, start_row, start_col)
            count = min(count, current_count)
    
    print(count)

'''
input
'''
N, M = map(int, sys.stdin.readline().split())
boards = []
for _ in range(N):
    boards.append(list(sys.stdin.readline()))
solution(N, M, boards)
