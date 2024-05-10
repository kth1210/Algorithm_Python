import sys

def solution():
    S = sys.stdin.readline().rstrip()
    alpha_count = [0 for _ in range(ord('a'), ord('z') + 1)]

    for alpha in S:
        alpha_count[ord(alpha) - ord('a')] += 1
    
    print(*alpha_count)


solution()