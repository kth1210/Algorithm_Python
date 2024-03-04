import sys

def solution():
    N, d, k, c = map(int, sys.stdin.readline().split())
    sushi_list = []
    for _ in range(N):
        sushi_list.append(int(sys.stdin.readline().rstrip()))
    
    count = 0
    for left in range(N):
        right = left+k
        if right >= N:
            right = right-N
            sushi_set = set(sushi_list[left:] + sushi_list[:right])
        else:
            sushi_set = set(sushi_list[left:right])
        
        sushi_count = len(sushi_set)
        if c not in sushi_set:
            sushi_count += 1

        count = max(count, sushi_count)
    
    print(count)

solution()