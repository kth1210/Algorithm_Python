import sys
from collections import deque

'''
제일 위에 있는 카드 버림
    이때 남은 카드 수가 한장이면 걔가 정답임
제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
마지막에 남는 카드?
'''
def solution():
    N = int(sys.stdin.readline().rstrip())
    cards = deque([card for card in range(1, N + 1)])

    if N == 1:
        print(1)
        return

    while cards:
        cards.popleft()

        if len(cards) == 1:
            print(cards[0])
            return
        
        top = cards.popleft()
        cards.append(top)

solution()