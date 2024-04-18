import sys
is_available = False

def find_friendship(graph, start_person, selected_person):
    global is_available

    if len(selected_person) == 5:
        is_available = True
        return
        
    for next_person in graph[start_person]:
        if next_person not in selected_person:
            selected_person.append(next_person)
            find_friendship(graph, next_person, selected_person)
            selected_person.pop()

def solution():
    N, M = map(int, sys.stdin.readline().split())
    graph = {person:[] for person in range(N)}

    for _ in range(M):
        first, second = map(int, sys.stdin.readline().split())
        graph[first].append(second)
        graph[second].append(first)

    for start_person in range(N):
        find_friendship(graph, start_person, [start_person])
        if is_available:
            print(1)
            return
    
    print(0)

solution()


'''
0 -> 1 -> 2 -> 3
0 -> 1 -> 4
1 -> 2 -> 3 -> 0
1 -> 4
2 -> 3 -> 0 -> 1 -> 4 됨
'''