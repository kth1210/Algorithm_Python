import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        K = int(sys.stdin.readline().rstrip())
        N = int(sys.stdin.readline().rstrip())

        apartment = [[1 for _ in range(N)] for _ in range(K + 1)]
        apartment[0] = [count for count in range(1, N + 1)]

        for floor in range(1, K + 1):
            for room in range(1, N):
                apartment[floor][room] = apartment[floor - 1][room] + apartment[floor][room - 1]
        
        print(apartment[K][N - 1])

solution()