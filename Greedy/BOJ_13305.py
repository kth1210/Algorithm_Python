import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    road_lengths = list(map(int, sys.stdin.readline().split()))
    prices = list(map(int, sys.stdin.readline().split()))

    current_price = prices[0]
    result = prices[0] * road_lengths[0]
    for idx in range(1, N-1):
        if current_price >= prices[idx]:
            current_price = prices[idx]
        result += current_price * road_lengths[idx]

    print(result)

solution()