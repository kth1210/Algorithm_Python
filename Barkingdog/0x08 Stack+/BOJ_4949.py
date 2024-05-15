import sys

def solution():
    while True:
        input_str = sys.stdin.readline().rstrip()
        if input_str == ".": break
        
        stack = []
        is_balance = True
        for character in input_str:
            if character == "(" or character == "[":
                stack.append(character)
            elif character == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    is_balance = False
                    break
            elif character == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    is_balance = False
                    break
        
        if not stack and is_balance:
            print("yes")
        else:
            print("no")

solution()