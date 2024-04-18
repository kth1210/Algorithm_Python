import sys

def is_available(numbers: list, number: int) -> bool:
    visited = [False for _ in range(len(numbers[0]) + 1)]
    visited[number] = True
    next_number = numbers[1][number]
    available = (number == next_number)

    while not visited[next_number]:
        visited[next_number] = True
        next_number = numbers[1][next_number]
        if next_number == number:
            available = True
            break

    return available

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = [[number for number in range(N + 1)], [0]]
    answers = []

    for _ in range(N):
        numbers[1].append(int(sys.stdin.readline().rstrip()))
    
    for number in range(1, N + 1):
        if is_available(numbers, number):
            answers.append(number)
    
    print(len(answers))
    for number in answers:
        print(number)

solution()

'''
세로 두 줄, 가로 N칸
첫째 줄에는 1 ~ N이 차례로 들어가있음
둘째 줄에는 1 ~ N이 마구잡이로 들어있음

몇 개의 열을 뽑아서, 첫째 줄 숫자 집합과 둘째 줄 숫자 집합이 같도록 최대한 많이 뽑기

(1, 3) -> (3, 1) => 1 나왔으니 됨
(2, 1) -> (1, 3) -> (3, 1) => 안됨
(3, 1) -> (1, 3) => 3 나왔으니 됨
(4, 5) -> (5, 5) => 안됨
(5, 5) => 됨
(6, 4) -> (4, 5) -> (5, 5) => 안됨
(7, 6) -> (6, 4) -> (4, 5) -> (5, 5) => 안됨
'''