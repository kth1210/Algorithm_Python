import sys
from collections import deque

def time_for_find_brother(subin_location, brother_location):    
    location = [-1] * 100001
    location[subin_location] = 0

    queue = deque()
    queue.append(subin_location)

    while queue:
        now_location = queue.popleft()
        now_location_time = location[now_location]

        for next_location in [now_location + 1, now_location - 1, now_location * 2]:
            if 0 <= next_location <= 100000 and location[next_location] == -1:
                location[next_location] = now_location_time + 1
                queue.append(next_location) 
        
        if location[brother_location] != -1:
            return location[brother_location]
    

def solution():
    subin_location, brother_location = map(int, sys.stdin.readline().split())

    time = time_for_find_brother(subin_location, brother_location)
    print(time)

solution()