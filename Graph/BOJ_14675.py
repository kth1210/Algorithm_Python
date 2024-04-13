import sys

'''
트리에서 해당 노드와 연결되어 있는 다른 노드의 개수가 1개거나 없다면? 단절점이 아님
트리에서 어떠한 간선을 제거하더라도 모두 단절선이 될 것임 (사이클이 없기 때문)
'''
def solution():
    N = int(sys.stdin.readline().rstrip())
    graph = {node:[] for node in range(1, N + 1)}

    for _ in range(N - 1):
        first, second = map(int, sys.stdin.readline().split())
        graph[first].append(second)
        graph[second].append(first)
    
    q = int(sys.stdin.readline().rstrip())
    
    for _ in range(q):
        t, k = map(int, sys.stdin.readline().split())

        if t == 1:
            if len(graph[k]) < 2:
                print("no")
            else:
                print("yes")
        else:
            print("yes")

solution()