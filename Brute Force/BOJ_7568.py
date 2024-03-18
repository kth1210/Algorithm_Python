import sys

def solution(N, people):
    ranks = []
    for i in range(N):
        rank = 1
        current_weight, current_height = people[i]

        for j in range(N):
            weight, height = people[j]
            if weight > current_weight and height > current_height:
                rank += 1

        ranks.append(rank)
    
    print(*ranks)

'''
input
'''
N = int(sys.stdin.readline().rstrip())
people = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

solution(N, people)