import sys

word = sys.stdin.readline().rstrip()
word_dict = dict()

for char in word:
    char = char.lower()
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 0
    
sorted_word = sorted(word_dict.items(), key = lambda x: -x[1])

if len(sorted_word) < 2:
    print(sorted_word[0][0].upper())
else:
    if sorted_word[0][1] == sorted_word[1][1]:
        print("?")
    else:
        print(sorted_word[0][0].upper())