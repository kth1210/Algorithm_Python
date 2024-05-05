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
                print(queue.popleft())
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            print(int(not queue))
        elif command == "front":
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif command == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1])

solution()