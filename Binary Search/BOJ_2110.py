import sys

def find_max_length(locations, C):
    start = 0
    end = locations[-1]
    length = 0

    while start <= end:
        mid = (start + end) // 2
        cur_location = locations[0]
        count = 1

        for location in locations:
            if location - mid >= cur_location:
                count += 1
                cur_location = location
        
        if count >= C:
            start = mid + 1
            length = max(length, mid)
        else:
            end = mid - 1
    
    return length


def solution():
    N, C = map(int, sys.stdin.readline().split())
    locations = []

    for _ in range(N):
        locations.append(int(sys.stdin.readline().rstrip()))
    
    locations.sort()
    
    max_length = find_max_length(locations, C)
    print(max_length)


solution()