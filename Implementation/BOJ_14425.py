import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    word_dict = {}
    count = 0

    for _ in range(N):
        input_word = sys.stdin.readline().rstrip()
        word_dict[input_word] = True
    
    for _ in range(M):
        find_word = sys.stdin.readline().rstrip()
        if find_word in word_dict:
            count += 1
    
    print(count)

solution()