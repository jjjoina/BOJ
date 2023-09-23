import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# prefix_sum
ps = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1])