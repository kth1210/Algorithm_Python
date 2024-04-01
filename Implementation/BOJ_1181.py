import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    words_set = set()

    for _ in range(N):
        words_set.add(sys.stdin.readline().rstrip())
    
    words = list(words_set)
    words.sort(key = lambda x: (len(x), x))

    for word in words:
        print(word)

solution()