import sys

def solution():
    K = int(sys.stdin.readline().rstrip())
    stack = []

    for _ in range(K):
        input_number = int(sys.stdin.readline().rstrip())

        if input_number == 0:
            stack.pop()
        else:
            stack.append(input_number)
        
    print(sum(stack))

solution()