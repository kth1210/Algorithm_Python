import sys
import heapq

def solution():
    N = int(sys.stdin.readline().rstrip())
    heap = []

    for _ in range(N):
        input_number = int(sys.stdin.readline().rstrip())
        if input_number == 0:
            if heap:
                minimum_number = heapq.heappop(heap)
                print(minimum_number)
            else:
                print(0)
        else:
            heapq.heappush(heap, input_number)

solution()