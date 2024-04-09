import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().rstrip())
    input_numbers = list(map(int, sys.stdin.readline().split()))
    numbers = deque([(idx + 1, number) for idx, number in enumerate(input_numbers)])
    answer = []

    while numbers:
        front = numbers.popleft()
        idx = front[0]
        number = front[1]

        answer.append(idx)

        if numbers:
            if number > 0:
                number -= 1
            numbers.rotate(-number)

    print(*answer)

solution()