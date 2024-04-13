import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    graph = list(map(int, sys.stdin.readline().split()))
    deleted_node = int(sys.stdin.readline().rstrip())
    deleted_nodes = [deleted_node]
    graph[deleted_node] = -2
    
    for node in range(N):
        if node in deleted_nodes: continue
	
		# 부모 노드 중 삭제된 노드가 있는 지 확인
		# 있다면 해당 노드도 삭제
        parent = graph[node]
        while parent != -1:
            if parent in deleted_nodes:
                deleted_nodes.append(node)
                graph[node] = -2
                break
            parent = graph[parent]
    
    leaf_count = 0
    for node in range(N):
        if node not in deleted_nodes and node not in graph:
            leaf_count += 1
    
    print(leaf_count)

solution()