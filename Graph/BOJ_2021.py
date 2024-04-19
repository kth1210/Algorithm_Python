import sys
from collections import deque

def calc_transfer_count(
    graph: dict,
    start_station: int,
    start_lines: int,
    end_station: int
) -> int:
    count_cache = [-1 for _ in range(len(graph))]
    count_cache[start_station] = 0
    queue = deque()

    for start_line in start_lines:
        queue.append((start_station, start_line, 0))
    
    while queue:
        cur_station, cur_line, cur_count = queue.popleft()

        if cur_count > count_cache[cur_station]: continue

        for next_station, next_line in graph[cur_station]:
            next_count = cur_count + 1 if cur_line != next_line else cur_count

            if count_cache[next_station] == -1 or count_cache[next_station] > next_count:
                count_cache[next_station] = next_count
                queue.append((next_station, next_line, next_count))
    
    return count_cache[end_station]

def solution():
    N, L = map(int, sys.stdin.readline().split())
    graph = {station_number: [] for station_number in range(N + 1)}
    line_dict = {station_number: [] for station_number in range(N + 1)}

    # 노선도 그래프 구축
    for line_number in range(L):
        input_line = list(map(int, sys.stdin.readline().split()))

        for idx in range(len(input_line) - 2):
            first = input_line[idx]
            second = input_line[idx + 1]
            graph[first].append((second, line_number))
            graph[second].append((first, line_number))

        for idx in range(len(input_line) - 1):
            line_dict[input_line[idx]].append(line_number)
    
    start_station, end_station = map(int, sys.stdin.readline().split())
    start_lines = line_dict[start_station]
    transfer_count = calc_transfer_count(graph, start_station, start_lines, end_station)

    print(transfer_count)

solution()

'''
지하철 노선에 대한 정보가 주어짐
출발지에서 목적지까지의 최소 환승 경로를 구하는 문제
환승 횟수만 구하면 됨

1 - 2 - 3 - 4 - 5
9 - 7 - 10
7 - 6 - 3 - 8

< graph > (연결된 노드, 노선 번호)
1: (2, 0)
2: (1, 0), (3, 0)
3: (2, 0), (4, 0), (6, 2), (8, 2)
4: (3, 0), (5, 0)
5: (4, 0)
6: (3, 2), (7, 2)
7: (6, 2), (9, 1), (10, 1)
8: (3, 2)
9: (7, 1)
10: (7, 1)

< 환승 횟수 저장 > (-1 이면 아직 안감)
1   2   3   4   5   6   7   8   9   10
-----------------------------------------
-1  -1  -1  -1  -1  -1  -1  -1  -1  -1
0   0   0   0   0   1   1   1   2   2

< 큐에 역 번호랑 노선 번호 저장 >
역 번호, 노선 번호 꺼냄
현재 환승 횟수는 역 번호로 가져옴

다음 역 번호, 노선 번호 비교
    같은 노선이면 횟수 그대로, 다른 노선이면 횟수 + 1인데
    이미 다음 역이 -1이 아니고, 내 횟수보다 작다면 이동 안함
        즉, -1일 때만 이동하고 횟수 업데이트하고 큐에 넣음
'''
