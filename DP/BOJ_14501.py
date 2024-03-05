import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    counsel = []

    for _ in range(N):
        T, P = map(int, sys.stdin.readline().split())
        counsel.append([T, P])
    
    benefit = [0 for _ in range(N)]
    for now in range(N):
        T, P = counsel[now][0], counsel[now][1]
        benefit[now] = P

        # 날짜가 넘어가는 경우
        if T + now > N:
            benefit[now] = 0
            continue

        for pre in range(now):
            pre_T = counsel[pre][0]
            # 이전 날의 상담 끝났는 지
            if pre_T + pre - 1 < now:
                benefit[now] = max(benefit[now], P + benefit[pre])

    print(max(benefit))

solution()