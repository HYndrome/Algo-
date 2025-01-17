import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if visited[x][y]:
       return visited[x][y]
    visited[x][y] = 1

    for i in range(4):  
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
          visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)
    return visited[x][y]

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

go = 0
for i in range(n):
    for j in range(n):
       go = max(go, dfs(i, j))
print(go)