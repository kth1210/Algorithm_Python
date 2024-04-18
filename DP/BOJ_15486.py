import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    time_cost_list = []
    cache = [0 for _ in range(N + 1)]

    for _ in range(N):
        T, P = map(int, sys.stdin.readline().split())
        time_cost_list.append((T, P))
    
    for day in range(N):
        time, price = time_cost_list[day]
        
        cache[day + 1] = max(cache[day + 1], cache[day])
        # 퇴사 전에 처리할 수 있는지 확인
        if day + time <= N:
            cache[day + time] = max(cache[day + time], cache[day] + price)
        
    print(max(cache))

solution()