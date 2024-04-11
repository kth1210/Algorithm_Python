import sys
from itertools import combinations

'''
각 괄호쌍의 위치를 (left_idx, right_idx)로 저장
모든 괄호쌍에서 조합으로 1 ~ 괄호 개수만큼 뽑음
뽑은 위치는 제외할 괄호의 위치가 됨
'''
def solution():
    input_formula = sys.stdin.readline().rstrip()
    parenthesis_locations = []
    stack = []
    answers = set()

    # 각 괄호쌍의 위치를 저장
    for idx in range(len(input_formula)):
        if input_formula[idx] == "(":
            stack.append(idx)
        elif input_formula[idx] == ")":
            previous_location = stack.pop()
            parenthesis_locations.append((previous_location, idx))

    # 모든 괄호쌍에서 조합으로 1 ~ 괄호 개수만큼 뽑음
    for count in range(1, len(parenthesis_locations) + 1):
        for case in combinations(parenthesis_locations, count):
            base_formula = list(input_formula)

            # 뽑은 위치의 괄호를 제거
            for (left, right) in case:
                base_formula[left] = ""
                base_formula[right] = ""
            
            answers.add("".join(base_formula))
    
    for answer in sorted(list(answers)):
        print(answer)

solution()