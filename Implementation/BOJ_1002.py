import sys

'''
두 점 사이의 거리를 반환합니다.
- Parameters:
    - x1: 첫 번째 점의 x 좌표
    - y1: 첫 번째 점의 y 좌표
    - x2: 두 번째 점의 x 좌표
    - y2: 두 번재 점의 y 좌표
- Returns: 두 점 사이의 거리
'''
def calc_distance(
    x1: int,
    y1: int,
    x2: int,
    y2: int
) -> float:
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        count = 0

        # 두 원의 중심이 같을 때
        if x1 == x2 and y1 == y2:
            if r1 == r2:
                count = -1
            else:
                count = 0
        else: # 중심이 다를 때
            distance = calc_distance(x1, y1, x2, y2)
            
            # 두 중심 간의 거리가 r1 + r2보다 작으면 두 점에서 만남
            if abs(r1 - r2) < distance < r1 + r2:
                count = 2
            # 같으면 한 점에서 만남
            elif distance == r1 + r2:
                count = 1
            # 중심 간의 거리와 차이가 같다면 내접함
            elif distance == abs(r1 - r2):
                count = 1
            # 더 크면 안 만남
            else:
                count = 0
        
        print(count)

solution()