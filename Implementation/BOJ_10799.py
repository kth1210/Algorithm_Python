import sys

def solution():
    input_parenthesis = sys.stdin.readline().rstrip()
    stick_count = 0
    answer = 0

    for idx in range(len(input_parenthesis)):
        current_parenthesis = input_parenthesis[idx]

        if current_parenthesis == "(":
            next_parenthesis = input_parenthesis[idx + 1]

            if next_parenthesis == ")":
                answer += stick_count
            else:
                stick_count += 1
        else:
            previous_parenthesis = input_parenthesis[idx - 1]

            if previous_parenthesis == ")":
                answer += 1
                stick_count -= 1

    print(answer)

solution()