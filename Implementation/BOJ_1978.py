import sys

def is_prime(number):
    if number < 2: return False
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            return False
    return True

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    count = 0

    for number in numbers:
        if is_prime(number):
            count += 1
        
    print(count)

solution()