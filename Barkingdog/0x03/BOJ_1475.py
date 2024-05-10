import sys

def solution():
    N = sys.stdin.readline().rstrip()
    number_count = [0 for _ in range(10)]

    for number_str in N:
        number = int(number_str)

        if number == 9:
            if number_count[6] > number_count[9]:
                number_count[9] += 1
            else:
                number_count[6] += 1
        elif number == 6:
            if number_count[9] > number_count[6]:
                number_count[6] += 1
            else:
                number_count[9] += 1
        else:
            number_count[number] += 1

    print(max(number_count))

solution()