import sys

def solution():
    changes = [500, 100, 50, 10, 5, 1]
    price = int(sys.stdin.readline().rstrip())
    output_change = 1000 - price

    result = 0
    for change in changes:
        if output_change >= change:
            result += output_change // change
            output_change %= change
        
    print(result)

solution()