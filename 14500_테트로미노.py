# # 풀이 2. [PyPy 716ms] [Python 1224ms] 구현
# import sys; input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# ans = 0

# # 1 x 4
# for i in range(N):
#     for j in range(M-3):
#         s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
#         if ans < s:
#             ans = s

# # 4 x 1
# for i in range(N-3):
#     for j in range(M):
#         s = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
#         if ans < s:
#             ans = s

# # 2 x 2
# for i in range(N-1):
#     for j in range(M-1):
#         s = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
#         if ans < s:
#             ans = s

# # 3 x 2
# for i in range(N-2):
#     for j in range(M-1):
#         s1 = arr[i][j] + arr[i+1][j] + arr[i+2][j] + max(arr[i][j+1], arr[i+1][j+1], arr[i+2][j+1])
#         s2 = max(arr[i][j], arr[i+1][j], arr[i+2][j]) + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
#         s3 = arr[i+1][j] + arr[i+1][j+1] + max(arr[i][j]+arr[i+2][j+1], arr[i][j+1]+arr[i+2][j])
#         s = max(s1, s2, s3)
#         if ans < s:
#             ans = s

# # 2 x 3
# for i in range(N-1):
#     for j in range(M-2):
#         s1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + max(arr[i+1][j], arr[i+1][j+1], arr[i+1][j+2])
#         s2 = max(arr[i][j], arr[i][j+1], arr[i][j+2]) + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
#         s3 = arr[i][j+1] + arr[i+1][j+1] + max(arr[i][j]+arr[i+1][j+2], arr[i][j+2]+arr[i+1][j])
#         s = max(s1, s2, s3)
#         if ans < s:
#             ans = s
    
# print(ans)



# 풀이 1. [PyPy 2600ms] [Python 초과] DFS
#      -> [PyPy 368ms] [Python 840ms] 가지치기 추가
#      -> [PyPy 208ms] [Python 192ms] 凸 모양 처리 수정
import sys; input = sys.stdin.readline

def dfs(i, j, depth, cur_sum):  # depth: 현재까지 고른 개수 / i,j: 탐색 기준점
    global ans

    # 가지치기 (나머지 선택에서 모두 최대값을 골라도 ans에 못 미치는 경우)
    if ans > cur_sum + (4 - depth) * max_v:
        return

    if depth == 4:
        if ans < cur_sum:
            ans = cur_sum
        return

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 주변 네 칸
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:    # 방문하지 않은 칸
            visited[ni][nj] = 1
            dfs(ni, nj, depth+1, cur_sum+arr[ni][nj])
            if depth == 2:  # 凸 모양 처리
                dfs(i, j, depth+1, cur_sum+arr[ni][nj]) # ㄱ자든 ㅣ자든 2번째 칸으로 돌아가게 된다.
            visited[ni][nj] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
visited = [[0] * M for _ in range(N)]
max_v = max(map(max, arr))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1   # 선택
        dfs(i, j, 1, arr[i][j]) # 하나 고른 상태
        visited[i][j] = 0   # 원복

print(ans)