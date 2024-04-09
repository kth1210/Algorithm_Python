import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    stack = []

    for _ in range(N):
        input_command = sys.stdin.readline().split()
        command = input_command[0]
        
        if command == "push":
            X = int(input_command[1])
            stack.append(X)
        elif command == "pop":
            if not stack:
                print(-1)
            else:
                number = stack.pop()
                print(number)
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            print(1 if not stack else 0)
        elif command == "top":
            if not stack:
                print(-1)
            else:
                print(stack[-1])

solution()