import sys
import heapq

def solution(numbers):
    left_queue = []
    right_queue = []
    mid = numbers[0]
    answer = [mid]

    for idx in range(1, len(numbers)):
        number = numbers[idx]
        count = idx + 1
        
        # mid보다 작은 값은 left_queue에,
        # 크거나 같은 값은 right_queue에 저장
        if number < mid:
            heapq.heappush(left_queue, -number)
        else:
            heapq.heappush(right_queue, number)
        
        # left_queue와 right_queue의 균형을 맞추며 중앙값 계산
        if count % 2 == 1:
            if len(left_queue) > len(right_queue):
                heapq.heappush(right_queue, mid)
                mid = -heapq.heappop(left_queue)
            elif len(left_queue) < len(right_queue):
                heapq.heappush(left_queue, -mid)
                mid = heapq.heappop(right_queue)
        
            answer.append(mid)

    # 출력
    print(len(answer))
    for idx in range(0, len(answer), 10):
        print(*answer[idx:idx + 10])


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M = int(sys.stdin.readline().rstrip())
    numbers = []
    count = M // 10 if M % 10 == 0 else M // 10 + 1

    for _ in range(count):
        numbers += list(map(int, sys.stdin.readline().split()))

    solution(numbers)