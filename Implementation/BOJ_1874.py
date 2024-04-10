import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    numbers = []
    stack = []
    pointer = 0
    answer = ""

    for _ in range(n):
        numbers.append(int(sys.stdin.readline().rstrip()))
    
    for number in range(1, n + 1):
        stack.append(number)
        answer += "+"

        while stack and stack[-1] == numbers[pointer]:
            stack.pop()
            answer += "-"
            pointer += 1

    if stack:
        print("NO")
    else:
        for op in answer:
            print(op)

solution()