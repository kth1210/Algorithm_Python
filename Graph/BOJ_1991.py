import sys

def print_preorder(tree, root):
    print(root, end = '')

    left_child = tree[root][0]
    right_child = tree[root][1]

    if left_child != '.':
        print_preorder(tree, left_child)

    if right_child != '.':
        print_preorder(tree, right_child)
        
def print_inorder(tree, root):
    left_child = tree[root][0]
    right_child = tree[root][1]

    if left_child != '.':
        print_inorder(tree, left_child)

    print(root, end = '')
    
    if right_child != '.':
        print_inorder(tree, right_child)
    
def print_postorder(tree, root):
    left_child = tree[root][0]
    right_child = tree[root][1]

    if left_child != '.':
        print_postorder(tree, left_child)
    
    if right_child != '.':
        print_postorder(tree, right_child)
    
    print(root, end = '')

def solution():
    N = int(sys.stdin.readline().rstrip())
    tree = {}

    for _ in range(N):
        root, left, right = sys.stdin.readline().split()
        tree[root] = [left, right]

    root = 'A'
    print_preorder(tree, root)
    print()
    print_inorder(tree, root)
    print()
    print_postorder(tree, root)

solution()