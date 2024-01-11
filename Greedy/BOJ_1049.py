import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    prices = []

    for _ in range(M):
        package_price, individual_price = map(int, sys.stdin.readline().split())
        prices.append([package_price, individual_price])
    
    minimum_individual_price = sorted(prices, key = lambda x: x[1])[0][1]
    minimum_package_price = min(sorted(prices, key = lambda x: x[0])[0][0], minimum_individual_price * 6)

    result_price = 0
    result_price += minimum_package_price * (N // 6)
    result_price += min(minimum_individual_price * (N % 6), minimum_package_price)

    print(result_price)

solution()