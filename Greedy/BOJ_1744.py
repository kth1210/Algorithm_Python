import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    positive_numbers = []
    negative_numbers = []
    is_exist_zero = False

    for _ in range(N):
        input_number = int(sys.stdin.readline().rstrip())
        if input_number == 0:
            is_exist_zero = True
        elif input_number < 0:
            negative_numbers.append(input_number)
        else:
            positive_numbers.append(input_number)
    
    positive_numbers.sort(reverse = True)
    negative_numbers.sort()

    result = 0
    # 양수 -> 큰 수부터 2개씩 묶어서 계산
    for idx in range(0, len(positive_numbers) - 1, 2):
        # 둘 중 하나의 수가 1이라면 묶는 것보다 그냥 더하는게 더 큼
        if positive_numbers[idx] == 1 or positive_numbers[idx + 1] == 1:
            result += positive_numbers[idx] + positive_numbers[idx + 1]
        else:
            result += positive_numbers[idx] * positive_numbers[idx + 1]
    
    # 양수 개수가 홀수라면 마지막 수 더하기
    if len(positive_numbers) % 2 != 0:
        result += positive_numbers[-1]
    
    # 음수 -> 작은 수부터 2개씩 묶어서 계산
    for idx in range(0, len(negative_numbers) - 1, 2):
        result += negative_numbers[idx] * negative_numbers[idx + 1]
    
    # 음수 개수가 홀수이고, 0이 존재하지 않는다면 마지막 수 더하기
    # 0이 있다면 묶어서 음수 하나를 무시할 수 있기 때문
    if len(negative_numbers) % 2 != 0 and not is_exist_zero:
        result += negative_numbers[-1]
    
    print(result)

solution()