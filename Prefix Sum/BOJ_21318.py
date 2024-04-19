import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    difficulties = list(map(int, sys.stdin.readline().split()))
    Q = int(sys.stdin.readline().rstrip())
    is_miss = [0 for _ in range(N)]
    prefix_sum = [0 for _ in range(N + 1)]

    # 실수 여부 확인
    for idx in range(N - 1):
        if difficulties[idx] > difficulties[idx + 1]:
            is_miss[idx] = 1

    # 누적합 구성
    for idx in range(1, N + 1):
        prefix_sum[idx] = prefix_sum[idx - 1] + is_miss[idx - 1]

    # 실수하는 곡 개수 출력
    for _ in range(Q):
        x, y = map(int, sys.stdin.readline().split())
        
        # 한 곡만 하는 경우
        if x == y:
            print(0)
        else:
            # 마지막 곡에서는 실수하지 않음
            y -= 1
            print(prefix_sum[y] - prefix_sum[x - 1])


solution()

'''
악보 1 ~ N 번
난이도를 가지고 있음
x번 ~ y번 악보를 순서대로 연주하는게 피아노 체조임
지금 연주하는 악보가 다음 악보보다 어렵다면 실수함
    근데 마지막 y번 악보는 절대 실수 안함
        만약에 2 ~ 5번이라면? 2 ~ 4번만 실수하는지 확인하면 됨
실수하는 곡 몇개?

1   2   3   4   5   6   7   8   9
1   2   3   3   4   1   10  8   1
-------------------------------------
is_miss
0   0   0   0   1   0   1   1   0
prefix_sum
0   0   0   0   1   1   2   3   3
'''