import sys

def find_maximum_length(lengths, count):
    low = 1
    high = max(lengths)
    maximum_length = 1

    while low <= high:
        current_length = (low+high) // 2

        current_count = 0
        for length in lengths:
            current_count += length // current_length
        
        if current_count >= count:
            maximum_length = current_length
            low = current_length + 1
        else:
            high = current_length - 1
    
    return maximum_length


def solution():
    K, N = map(int, sys.stdin.readline().split())
    LAN_lengths = []

    for _ in range(K):
        LAN_lengths.append(int(sys.stdin.readline().rstrip()))
    
    maximum_length = find_maximum_length(LAN_lengths, N)
    print(maximum_length)

solution()