import sys

def is_prime(number):
    if number < 2: return False
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            return False
    return True

def solution():
    M, N = map(int, sys.stdin.readline().split())

    for number in range(M, N + 1):
        if is_prime(number):
            print(number)

solution()