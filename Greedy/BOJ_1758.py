import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    tips = []

    for _ in range(N):
        tips.append(int(sys.stdin.readline().rstrip()))
    
    tips.sort(reverse = True)

    answer = 0
    for idx, tip in enumerate(tips):
        if tip - idx > 0:
            answer += tip - idx

    print(answer)
    
solution()