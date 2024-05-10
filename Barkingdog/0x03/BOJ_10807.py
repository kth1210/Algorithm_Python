import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    target_number = int(sys.stdin.readline().rstrip())
    count = 0

    for number in numbers:
        if number == target_number:
            count += 1
    
    print(count)

solution()