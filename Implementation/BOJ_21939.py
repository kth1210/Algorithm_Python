import sys
import heapq

def solution():
    N = int(sys.stdin.readline().rstrip())
    min_heap = []
    max_heap = []
    solved = {}

    for _ in range(N):
        P, L = map(int, sys.stdin.readline().split())
        heapq.heappush(min_heap, (L, P))
        heapq.heappush(max_heap, (-L, -P))
    
    M = int(sys.stdin.readline().rstrip())

    for _ in range(M):
        input_command = sys.stdin.readline().split()
        command = input_command[0]

        if command == "add":
            P, L = map(int, input_command[1:])
            
            while min_heap[0][1] in solved:
                heapq.heappop(min_heap)
            while -max_heap[0][1] in solved:
                heapq.heappop(max_heap)

            heapq.heappush(min_heap, (L, P))
            heapq.heappush(max_heap, (-L, -P))

            if P in solved:
                solved.pop(P)
        elif command == "solved":
            P = int(input_command[1])
            solved[P] = True
        elif command == "recommend":
            x = int(input_command[1])
            if x == 1:
                # 가장 어려운 문제 꺼내기
                while max_heap:
                    most_difficult = heapq.heappop(max_heap)
                    # solved가 아닌 문제여야 함
                    if -most_difficult[1] not in solved:
                        print(-most_difficult[1])
                        heapq.heappush(max_heap, most_difficult)
                        break
            elif x == -1:
                # 가장 쉬운 문제 꺼내기
                while min_heap:
                    easiest = heapq.heappop(min_heap)
                    # solved가 아닌 문제여야 함
                    if easiest[1] not in solved:
                        print(easiest[1])
                        heapq.heappush(min_heap, easiest)
                        break
                
solution()