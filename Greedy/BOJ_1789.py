import sys

def solution():
    S = int(sys.stdin.readline().rstrip())

    result = 0
    number = 0
    while result <= S:
        number += 1
        result += number

    print(number - 1)

solution()