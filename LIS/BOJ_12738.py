import sys

def find_location(array, value):
    start = 0
    end = len(array)
    result = 0

    while start <= end:
        mid = (start+end) // 2

        if array[mid] == value:
            return mid
        elif array[mid] > value:
            result = mid
            end = mid-1
        else:
            start = mid+1
        
    return result

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    LIS = [numbers[0]]

    for idx in range(1, N):
        if LIS[-1] < numbers[idx]:
            LIS.append(numbers[idx])
        else:
            location = find_location(LIS, numbers[idx])
            LIS[location] = numbers[idx]
    
    print(len(LIS))

solution()