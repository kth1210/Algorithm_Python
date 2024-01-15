import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    count = 0
    while n > 0:
        if n % 5 == 0:
            count += n // 5
            n = 0
        else:
            count += 1
            n -= 2
    
    if n != 0:
        print(-1)
    else:
        print(count)

solution()