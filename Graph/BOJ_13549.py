import sys
from collections import deque

def solution():
    N, K = map(int, sys.stdin.readline().split())
    
    # 이미 앞지르고 있는 경우 처리
    if N > K:
        print(N - K)
        return
    elif N == K:
        print(0)
        return
    
    times = [-1 for _ in range(K * 2 + 1)]
    queue = deque()
    queue.append(N)
    times[N] = 0

    while queue:
        now_location = queue.popleft()
        now_time = times[now_location]

        if now_location == K: break

        if now_location * 2 < K * 2 + 1:
            if times[now_location * 2] == -1 or times[now_location * 2] > now_time:
                times[now_location * 2] = now_time
                queue.append(now_location * 2)
        if now_location + 1 < K * 2 + 1:
            if times[now_location + 1] == -1 or times[now_location + 1] > now_time:
                times[now_location + 1] = now_time + 1
                queue.append(now_location + 1)
        if now_location - 1 > 0:
            if times[now_location - 1] == -1 or times[now_location - 1] > now_time:
                times[now_location - 1] = now_time + 1
                queue.append(now_location - 1)
        
    print(times[K])

solution()

'''
1초 후에 앞으로, 뒤로 한 칸 또는 0초 후에 * 2의 위치로 이동
출발 -> 도착까지 가장 빠르게 이동하는 시간

각 시간은 모두 -1초로 초기화

시작 위치 큐에 넣음
큐에서 위치 하나씩 뺌
    위치 * 2에 -1이나 현재 시간보다 큰 값 들어있으면 현재 시간 넣고 큐에 넣음
    위치 + 1에 -1이나 현재 시간 + 1보다 큰 값 들어있으면 현재 시간 + 1 넣고 큐에 넣음
    위치 - 1에 -1이나 현재 시간 + 1보다 큰 값 들어있으면 현재 시간 + 1 넣고 큐에 넣음
'''