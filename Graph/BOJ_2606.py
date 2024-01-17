import sys
from collections import deque

def infection_worm_virus(start_computer, computer_graph):
    is_infected = [False] * len(computer_graph)
    queue = deque()

    queue.append(start_computer)
    is_infected[start_computer] = True

    while queue:
        current_computer = queue.popleft()

        for next_computer in computer_graph[current_computer]:
            if not is_infected[next_computer]:
                queue.append(next_computer)
                is_infected[next_computer] = True

    # 첫 번째 컴퓨터 제외
    return is_infected.count(True) - 1

def solution():
    computer_count = int(sys.stdin.readline().rstrip())
    couple_of_computer = int(sys.stdin.readline().rstrip())
    computer_graph = [[] for _ in range(computer_count + 1)]

    for _ in range(couple_of_computer):
        first_computer, second_computer = map(int, sys.stdin.readline().split())

        computer_graph[first_computer].append(second_computer)
        computer_graph[second_computer].append(first_computer)

    infected_computer_count = infection_worm_virus(1, computer_graph)
    print(infected_computer_count)

solution()