import sys
from collections import deque

def find_print_sequence(papers, current_location):
    queue = deque(papers)
    sequence = 1

    while queue:
        max_value = max(queue)
        current_value = queue.popleft()
        current_location -= 1

        # 궁금한 문서 차례일 때
        if current_location < 0:
            if current_value == max_value:
                return sequence
            elif current_value < max_value:
                queue.append(current_value)
                current_location = len(queue) - 1
        else:
            if current_value < max_value:
                queue.append(current_value)
            else:
                sequence += 1

    return -1

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        papers = list(map(int, sys.stdin.readline().split()))

        answer = find_print_sequence(papers, M)
        print(answer)

solution()