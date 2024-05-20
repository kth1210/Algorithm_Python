import sys
from collections import deque

def solution():
    F, S, G, U, D = map(int, sys.stdin.readline().split())
    NOT_VISITED = -1
    counts = [NOT_VISITED for _ in range(F + 1)]
    queue = deque()
    queue.append(S)
    counts[S] = 0

    while queue:
        cur_floor = queue.popleft()

        for move in [U, -D]:
            next_floor = cur_floor + move

            if 1 <= next_floor <= F:
                if counts[next_floor] == NOT_VISITED or counts[cur_floor] + 1 < counts[next_floor]:
                    counts[next_floor] = counts[cur_floor] + 1
                    queue.append(next_floor)
    
    if counts[G] == NOT_VISITED:
        print("use the stairs")
    else:
        print(counts[G])


solution()

'''
모든 층에 대해서 횟수를 저장하는 배열을 만듬 (방문도 처리)
queue에 들어간 위치에 대해서 U, D 연산 진행
    근데 이동한 위치가 이미 그 전에 방문했었따면 (횟수가 더 작다면) 패스
'''