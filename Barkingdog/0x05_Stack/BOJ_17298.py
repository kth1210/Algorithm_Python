import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    NGE = [-1 for _ in range(N)]
    stack = []  # (위치, 숫자)

    for idx, number in enumerate(numbers):
        # 현재 숫자가 NGE 숫자인 경우 계산
        while stack and stack[-1][1] < number:
            NGE[stack[-1][0]] = number
            stack.pop()
            
        stack.append((idx, number))
    
    print(*NGE)


solution()