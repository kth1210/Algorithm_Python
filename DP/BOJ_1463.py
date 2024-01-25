import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers_count = [0] * (N + 1)

    for number in range(1, N + 1):
        current_count = numbers_count[number]

        for next_number in [number + 1, number * 2, number * 3]:
            if next_number > N: continue

            if numbers_count[next_number] > current_count + 1 or numbers_count[next_number] == 0:
                numbers_count[next_number] = current_count + 1

    print(numbers_count[N])
    
solution()