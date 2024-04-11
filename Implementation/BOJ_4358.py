import sys

def solution():
    total_count = 0
    tree_dict = {}

    while True:
        input_tree = sys.stdin.readline().rstrip()

        if len(input_tree) == 0: break

        total_count += 1
            
        if input_tree in tree_dict:
            tree_dict[input_tree] += 1
        else:
            tree_dict[input_tree] = 1
        
    for tree_name, tree_count in sorted(tree_dict.items()):
        percent = tree_count * 100 / total_count
        print(f"{tree_name} {percent:.4f}")
    
solution()