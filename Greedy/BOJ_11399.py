import sys

N = int(sys.stdin.readline().rstrip())
P = sorted(list(map(int, sys.stdin.readline().split())))
result = 0

for idx in range(len(P) + 1):
    result += sum(P[:idx])

print(result)