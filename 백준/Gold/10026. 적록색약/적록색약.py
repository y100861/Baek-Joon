import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
visited = []
for i in range(n):
    graph.append(list(input().rstrip()))
    visited.append([0] * n)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    color = graph[i][j]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue
            if graph[nx][ny] == color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

cnt_1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt_1 += 1
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

visited = [[0] * n for _ in range(n)]

cnt_2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt_2 += 1
            bfs(i, j)
print(cnt_1, cnt_2)