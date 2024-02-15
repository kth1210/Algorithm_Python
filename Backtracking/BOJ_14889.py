import sys

minimum_gap = sys.maxsize

# 두 팀의 점수 차이 계산
def calculate_gap(values, start_teammates, N):
    link_teammates = [teammate for teammate in range(1, N+1) if teammate not in start_teammates]
    start_team_point = 0
    link_team_point = 0

    for i in range(len(start_teammates)-1):
        for j in range(i+1, len(start_teammates)):
            s_teammate1, s_teammate2 = start_teammates[i]-1, start_teammates[j]-1
            l_teammate1, l_teammate2 = link_teammates[i]-1, link_teammates[j]-1
            start_team_point += values[s_teammate1][s_teammate2] + values[s_teammate2][s_teammate1]
            link_team_point += values[l_teammate1][l_teammate2] + values[l_teammate2][l_teammate1]
    
    return abs(start_team_point - link_team_point)


def find_minimum_gap(values, start_teammates, N):
    global minimum_gap

    # 스타트 팀 인원 수가 N/2 명이면 두 팀의 점수 차이 계산
    if len(start_teammates) == N//2:
        gap = calculate_gap(values, start_teammates, N)
        minimum_gap = min(minimum_gap, gap)
        return

    for teammate in range(1, N+1):
        if not start_teammates or teammate > start_teammates[-1]:
            start_teammates.append(teammate)
            find_minimum_gap(values, start_teammates, N)
            start_teammates.pop()


def solution():
    N = int(sys.stdin.readline().rstrip())
    values = []
    global minimum_gap

    for _ in range(N):
        values.append(list(map(int, sys.stdin.readline().split())))
    
    find_minimum_gap(values, [], N)
    print(minimum_gap)

solution()