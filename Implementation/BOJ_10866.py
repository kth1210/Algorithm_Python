import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().rstrip())
    deq = deque()

    for _ in range(N):
        input_command = sys.stdin.readline().split()
        command = input_command[0]

        if command == "push_front":
            X = int(input_command[1])
            deq.appendleft(X)
        elif command == "push_back":
            X = int(input_command[1])
            deq.append(X)
        elif command == "pop_front":
            if not deq:
                print(-1)
            else:
                front = deq.popleft()
                print(front)
        elif command == "pop_back":
            if not deq:
                print(-1)
            else:
                back = deq.pop()
                print(back)
        elif command == "size":
            print(len(deq))
        elif command == "empty":
            print(1 if not deq else 0)
        elif command == "front":
            print(deq[0] if deq else -1)
        elif command == "back":
            print(deq[-1] if deq else -1)

solution()