import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    x = int(sys.stdin.readline().rstrip())
    number_set = {}
    count = 0

    for number in numbers:
        if (x-number) in number_set:
            count += 1

        number_set[number] = 1
    
    print(count)

solution()