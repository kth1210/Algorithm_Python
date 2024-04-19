import sys
INF = float('inf')

def solution():
    N = int(sys.stdin.readline().rstrip())
    stones = list(map(int, sys.stdin.readline().split()))
    cache = [INF for _ in range(N)]
    cache[0] = 0

    for j in range(1, N):
        for i in range(j):
            needed_energy = max((j - i) * (1 + abs(stones[j] - stones[i])), cache[i])
            cache[j] = min(cache[j], needed_energy)
        
    print(cache[-1])


solution()


'''
-> 방향으로만 이동
i -> j 비용 = (j - i) * (1 + abs(Ai - Aj))
한 번에 최대 K 비용 가능
K의 최솟값 구하기

0   1   2   3   4
1   4   1   3   1
---------------------
0   -1  -1  -1  -1
0   4   -1  -1  -1
0   4   2   3   2

0->3
    3 * 3 = 9 와 cache[0] 중 큰 값 = 9
1->3
    2 * (1 + 1) = 4 와 cache[1] 중 큰 값 = 4
2->3
    1 * (1 + 2) = 3 와 cache[2] 중 큰 값 = 3
< 나온 값 중 가장 작은 값을 취함 >

0->4
    4 * 1 = 4 와 cache[0] 중 큰 값 = 4
1->4
    3 * (1 + 3) = 12 와 cache[1] 중 큰 값 = 12
2->4
    2 * 1 = 2 와 cache[2] 중 큰 값 = 2 (정답))
3->4
    1 * (1 + 2) = 3 와 cache[3] 중 큰 값 = 3
< 나온 값 중 가장 작은 값을 취함 >
    
답은 2가 됨
'''