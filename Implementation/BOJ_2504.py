import sys

def solution():
    input_parenthesis = sys.stdin.readline().rstrip()
    stack = []

    for parenthesis in input_parenthesis:
        if parenthesis == "(" or parenthesis == "[":
            stack.append(parenthesis)
        elif parenthesis == ")":
            pre_value = 0
            while stack and stack[-1] != "(":
                # 괄호 사이에 계산되지 않은 것이 존재하면 잘못된 식
                if not stack[-1].isdigit():
                    print(0)
                    return
                pre_value += int(stack.pop())

            # 여는 괄호 매칭이 안되면 잘못된 식
            try:
                stack.pop()
            except:
                print(0)
                return
            
            if pre_value == 0:
                stack.append("2")
            else:
                stack.append(str(pre_value * 2))
        elif parenthesis == "]":
            pre_value = 0
            while stack and stack[-1] != "[":
                # 괄호 사이에 계산되지 않은 것이 존재하면 잘못된 식
                if not stack[-1].isdigit():
                    print(0)
                    return
                pre_value += int(stack.pop())
            
            # 여는 괄호 매칭이 안되면 잘못된 식
            try:
                stack.pop()
            except:
                print(0)
                return
            
            if pre_value == 0:
                stack.append("3")
            else:
                stack.append(str(pre_value * 3))

    # 스택에 계산되지 않은 수가 있으면 잘못된 식
    try:
        answer = sum(map(int, stack))
        print(answer)
    except:
        print(0)

solution()