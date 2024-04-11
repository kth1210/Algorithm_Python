import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    name_dict = {}
    number_dict = {}
    
    for number in range(1, N + 1):
        name = sys.stdin.readline().rstrip()
        name_dict[name] = number
        number_dict[number] = name
    
    for _ in range(M):
        input_pokemon = sys.stdin.readline().rstrip()

        if input_pokemon.isdigit():
            number = int(input_pokemon)
            print(number_dict[number])
        else:
            print(name_dict[input_pokemon])

solution()