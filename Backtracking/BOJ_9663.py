import sys

def calculate_n_queen_case(size):
    answer = []
    # 각 index에는 해당 index 행의 퀸 col 위치를 저장
    # -1 이라면 퀸이 없는 경우임
    queen_map = [-1 for _ in range(size)]
    backtracking(queen_map, 0, size, answer)
    return len(answer)


def backtracking(queen_map, row, size, total_count):
    if row == size:
        total_count.append(True)
        return

    for next_col in range(size):
        # row 행 next_col 열에 퀸을 위치시켜봄
        queen_map[row] = next_col
        # row 행 next_col 열에 퀸 놨을 때 조건 맞는지 확인
        if queen_available(queen_map, row, next_col):
            # 조건 맞으면 다음 row 확인
            backtracking(queen_map, row+1, size, total_count)
        # 돌아왔으면 퀸 뻬기
        queen_map[row] = -1


# row 행 col 열에 퀸 놓았을 때 조건 만족하는지 확인
def queen_available(queen_map, row, col):
    # 각 행의 퀸 위치를 가져옴
    for pre_row, pre_col in enumerate(queen_map):
        # 지금 놓으려는 행과 퀸이 아직 없는 경우는 패스
        if pre_row == row or pre_col == -1:
            continue
        
        # 열이 같거나
        # 열+행 합이 같거나 (y=x 대각)
        # 열-행 또는 행-열의 차이가 같으면 (y=-x 대각) 공격 가능한 경우이므로 False 반환
        if pre_col == col or pre_col+pre_row == col+row or pre_col-pre_row == col-row or pre_row-pre_col == row-col:
            return False
    return True


def solution():
    N = int(sys.stdin.readline().rstrip())
    answer = calculate_n_queen_case(N)
    print(answer)

solution()