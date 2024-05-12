import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    heights = list(map(int, sys.stdin.readline().split()))
    destinations = [-1 for _ in range(N)]
    stack = []

    for idx, height in enumerate(heights):
        if not stack:
            stack.append((height, idx))
        else:
            while stack and stack[-1][0] < height:
                stack.pop()
            
            if stack:
                destinations[idx] = stack[-1][1]
            
            stack.append((height, idx))

    for destination in destinations:
        destination += 1   
        print(destination, end = " ")

solution()

# 풀이 과정
'''
일직선 위에 N개의 높이가 서로 다른 탑 -> 방향
각 탑의 꼭대기에 레이저 송신기 설치 <- 방향으로 발사
    탑의 기둥에는 레이저 신호 수신하는 장치 있음
    레이저는 가장 먼저 만나는 하나의 탑에서만 수신 가능

각 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지?
    수신하는 탑이 존재하지 않으면 0

N이 500,000 -> N^2 불가능


6   9   5   7   4
0   0   0   0   0
0   0   0   0   0
0   0   2   0   0
0   0   2   2   4

stack에 없으면 지나가기
stack[-1]보다 큰 동안
    stack.pop

stack에 있으면 (큰 게 남음)
    stack[-1]보다 작으면
        stack[-1]의 위치 저장
        stack.append
없으면
    stack.append

stack
6,1   9,2   7,4
'''