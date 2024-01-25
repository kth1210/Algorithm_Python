import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        
        if N == 0:
            print(1, 0)
        elif N == 1:
            print(0, 1)
        else:
            fibonacci_count = [[0, 0] for _ in range(N + 1)]
            fibonacci_count[0] = [1, 0]
            fibonacci_count[1] = [0, 1]

            for number in range(2, N + 1):
                zero_count = fibonacci_count[number - 2][0] + fibonacci_count[number - 1][0]
                one_count = fibonacci_count[number - 2][1] + fibonacci_count[number - 1][1]
                fibonacci_count[number] = [zero_count, one_count]
            
            print(fibonacci_count[N][0], fibonacci_count[N][1])

solution()