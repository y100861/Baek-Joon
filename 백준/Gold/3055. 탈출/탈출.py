import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = []
for _ in range(n):
    graph.append(list(input().rstrip()))
    visited.append([0] * m)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == "*":
            q.append((i, j))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "S":
            a, b = i, j
            q.append((i, j))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "D":
            v, c = i, j

def bfs(i, j):
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (0<=nx<n and 0<=ny<m):
                continue
            
            if visited[nx][ny] == 0:
                if (graph[nx][ny] == "." or graph[nx][ny] == "S") and graph[x][y] == "*":
                    graph[nx][ny] = "*"
                    q.append((nx, ny))

                if (graph[nx][ny] == "." or graph[nx][ny] == "D") and graph[x][y] == "S":
                    graph[nx][ny] = "S"
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

bfs(a, b)

if visited[v][c] == 0:
    print("KAKTUS")
else:
    print(visited[v][c] - 1)