import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    fibonacci = [0 for _ in range(n+1)]

    if n < 2:
        print(n)
    else:
        fibonacci[1] = 1

        for idx in range(2, n+1):
            fibonacci[idx] = fibonacci[idx-2] + fibonacci[idx-1]
        
        print(fibonacci[n])
        
solution()