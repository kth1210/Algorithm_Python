import sys

def solution(str1, str2):
    dp = [0 for _ in range(len(str1))]

    for char in str2:
        pre_value = 0
        for idx in range(len(str1)):
            if char == str1[idx]:
                if pre_value < dp[idx]:
                    pre_value = dp[idx]
                else:
                    dp[idx] = pre_value + 1
            else:
                pre_value = max(pre_value, dp[idx])
    
    print(max(dp))

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
solution(str1, str2)

# solution("XXXXXF", "XFXXXQ") # 4