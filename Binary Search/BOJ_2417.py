import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    start = 1
    end = n
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)

solution()


'''
제곱근 찾기
start = 1
end = number

mid 구해서 얘 제곱이 number랑 같은지 확인
    제곱이 더 크거나 같다?
        맞을 수도 있으니 일단 저장하고
        mid 줄이기 => end = mid - 1
    제곱이 더 작다?
        mid 키우기 => start = mid + 1
'''