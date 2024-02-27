import sys

def solution(N, S, sequence):
    min_length = N
    left_idx = 0
    prefix_sum = [0 for _ in range(N+1)]

    # 합을 만드는게 불가능한 경우
    if sum(sequence) < S:
        print(0)
        return

    for right_idx in range(N):
        current_value = prefix_sum[right_idx-1] + sequence[right_idx]

        # 왼쪽 끝 수를 빼도 S보다 클 때 -> 길이 줄여도 됨
        while current_value-sequence[left_idx] >= S:
            current_value -= sequence[left_idx]
            left_idx += 1

        if current_value >= S:
            min_length = min(min_length, right_idx-left_idx+1)

        prefix_sum[right_idx] = current_value

    print(min_length)

def main():
    N, S = map(int, sys.stdin.readline().split())
    sequence = list(map(int, sys.stdin.readline().split()))
    solution(N, S, sequence)
    
    # solution(10, 15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) # 2
    # solution(5, 1, [1, 1, 1, 1, 1]) # 1
    # solution(5, 15, [1, 2, 3, 4, 5]) # 5
    # solution(5, 15, [10, 1, 1, 1, 2]) # 5
    # solution(5, 15, [1, 1, 1, 15, 1]) # 1
    # solution(5, 10, [1, 1, 5, 4, 1]) # 3
    # solution(5, 10, [10, 1, 1, 1, 1]) # 1

main()