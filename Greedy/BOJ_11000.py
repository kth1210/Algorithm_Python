import sys
import heapq

def solution():
    N = int(sys.stdin.readline().rstrip())
    classes = []

    for _ in range(N):
        S, T = map(int, sys.stdin.readline().split())
        classes.append((S, T))
    
    classes.sort()

    room = []
    for start_time, end_time in classes:
        if not room:
            heapq.heappush(room, end_time)
            continue
        
        minimum_time = room[0]
        if start_time < minimum_time:
            heapq.heappush(room, end_time)
        else:
            heapq.heappop(room)
            heapq.heappush(room, end_time)
    
    print(len(room))

solution()