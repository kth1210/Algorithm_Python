import sys
import heapq

def solution():
    N = int(sys.stdin.readline().rstrip())
    heap = []

    for _ in range(N):
        input_numbers = map(int, sys.stdin.readline().split())

        for number in input_numbers:
            if len(heap) < N:
                heapq.heappush(heap, number)
            else:
                if heap[0] < number:
                    heapq.heappop(heap)
                    heapq.heappush(heap, number)
    
    print(heap[0])

solution()