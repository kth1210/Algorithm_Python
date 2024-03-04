import sys

def solution():
    N, d, k, c = map(int, sys.stdin.readline().split())
    sushi_list = []
    sushi_dict = {}
    
    for _ in range(N):
        sushi_list.append(int(sys.stdin.readline().rstrip()))

    for idx in range(1, d+1):
        sushi_dict[idx] = 0
    
    count = 0
    for sushi in sushi_list[:k]:
        if sushi_dict[sushi] == 0:
            count += 1
        sushi_dict[sushi] += 1
    
    answer = count if sushi_dict[c] else count+1
    for left in range(N):
        right = (left+k) % N
        left_sushi = sushi_list[left]
        right_sushi = sushi_list[right]

        sushi_dict[left_sushi] -= 1
        if sushi_dict[left_sushi] == 0:
            count -= 1
        
        if sushi_dict[right_sushi] == 0:
            count += 1
        sushi_dict[right_sushi] += 1

        if sushi_dict[c] == 0:
            answer = max(answer, count+1)
        else:
            answer = max(answer, count)
        
    print(answer)

solution()