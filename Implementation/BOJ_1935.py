import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    input_formula = sys.stdin.readline().rstrip()
    alpha_dict = {}
    stack = []

    for idx in range(N):
        number = int(sys.stdin.readline().rstrip())
        alpha_ord = idx + ord("A")
        alpha_dict[chr(alpha_ord)] = number
    
    for oper in input_formula:
        if oper.isalpha():
            stack.append(alpha_dict[oper])
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            if oper == "+":    
                stack.append(op1 + op2)
            elif oper == "-":
                stack.append(op1 - op2)
            elif oper == "*":
                stack.append(op1 * op2)
            elif oper == "/":
                stack.append(op1 / op2)
    
    answer = stack[0]
    print(f"{answer:.2f}")

solution()