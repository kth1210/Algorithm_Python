import sys
from collections import deque

'''
start_node에서 가장 먼 노드와 해당 노드까지의 거리를 반환
'''
def find_furthest_node(graph, start_node):
    weights = [-1 for _ in range(len(graph) + 1)]
    queue = deque()
    queue.append(start_node)
    weights[start_node] = 0

    while queue:
        cur_node = queue.popleft()

        for next_node, next_weight in graph[cur_node]:
            if weights[next_node] == -1:
                weights[next_node] = weights[cur_node] + next_weight
                queue.append(next_node)

    max_weight = max(weights)
    furthest_node = weights.index(max_weight)

    return (furthest_node, max_weight)


def solution():
    V = int(sys.stdin.readline().rstrip())
    graph = {node:[] for node in range(V + 1)}

    for _ in range(V):
        input_row = list(map(int, sys.stdin.readline().split()))
        node = input_row[0]

        for idx in range(1, len(input_row) - 1, 2):
            next_node = input_row[idx]
            next_weight = input_row[idx + 1]
            graph[node].append((next_node, next_weight))
    
    furthest_node, _ = find_furthest_node(graph, 1)
    _, weight = find_furthest_node(graph, furthest_node)

    print(weight)

solution()