import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    budget_list = list(map(int, sys.stdin.readline().split()))
    total_budget = int(sys.stdin.readline().rstrip())

    start = 0
    end = max(budget_list)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for budget in budget_list:
            total += min(budget, mid)
        
        if total <= total_budget:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)

solution()