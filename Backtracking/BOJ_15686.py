import sys
INF = sys.maxsize
answer = INF

'''
집 위치, 치킨집 위치에서 치킨 거리를 계산해 반환
'''
def calculate_chicken_dist(houses, selected_chickens):
    chicken_dist = 0
    for house_row, house_col in houses:
        cur_dist = INF
        for chicken_row, chicken_col in selected_chickens:
            dist = abs(chicken_row - house_row) + abs(chicken_col - house_col)
            cur_dist = cur_dist if cur_dist < dist else dist
        chicken_dist += cur_dist
    return chicken_dist

'''
백트래킹을 통해 치킨집을 선택하고, 최대 개수만큼 골랐을 때 치킨 거리 계산
'''
def backtracking(houses, chickens, selected_chickens, M):
    global answer
    if len(selected_chickens) == M:
        chicken_dist = calculate_chicken_dist(houses, selected_chickens)
        answer = answer if answer < chicken_dist else chicken_dist
        return

    for idx in range(len(chickens)):
        if chickens[idx] not in selected_chickens:
            selected_chickens.append(chickens[idx])
            backtracking(houses, chickens[idx:], selected_chickens, M)
            selected_chickens.pop()

def solution():
    global answer
    N, M = map(int, sys.stdin.readline().split())
    houses = []
    chickens = []

    # 집 위치, 치킨집 위치 저장
    for row in range(N):
        input_row = list(map(int, sys.stdin.readline().split()))
        for col in range(len(input_row)):
            if input_row[col] == 1:
                houses.append((row, col))
            elif input_row[col] == 2:
                chickens.append((row, col))
    
    backtracking(houses, chickens, [], M)

    print(answer)

solution()