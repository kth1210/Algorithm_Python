import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.pre_node = None
        self.next_node = None

def solution():
    initial_str = sys.stdin.readline().rstrip()
    M = int(sys.stdin.readline().rstrip())
    head = Node(initial_str[0])
    cursor = head

    for next_str in initial_str[1:]:
        next_node = Node(next_str)
        next_node.pre_node = cursor
        cursor.next_node = next_node
        cursor = next_node

    # 문장 끝을 나타내는 더미 노드
    last_node = Node(None)
    last_node.pre_node = cursor
    cursor.next_node = last_node
    cursor = last_node
    
    for _ in range(M):
        input_command = sys.stdin.readline().split()

        if input_command[0] == "L":
            if cursor.pre_node:
                cursor = cursor.pre_node
        elif input_command[0] == "D":
            if cursor.next_node:
                cursor = cursor.next_node
        elif input_command[0] == "B":
            # head가 아닌 경우
            if cursor.pre_node:
                # 전전 노드가 있는 경우 next_node를 현재 노드로 연결
                if cursor.pre_node.pre_node:
                    cursor.pre_node.pre_node.next_node = cursor
                cursor.pre_node = cursor.pre_node.pre_node
        elif input_command[0] == "P":
            new_node = Node(input_command[1])
            # head가 아닌 경우
            if cursor.pre_node:
                new_node.next_node = cursor
                new_node.pre_node = cursor.pre_node
                cursor.pre_node.next_node = new_node
                cursor.pre_node = new_node
            else:
                new_node.next_node = cursor
                cursor.pre_node = new_node
    
    while cursor.pre_node:
        cursor = cursor.pre_node

    while cursor.next_node:
        print(cursor.data, end = "")
        cursor = cursor.next_node
    

solution()