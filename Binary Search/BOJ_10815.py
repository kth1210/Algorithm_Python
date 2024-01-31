import sys

def find_numbers(cards, number):
    start = 0
    end = len(cards) - 1

    while start <= end:
        mid = (start+end) // 2

        if cards[mid] == number:
            return True
        elif cards[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

def solution():
    N = int(sys.stdin.readline().rstrip())
    cards = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))

    for number in numbers:
        if find_numbers(cards, number):
            print(1, end = ' ')
        else:
            print(0, end = ' ')


solution()