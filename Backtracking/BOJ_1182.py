import sys
answer = 0

def backtracking(numbers, selected_numbers, target_number):
    global answer
    if selected_numbers and sum(selected_numbers) == target_number:
        answer += 1
    
    for idx in range(len(numbers)):
        selected_numbers.append(numbers[idx])
        backtracking(numbers[idx+1:], selected_numbers, target_number)
        selected_numbers.pop()

def solution():
    global answer
    N, S = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    backtracking(numbers, [], S)

    print(answer)

solution()