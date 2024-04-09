import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().rstrip())
    queue = deque()

    for _ in range(N):
        input_command = sys.stdin.readline().split()
        command = input_command[0]

        if command == "push":
            X = int(input_command[1])
            queue.append(X)
        elif command == "pop":
            if not queue:
                print(-1)
            else:
                front = queue.popleft()
                print(front)
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            print(1 if not queue else 0)
        elif command == "front":
            print(queue[0] if queue else -1)
        elif command == "back":
            print(queue[-1] if queue else -1)

solution()