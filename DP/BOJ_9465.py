import sys

def solution(n, stickers):
    cache = [[0 for _ in range(n)] for _ in range(2)]
    cache[0][0] = stickers[0][0]
    cache[1][0] = stickers[1][0]

    if n < 2:
        answer = max(cache[0][0], cache[1][0])
        print(answer)
        return

    for idx in range(1, n):
        if idx == 1:
            cache[0][idx] = cache[1][idx - 1] + stickers[0][idx]
            cache[1][idx] = cache[0][idx - 1] + stickers[1][idx]
        else:
            cache[0][idx] = max(cache[1][idx - 1], cache[1][idx - 2], cache[0][idx - 2]) + stickers[0][idx]
            cache[1][idx] = max(cache[0][idx - 1], cache[0][idx - 2], cache[1][idx - 2]) + stickers[1][idx]
    
    answer = max(cache[0][n - 1], cache[1][n - 1])
    print(answer)


'''
input, test case
'''
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    
    solution(n, stickers)