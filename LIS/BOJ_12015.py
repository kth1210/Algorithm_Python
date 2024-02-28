import sys

# value가 arr에서 어디에 들어갈 지 찾음
# value보다 큰 arr의 숫자 중 가장 작은 숫자의 위치에 들어가면 됨
def find_location(arr, value):
    start = 0
    end = len(arr)
    result = 0

    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            # value보다 큰 arr의 숫자의 위치는 저장하고 더 작은 숫자 있는지 탐색
            result = mid
            end = mid - 1
        elif arr[mid] < value:
            start = mid + 1

    return result

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    LIS = [numbers[0]]

    for number in numbers:
        if number > LIS[-1]: # LIS의 최대 값보다 크면 뒤에 붙이기
            LIS.append(number)
        else: # 그렇지 않으면, 해당 숫자가 LIS에서 어떤 위치에 들어갈 지 찾기
            location = find_location(LIS, number)
            LIS[location] = number
    
    print(len(LIS))

solution()