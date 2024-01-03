import sys

N, K = map(int, sys.stdin.readline().split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse = True)

count = 0
for coin in coins:
    if coin <= K:
        count += K // coin
        K %= coin

print(count)