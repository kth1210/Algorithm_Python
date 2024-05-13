import sys
from collections import deque

def solution():
    N, M = map(int, sys.stdin.readline().split())
    locations = list(map(int, sys.stdin.readline().split()))
    queue = deque([number for number in range(1, N + 1)])
    count = 0

    for location in locations:
        left_count = 0
        while queue[0] != location:
            queue.rotate(-1)
            left_count += 1
        
        # 왼쪽, 오른쪽 회전 중 더 가까운 방법 선택
        right_count = len(queue) - left_count
        count += min(left_count, right_count)
        queue.popleft()
    
    print(count)


solution()

'''
N개 원소 양방향 순환 큐
1. popleft
2. rotate(-1)
3. rotate(1)

뽑으려고 하는 원소의 위치가 주어짐 (큐의 첫번째 상태에서의 위치)
1   2   3   4   5
4 찾는다 -> 왼쪽으로 회전 3번 또는 오른쪽으로 회전 2번
'''