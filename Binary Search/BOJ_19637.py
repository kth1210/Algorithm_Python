import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    level_list = []

    for _ in range(N):
        level_name, level_maximum = sys.stdin.readline().split()
        level_list.append((level_name, int(level_maximum)))
    
    for _ in range(M):
        point = int(sys.stdin.readline().rstrip())

        start = 0
        end = N - 1
        answer = ""

        while start <= end:
            mid = (start + end) // 2
            level_name, level_maximum = level_list[mid]

            if point <= level_maximum:
                answer = level_name
                end = mid - 1
            else:
                start = mid + 1

        print(answer)
            

solution()