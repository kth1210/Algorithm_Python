import sys
sys.setrecursionlimit(10 ** 6)

def DFS(tree, parent, parents_list):
    for child in tree[parent]:
        if parents_list[child] == 0:
            parents_list[child] = parent
            DFS(tree, child, parents_list)

def solution():
    N = int(sys.stdin.readline().rstrip())
    tree = {n:[] for n in range(1, N + 1)}
    parents_list = [0 for _ in range(N + 1)]

    for _ in range(N-1):
        f, s = map(int, sys.stdin.readline().split())
        tree[f].append(s)
        tree[s].append(f)

    parents_list[1] = -1
    DFS(tree, 1, parents_list)
    for parent in parents_list[2:]:
        print(parent)

solution()