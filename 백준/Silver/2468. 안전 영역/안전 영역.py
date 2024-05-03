import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 0

    while q:
        x, y = q.popleft()

        for v in range(4):
            nx = x + dx[v]
            ny = y + dy[v]

            if not (0<=nx<n and 0<=ny<n):
                continue

            if visited[nx][ny] == 1:
                visited[nx][ny] = 0
                q.append((nx, ny))

result = 0
for k in range(max(map(max, graph))):
    visited = [[1] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if graph[a][b] <= k:
                visited[a][b] = 0

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt += 1
                bfs(i, j)
    
    result = max(result, cnt)

print(result)