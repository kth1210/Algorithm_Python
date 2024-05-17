import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    count = 0

    for _ in range(N):
        word = sys.stdin.readline().rstrip()
        stack = []

        for character in word:
            if stack and stack[-1] == character:
                stack.pop()
            else:
                stack.append(character)
        
        if not stack:
            count += 1

    print(count)

solution()