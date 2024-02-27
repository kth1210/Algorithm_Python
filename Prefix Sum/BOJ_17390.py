import sys

def make_prefix_sum(N, sequence):
    prefix_sum = [0 for _ in range(N+1)]
    for idx in range(1, N+1):
        prefix_sum[idx] = sequence[idx-1] + prefix_sum[idx-1]
    return prefix_sum

def main():
    N, Q = map(int, sys.stdin.readline().split())
    sequence = sorted(list(map(int, sys.stdin.readline().split())))
    prefix_sum = make_prefix_sum(N, sequence)

    for _ in range(Q):
        L, R = map(int, sys.stdin.readline().split())
        answer = prefix_sum[R] - prefix_sum[L-1]
        print(answer)

main()