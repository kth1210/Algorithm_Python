import sys

'''
선택된 알파벳으로 유효한 비밀번호를 만들 수 있는지 확인
'''
def is_valid(selected_characters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for character in selected_characters:
        if character in vowels:
            vowel_count += 1
    
    # 모음이 하나 이상, 자음이 두 개 이상인지 확인
    is_valid = (vowel_count >= 1) and (len(selected_characters) - vowel_count >= 2)
    return is_valid

'''
백트래킹을 통해 알파벳을 하나씩 선택
'''
def backtracking(passwords, characters, selected_characters, L):
    if len(selected_characters) == L:
        if is_valid(selected_characters):
            password = ''.join(selected_characters)
            passwords.append(password)
        return

    for idx in range(len(characters)):
        if not selected_characters or selected_characters[-1] < characters[idx]:
            selected_characters.append(characters[idx])
            backtracking(passwords, characters, selected_characters, L)
            selected_characters.pop()


def solution():
    L, _ = map(int, sys.stdin.readline().split())
    characters = list(sys.stdin.readline().split())

    passwords = []
    selected_characters = []
    backtracking(passwords, characters, selected_characters, L)

    for password in sorted(passwords):
        print(password)

solution()