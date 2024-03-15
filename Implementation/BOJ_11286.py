import sys
import heapq

def solution():
    N = int(sys.stdin.readline().rstrip())
    heap = []

    for _ in range(N):
        input_number = int(sys.stdin.readline().rstrip())
        abs_number = abs(input_number)
        if input_number == 0:
            if heap:
                _, minimum_number = heapq.heappop(heap)
                print(minimum_number)
            else:
                print(0)
        else:
            heapq.heappush(heap, (abs_number, input_number))

solution()