import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        answer_cache = [0] * (n + 1)
        answer_cache[1] = 1
        answer_cache[2] = 2

        for number in range(3, n + 1):
            answer_cache[number] = (answer_cache[number - 2] + answer_cache[number - 1]) % 10_007
        
        print(answer_cache[n])

solution()