import sys

def solution():
    first_word = sys.stdin.readline().rstrip()
    second_word = sys.stdin.readline().rstrip()
    word_count = {}
    count = 0 # 공통 부분 길이

    for word in first_word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
    for word in second_word:
        if word in word_count:
            count += 1
            word_count[word] -= 1
            if word_count[word] == 0:
                word_count.pop(word)
    
    print(len(first_word) + len(second_word) - 2*count)

solution()