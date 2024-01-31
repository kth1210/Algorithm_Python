import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    cards = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline().rstrip())
    cards_to_find = list(map(int, sys.stdin.readline().split()))
    cards_count = {}

    for number in cards:
        if number in cards_count:
            cards_count[number] += 1
        else:
            cards_count[number] = 1

    for number in cards_to_find:
        print(cards_count.get(number, 0), end=' ')

solution()