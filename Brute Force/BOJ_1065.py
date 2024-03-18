import sys

def solution(N):
    count = 0

    for number in range(1, N + 1):
        number_str = str(number)

        if len(number_str) <= 2:
            count += 1
        else:
            is_hansu = True
            gap = int(number_str[1]) - int(number_str[0])
            for idx in range(2, len(number_str)):
                if int(number_str[idx]) - int(number_str[idx - 1]) != gap:
                    is_hansu = False
            if is_hansu:
                count += 1

    print(count)

'''
input
'''
N = int(sys.stdin.readline().rstrip())
solution(N)