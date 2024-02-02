import sys

def check_section_color(section, x, y, width):
    current_color = section[x][y]
    white_count = 0
    blue_count = 0

    for row in range(x, x + width):
        for col in range(y, y + width):
            if current_color != section[row][col]:
                first_section = check_section_color(section, x, y, width//2)
                second_section = check_section_color(section, x, y + width//2, width//2)
                third_section = check_section_color(section, x + width//2, y, width//2)
                fourth_section = check_section_color(section, x + width//2, y + width//2, width//2)

                white_count += first_section[0] + second_section[0] + third_section[0] + fourth_section[0]
                blue_count += first_section[1] + second_section[1] + third_section[1] + fourth_section[1]
                return [white_count, blue_count]
    
    if current_color == 0:
        white_count += 1
    else:
        blue_count += 1
    
    return [white_count, blue_count]


def solution():
    N = int(sys.stdin.readline().rstrip())
    color_list = []

    for _ in range(N):
        color_list.append(list(map(int, sys.stdin.readline().split())))
    
    white_count, blue_count = check_section_color(color_list, 0, 0, N)
    print(white_count)
    print(blue_count)

solution()