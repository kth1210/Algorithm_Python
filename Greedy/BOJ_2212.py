import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())
    locations = sorted(list(map(int, sys.stdin.readline().split())))
    distances = []
    
    for idx in range(len(locations) - 1):
        distances.append(locations[idx + 1] - locations[idx])

    distances.sort()
    
    print(sum(distances[:N - K]))


solution()