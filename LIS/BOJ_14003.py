import sys

def find_location(arr, value):
    start = 0
    end = len(arr)
    result = -1

    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            result = mid
            end = mid - 1
        elif arr[mid] < value:
            start = mid + 1
    
    return result

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    temp_LIS = [numbers[0]]  
    lengths = [0 for _ in range(N)]

    for i in range(N):
        if numbers[i] > temp_LIS[-1]:
            temp_LIS.append(numbers[i])
            lengths[i] = len(temp_LIS)
        else:
            location = find_location(temp_LIS, numbers[i])
            temp_LIS[location] = numbers[i]
            lengths[i] = location+1
    
    max_length = max(lengths)
    print(max_length)

    LIS = []
    for idx in range(N-1, -1, -1):
        if lengths[idx] == max_length:
            LIS.append(numbers[idx])
            max_length -= 1
    
    print(*LIS[::-1])

solution()