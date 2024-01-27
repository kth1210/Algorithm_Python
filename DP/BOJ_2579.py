import sys

def solution():
    stair_count = int(sys.stdin.readline().rstrip())
    stair_point_list = []

    for _ in range(stair_count):
        input_point = int(sys.stdin.readline().rstrip())
        stair_point_list.append(input_point)
    
    if stair_count == 1:
        print(stair_point_list[0])
    else:
        through_previous_stair = [0] * 301
        through_previous_stair[0] = 0
        through_previous_stair[1] = stair_point_list[0] + stair_point_list[1]

        nonthrough_previous_stair = [0] * 301
        nonthrough_previous_stair[0] = stair_point_list[0]
        nonthrough_previous_stair[1] = stair_point_list[1]

        for stair in range(2, stair_count):
            nonthrough_previous_stair[stair] = stair_point_list[stair] + max(through_previous_stair[stair - 2], nonthrough_previous_stair[stair - 2])
            through_previous_stair[stair] = stair_point_list[stair] + nonthrough_previous_stair[stair - 1]
        
        print(max(nonthrough_previous_stair[stair_count - 1], through_previous_stair[stair_count - 1]))

solution()