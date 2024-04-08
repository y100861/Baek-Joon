import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    c = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue

            if graph[nx][ny] == "L" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                c = max(visited[nx][ny], visited[x][y] + 1)
                q.append((nx, ny))
    
    return c - 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)