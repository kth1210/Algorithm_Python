import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    meetings = []
    now_time = 0
    count = 0

    for _ in range(N):
        start_time, end_time = map(int, sys.stdin.readline().split())
        meetings.append((start_time, end_time))

    meetings.sort(key = lambda x: (x[1], x[0]))

    meeting_index = 0
    while meeting_index < len(meetings):
        if meetings[meeting_index][0] >= now_time:
            count += 1
            now_time = meetings[meeting_index][1]
        meeting_index += 1
    
    print(count)

solution()