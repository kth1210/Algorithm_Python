import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    words = {}

    for _ in range(N):
        input_word = sys.stdin.readline().rstrip()
        input_word_length = len(input_word)

        for idx, word in enumerate(input_word):
            weight = 10 ** (input_word_length - idx - 1)
            if word in words:
                words[word] = words[word] + weight
            else:
                words[word] = weight
    
    max_number = 9
    result = 0
    for value in reversed(sorted(words.values())):
        result += value * max_number
        max_number -= 1
    
    print(result)

solution()