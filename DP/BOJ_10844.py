import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    history = [[0 for _ in range(10)] for _ in range(N+1)]

    for last_num in range(1, 10):
        history[1][last_num] = 1
    
    for num in range(2, N+1):
        for last_num in range(10):
            if last_num == 0:
                history[num][last_num] = history[num-1][1]
            elif last_num == 9:
                history[num][last_num] = history[num-1][8]
            else:
                history[num][last_num] = history[num-1][last_num-1] + history[num-1][last_num+1]
    
    answer = sum(history[N])
    print(answer % 1_000_000_000)

solution()