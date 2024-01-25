import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        if n == 1:
            print(1)
        elif n == 2:
            print(2)
        elif n == 3:
            print(4)
        else:
            number_of_ways = [0] * (n + 1)
            number_of_ways[1] = 1
            number_of_ways[2] = 2
            number_of_ways[3] = 4

            for number in range(4, n + 1):
                number_of_ways[number] = number_of_ways[number - 3] + number_of_ways[number - 2] + number_of_ways[number - 1]
            
            print(number_of_ways[n])

solution()