import sys
from itertools import combinations

# 글자 배열에서 count만큼 선택해 추가한 이진수 단어 리스트를 반환
# 필수 글자 + 추가 글자
def make_bin_character_combinations(origin_bin_character, character_list, count):
    bin_combinations = []
    character_combinations = combinations(character_list, count)

    for character_combination in character_combinations:
        bin_character = origin_bin_character
        for characters in character_combination:
            bin_character = bin_character | make_bin_characters(characters)
        bin_combinations.append(bin_character)

    return bin_combinations

# 단어 포함 여부를 이진수로 변경해 반환
def make_bin_characters(characters):
    base = 0
    for character in characters:
        base = base | (1 << (ord(character)-97))
    return base

def solution():
    N, K = map(int, sys.stdin.readline().split())
    words = []
    essential_characters = ['a', 'c', 'i', 'n', 't']

    for _ in range(N):
        words.append(sys.stdin.readline().rstrip())
    
    if K < 5:
        print(0)
        return

    K -= 5
    learned_characters = essential_characters[:]
    bin_learned_characters = make_bin_characters(learned_characters)
    
    word_set = set()
    bin_words = []
    for word in words:
        bin_words.append(make_bin_characters(word))
        word_between_essential = word[4:-4]
        for character in word_between_essential:
            if character not in essential_characters:
                word_set.add(character)

    if len(word_set) <= K:
        print(N)
        return
    
    bin_character_combination = make_bin_character_combinations(bin_learned_characters, list(word_set), K)

    result = 0
    for bin_character in bin_character_combination:
        count = 0
        for bin_word in bin_words:
            if bin_character & bin_word == bin_word:
                count += 1
        result = max(result, count)
    
    print(result)

solution()