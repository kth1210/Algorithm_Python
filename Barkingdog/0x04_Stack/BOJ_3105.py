import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    heights = []
    stack = []  # (키, 나온 횟수)
    count = 0

    for _ in range(N):
        heights.append(int(sys.stdin.readline().rstrip()))
    
    for height in heights:
        while stack and stack[-1][0] < height:
            count += stack.pop()[1]

        # 같은 키가 남아있는 경우
        if stack and stack[-1][0] == height:
            same_height_count = stack.pop()[1]
            count += same_height_count
            
            # 같은 키 제외하고 더 큰 키도 있는 경우
            if stack:
                count += 1

            stack.append((height, same_height_count + 1))
        else:
            # 큰 키만 있는 경우
            if stack:
                count += 1
            stack.append((height, 1))
    
    print(count)

solution()