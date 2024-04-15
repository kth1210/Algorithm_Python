import sys
from collections import deque

'''
해킹 가능한 컴퓨터의 개수를 반환합니다.
- Parameters:
    - graph: 컴퓨터의 신뢰 관계를 나타내는 그래프
    - number: 선택한 컴퓨터 번호
- Returns: 해킹 가능한 컴퓨터 개수
'''
def calc_hackable_count(graph: dict, number: int) -> int:
    visited = [False for _ in range(len(graph) + 1)]
    queue = deque()
    queue.append(number)
    visited[number] = True
    count = 1

    while queue:
        current_computer = queue.popleft()

        for next_computer in graph[current_computer]:
            if not visited[next_computer]:
                visited[next_computer] = True
                count += 1
                queue.append(next_computer)

    return count


def solution():
    N, M = map(int, sys.stdin.readline().split())
    graph = {node:[] for node in range(1, N + 1)}

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[B].append(A)
    
    max_count = 0
    computer_numbers = []
    for number in range(1, N + 1):
        count = calc_hackable_count(graph, number)
        if count > max_count:
            max_count = count
            computer_numbers = [number]
        elif count == max_count:
            computer_numbers.append(number)
    
    print(*computer_numbers)

solution()