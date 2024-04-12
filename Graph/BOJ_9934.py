import sys

def make_graph(K, graph, buildings, depth):
    if depth == K:
        graph[depth].append(buildings[0])
        return
        
    length = len(buildings)
    parent = length // 2
    graph[depth].append(buildings[parent])
    make_graph(K, graph, buildings[:parent], depth + 1)
    make_graph(K, graph, buildings[parent + 1:], depth + 1)

def solution():
    K = int(sys.stdin.readline().rstrip())
    buildings = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(K + 1)]

    make_graph(K, graph, buildings, 1)
    for row in graph[1:]:
        print(*row)

solution()