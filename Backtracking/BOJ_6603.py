import sys

def backtracking(numbers, selected_numbers):
    if len(selected_numbers) == 6:
        print(*selected_numbers)
        return

    for idx in range(len(numbers)):
        selected_numbers.append(numbers[idx])
        backtracking(numbers[idx+1:], selected_numbers)
        selected_numbers.pop()

def solution():
    test_cases = []
    while True:
        input_row = list(map(int, sys.stdin.readline().split()))

        if input_row[0] == 0:
            break
        else:
            test_cases.append(input_row)
    
    for idx in range(len(test_cases)):
        k = test_cases[idx][0]
        numbers = test_cases[idx][1:]

        backtracking(numbers, [])
        if idx < len(test_cases) - 1:
            print()

solution()