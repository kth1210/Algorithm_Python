import sys

min_value = sys.maxsize
max_value = -sys.maxsize

def backtracking(current_value, idx, numbers, operators_count):
    global min_value
    global max_value

    if idx == len(numbers):
        min_value = min(min_value, current_value)
        max_value = max(max_value, current_value)
        return
    
    current_number = numbers[idx]
    for operator, count in operators_count.items():
        if count > 0:
            operators_count[operator] -= 1
            eval_value = 0
            
            if operator == "+":
                eval_value = current_value + current_number
            elif operator == "-":
                eval_value = current_value - current_number
            elif operator == "*":
                eval_value = current_value * current_number
            elif operator == "/":
                eval_value = current_value // current_number
                if current_value < 0 and current_number > 0:
                    eval_value = -((-current_value) // current_number)

            backtracking(eval_value, idx+1, numbers, operators_count)
            operators_count[operator] += 1

def solution():
    global min_value
    global max_value

    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    operators = ["+", "-", "*", "/"]
    operators_count = {}
    input_operators_count = list(map(int, sys.stdin.readline().split()))

    for idx, count in enumerate(input_operators_count):
        operators_count[operators[idx]] = count    

    current_value = numbers[0]
    backtracking(current_value, 1, numbers, operators_count)

    print(max_value)
    print(min_value)

solution()