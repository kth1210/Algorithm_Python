import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    heights = []
    stack = []
    count = 0

    for _ in range(N):
        heights.append(int(sys.stdin.readline().rstrip()))
    
    for height in heights:
        while stack and stack[-1] <= height:
            stack.pop()
        
        count += len(stack)
        stack.append(height)

    print(count)
        

solution()

# 풀이 과정
'''
N개의 빌딩
    i번째 빌딩의 키가 hi
    모든 빌딩은 오른쪽으로만 봄
각 빌딩에서 자신 빌딩보다 높거나 같은 빌딩은 옥상을 못봄
    볼 수 있는 옥상의 개수?

현재 빌딩을 볼 수 있는 관리인의 수를 구하기
10  3   7   4   12  2

stack
12  2
0
1
1
2
0
1
'''