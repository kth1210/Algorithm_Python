import sys
from collections import deque

def move_people(countries, visited, start_row, start_col, L, R):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    opened_countries = [(start_row, start_col)]
    total_people = countries[start_row][start_col]

    while queue:
        current_row, current_col = queue.popleft()
        current_people = countries[current_row][current_col]

        for idx in range(4):
            next_row = current_row + dr[idx]
            next_col = current_col + dc[idx]

            if 0 <= next_row < len(countries) and 0 <= next_col < len(countries[0]):
                next_people = countries[next_row][next_col]
                if not visited[next_row][next_col] and L <= abs(current_people - next_people) <= R:
                    total_people += next_people
                    visited[next_row][next_col] = True
                    opened_countries.append((next_row, next_col))
                    queue.append((next_row, next_col))
    
    if len(opened_countries) == 1:
        visited[start_row][start_col] = False
        return
    elif len(opened_countries) > 1:
        divided_people = total_people // len(opened_countries)
        for row, col in opened_countries:
            countries[row][col] = divided_people

def solution():
    N, L, R = map(int, sys.stdin.readline().split())
    countries = []

    for _ in range(N):
        countries.append(list(map(int, sys.stdin.readline().split())))
    
    day = 0
    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    move_people(countries, visited, i, j, L, R)
        
        is_moved = False
        for row in visited:
            for is_visited in row:
                if is_visited:
                    is_moved = True
        
        if not is_moved: break
        day += 1
    
    print(day)

solution()

# 문제 정리
'''
모든 나라와 국경선은 정사각형
더이상 인구 이동이 없을 때까지 인구 이동됨
1. 국경을 맞대고 있는 나라의 인구 차이가 L 이상 R 이하라면 두 나라의 국경선을 오늘 하루 염
2. 국경선 다 연 다음에 인구이동
3. 국경선이 열려있는 두 나라는 오늘 하루 연합임
4. 연합은 인구 다 합쳐서 나누기 나라 수로 해버림 (소수점 버림)
5. 국경 닫음

이때 며칠동안 인구 이동 발생하는지 계산
'''

# 풀이 과정
'''
이동 가능한 나라? -> 상하좌우 중 인구 차이가 L 이상 R 이하인 곳
계속 상하좌우 나라 확인하면서 이동 가능한 나라면 queue에 추가,
배열에 나라 위치 저장하고, 총 인구 수도 계속 누적함
queue로 방문 끝났는데, 배열에 나라가 2개 이상이다? 그럼 위치마다 총 인구수 / 배열 길이만큼 넣음

밖에서는 visited를 하루마다 초기화 함
not visited면 인구 이동 시키고, visited면 안함
하루 다 지났는데 visited가 다 False면 종료
'''