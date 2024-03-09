import sys
from collections import deque

'''
start 노드에서 가장 먼 노드와 해당 노드까지의 거리를 반환
'''
def find_furthest(tree, start):
    weights = [-1 for _ in range(len(tree) + 1)]
    queue = deque()
    queue.append(start)
    weights[start] = 0

    while queue:
        current_node = queue.popleft()
        current_weight = weights[current_node]

        for next_node, next_weight in tree[current_node]:
            if weights[next_node] == -1:
                weights[next_node] = current_weight + next_weight
                queue.append(next_node)
        
    furthest_weight = max(weights)
    furthest_node = weights.index(furthest_weight)
    
    return (furthest_node, furthest_weight)

def solution():
    n = int(sys.stdin.readline().rstrip())
    tree = {node:[] for node in range(1, n + 1)}

    for _ in range(n - 1):
        p, c, w = map(int, sys.stdin.readline().split())
        tree[p].append((c, w))
        tree[c].append((p, w))
    
    # 아무 노드에서 가장 먼 노드를 구하고, 구한 노드에서 다시 가장 먼 노드를 구하면 지름이 됨
    random_start_node = 1
    furthest_node, _ = find_furthest(tree, random_start_node)
    _, weight = find_furthest(tree, furthest_node)

    print(weight)

solution()