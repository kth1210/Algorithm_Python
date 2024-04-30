import sys

def solution():
    N = int(sys.stdin.readline().rstrip())

    for number in range(1, N):
        cur_sum = sum(map(int, str(number))) + number
        
        if cur_sum == N:
            print(number)
            return
    
    print(0)


solution()