import sys
import heapq

def solution():
    N = int(sys.stdin.readline().rstrip())
    cards = []

    for _ in range(N):
        cards.append(int(sys.stdin.readline().rstrip()))
    
    heapq.heapify(cards)

    count = 0
    for _ in range(N-1):
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        count += first + second
        heapq.heappush(cards, first + second)
    
    print(count)

solution()