import sys

def solution():
    N, K, Q, M = map(int, sys.stdin.readline().split())
    sleeping_numbers = list(map(int, sys.stdin.readline().split()))
    check_numbers = list(map(int, sys.stdin.readline().split()))
    # 모두 출석 안한 것으로 초기화
    cache = [1 for _ in range(N + 3)]
    prefix_sum = [0 for _ in range(N + 3)]

    # 출석 처리
    for number in check_numbers:
        if number in sleeping_numbers: continue

        for next_number in range(number, N + 3, number):
            if next_number not in sleeping_numbers:
                cache[next_number] = 0

    # 출석 안한 사람 수 누적합
    for idx in range(3, N + 3):
        prefix_sum[idx] = prefix_sum[idx - 1] + cache[idx]

    # 구간 출력
    for _ in range(M):
        S, E = map(int, sys.stdin.readline().split())
        print(prefix_sum[E] - prefix_sum[S - 1])

solution()

'''
학생 번호 = 3번 ~ N + 2번
출석 코드 한명한테 보내면 그사람이 자기 번호 배수 사람들한테 보내줌
근데 K명은 졸고 있어서 안보내줌

                졸
3   4   5   6   7   8   9   10  11  12
------------------------------------------
x   x   x   x   x   x   x   x   x   x
o   x   x   o   x   x   o   x   x   o
o   x   o   o   x   x   o   o   x   o
o   x   o   o   x   x   o   o   x   o
0   1   1   1   2   3   3   3   4   4
'''