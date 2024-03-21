import sys
from collections import deque

def print_result(numbers: list):
    str_num = ','.join(numbers)
    print(f'[{str_num}]')

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        str_p = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline().rstrip())
        str_numbers = sys.stdin.readline().rstrip()[1:-1]
        
        numbers = deque()
        if len(str_numbers) > 0:
            numbers = deque(list(str_numbers.split(',')))
        
        is_error = False
        is_r_even = False
        idx = 0
        r_count = 0
        while idx < len(str_p) and not is_error:
            while idx < len(str_p) and str_p[idx] == 'R':
                r_count += 1
                idx += 1

            is_r_even = r_count % 2 == 0
            while idx < len(str_p) and str_p[idx] == 'D':
                if len(numbers) > 0:
                    if is_r_even:
                        numbers.popleft()
                    else:
                        numbers.pop()
                else:
                    is_error = True
                    break
                idx += 1
        
        if not is_r_even:
            numbers.reverse()

        if not is_error:
            print_result(numbers)
        else:
            print('error')

solution()