import sys

def binary_search(tree_heights, needed_height):
    start = 0
    end = tree_heights[-1]
    max_height = tree_heights[-1]

    while start <= end:
        current_height = (start+end) // 2

        cutted_height = 0
        for height in tree_heights:
            if height > current_height:
                cutted_height += height - current_height
        
        if cutted_height >= needed_height:
            max_height = current_height
            start = current_height + 1
        else:
            end = current_height - 1
    
    return max_height


def solution():
    N, M = map(int, sys.stdin.readline().split())
    tree_heights = sorted(list(map(int, sys.stdin.readline().split())))

    max_height = binary_search(tree_heights, M)
    print(max_height)

solution()