import sys
from collections import deque
INF = float('inf')

def solution():
    N, K = map(int, sys.stdin.readline().split())
    if N == K:
        print(0)
        print(N)
        return
    distances = [INF for _ in range(200_001)]
    paths = [-1 for _ in range(200_001)]

    queue = deque()
    queue.append(N)
    distances[N] = 0
    is_found = False

    while queue and not is_found:
        cur_location = queue.popleft()
        cur_distance = distances[cur_location]

        for next_location in [cur_location+1, cur_location-1, cur_location*2]:
            if next_location == K:
                distances[next_location] = cur_distance + 1
                paths[next_location] = cur_location
                is_found = True
                break
            if 0 <= next_location <= 200_000:
                if distances[next_location] > cur_distance + 1:
                    distances[next_location] = cur_distance + 1
                    paths[next_location] = cur_location
                    queue.append(next_location)

    print(distances[K])
    location = K
    answers = [location]
    while location != N:
        location = paths[location]
        answers.append(location)
    print(*reversed(answers))

solution()