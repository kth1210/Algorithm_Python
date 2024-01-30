import sys

def is_satisfy_condition(condition, current_condition):
    DNA = ["A", "C", "G", "T"]
    for idx in range(4):
        if condition[idx] > current_condition[DNA[idx]]:
            return False
    return True

def solution():
    S, P = map(int, sys.stdin.readline().split())
    input_DNA = sys.stdin.readline().rstrip()
    DNA_condition = list(map(int, sys.stdin.readline().split()))

    available_password_count = 0
    current_password = input_DNA[:P]
    current_condition = {
        "A": current_password.count('A'),
        "C": current_password.count('C'),
        "G": current_password.count('G'),
        "T": current_password.count('T')
    }
    
    if is_satisfy_condition(DNA_condition, current_condition):
        available_password_count += 1
    
    for idx in range(1, S-P+1):
        current_condition[input_DNA[idx-1]] -= 1
        current_condition[input_DNA[idx+P-1]] += 1

        if is_satisfy_condition(DNA_condition, current_condition):
            available_password_count += 1

    print(available_password_count)

solution()