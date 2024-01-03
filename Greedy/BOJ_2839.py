import sys

def solution(N):
    result = -1

    for count_of_five in range(N // 5 + 1):
        temp = N
        if (temp - 5 * count_of_five) % 3 == 0:
            temp -= 5 * count_of_five
            if result != -1:
                result = min(count_of_five + temp // 3, result)
            else:
                result = count_of_five + temp // 3

    print(result)

N = int(sys.stdin.readline().rstrip())

solution(N)