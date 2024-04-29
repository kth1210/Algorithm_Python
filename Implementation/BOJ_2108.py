import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = []

    for _ in range(N):
        numbers.append(int(sys.stdin.readline().rstrip()))

    # 산술평균
    print(f"{round(sum(numbers) / N)}")

    # 중앙값
    numbers.sort()
    print(numbers[N // 2])

    # 최빈값
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    sorted_count = sorted(count_dict.items(), key = lambda x: -x[1])
    if N > 1:
        if sorted_count[0][1] == sorted_count[1][1]:
            print(sorted_count[1][0])
        else:
            print(sorted_count[0][0])
    else:
        print(sorted_count[0][0])

    # 범위
    print(numbers[-1] - numbers[0])

solution()