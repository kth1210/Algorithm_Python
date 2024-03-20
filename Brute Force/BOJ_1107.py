import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())

    if M == 0:
        print(min(len(str(N)), abs(N - 100)))
        return

    disable_buttons = list(map(int, sys.stdin.readline().split()))

    if M == 10:
        print(abs(N - 100))
        return
    if N == 100:
        print(0)
        return

    count = abs(N - 100)
    for number in range(1_000_000):
        str_number = str(number)
        is_makeable = True

        for idx in range(len(str_number)):
            if int(str_number[idx]) in disable_buttons:
                is_makeable = False
                break
        
        if is_makeable:
            cur_count = len(str_number) + abs(N - number)
            count = min(count, cur_count)

    print(count)
    
solution()