import sys
import heapq

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        K = int(sys.stdin.readline().rstrip())
        min_heap = []
        max_heap = []
        num_dict = {}
        count = 0
        operations = []

        for _ in range(K):
            operations.append(sys.stdin.readline().rstrip())
        
        for operation in operations:
            str_op, str_num = operation.split()

            if str_op == "I":
                number = int(str_num)
                heapq.heappush(min_heap, number)
                heapq.heappush(max_heap, -number)
                if number in num_dict:
                    num_dict[number] += 1
                else:
                    num_dict[number] = 1
                count += 1
            elif str_op == "D":
                if count <= 0:
                    continue

                count -= 1
                if str_num == "1":
                    number = heapq.heappop(max_heap)
                        
                    while -number not in num_dict:
                        number = heapq.heappop(max_heap)

                    num_dict[-number] -= 1
                    if num_dict[-number] == 0:
                        num_dict.pop(-number)

                elif str_num == "-1":
                    number = heapq.heappop(min_heap)

                    while number not in num_dict:
                        number = heapq.heappop(min_heap)

                    num_dict[number] -= 1
                    if num_dict[number] == 0:
                        num_dict.pop(number)

        if count == 0:
            print("EMPTY")
        else:
            min_value = heapq.heappop(min_heap)
            while min_value not in num_dict:
                min_value = heapq.heappop(min_heap)

            max_value = heapq.heappop(max_heap)
            while -max_value not in num_dict:
                max_value = heapq.heappop(max_heap)

            print(-max_value, min_value)


solution()