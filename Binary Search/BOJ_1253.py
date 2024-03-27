import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers.sort()

    if N < 3:
        print(0)
        return

    count = 0
    for idx in range(N):
        number = numbers[idx]

        left = 0
        right = N - 1
        while left < right:
            if left == idx:
                left += 1
                continue
            
            if right == idx:
                right -= 1
                continue
                
            value = numbers[left] + numbers[right]
            if value == number:
                count += 1
                break
            elif value < number:
                left += 1
            else:
                right -= 1

    print(count)


solution()