import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        input_str = sys.stdin.readline().rstrip()
        left_stack = []
        right_stack = []

        for command in input_str:
            if command == "<":
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif command == ">":
                if right_stack:
                    left_stack.append(right_stack.pop())
            elif command == "-":
                if left_stack:
                    left_stack.pop()
            else:
                left_stack.append(command)

        print("".join(left_stack + list(reversed(right_stack))))
        

solution()