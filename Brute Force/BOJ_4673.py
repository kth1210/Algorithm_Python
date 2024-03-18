import sys

def d(n):
    result = n
    for digit in str(n):
        result += int(digit)
    return result

def solution():
    self_numbers = [True for _ in range(10_001)]

    for number in range(1, 10_001):
        next_number = d(number)
        if next_number < 10_001:
            self_numbers[next_number] = False
    
    for number in range(1, 10_001):
        if self_numbers[number]:
            print(number)

solution()