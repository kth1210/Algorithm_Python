import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        input_parenthesis = sys.stdin.readline().rstrip()
        stack = []
        is_valid = True

        for parenthesis in input_parenthesis:
            if parenthesis == "(":
                stack.append(parenthesis)
            else:
                if not stack:
                    is_valid = False
                    break

                stack.pop()
        
        print("YES" if not stack and is_valid else "NO")

solution()