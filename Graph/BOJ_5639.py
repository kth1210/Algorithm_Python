import sys
sys.setrecursionlimit(10**6)

'''
전위 순회 결과를 후위 순회로 출력합니다.
- Parameters:
    - preorder: 전위 순회 결과
    - root_index: 루트 노드 위치
    - end_index: 마지막 노드 위치
'''
def print_postorder(
    preorder: list,
    root_index: int,
    end_index: int
):
    if root_index > end_index: return

    # 오른쪽 서브트리 시작점 찾기
    right_index = end_index + 1
    for index in range(root_index + 1, end_index + 1):
        if preorder[index] > preorder[root_index]:
            right_index = index
            break

    # 왼쪽 서브트리 탐색
    print_postorder(preorder, root_index + 1, right_index - 1)

    # 오른쪽 서브트리 탐색
    print_postorder(preorder, right_index, end_index)

    # 루트 출력
    print(preorder[root_index])


def solution():
    preorder_result = []

    while True:
        try:
            input_node = int(sys.stdin.readline().rstrip())
            preorder_result.append(input_node)
        except:
            break
    
    print_postorder(preorder_result, 0, len(preorder_result) - 1)

solution()