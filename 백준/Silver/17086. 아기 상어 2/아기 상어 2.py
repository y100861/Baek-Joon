import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n and 0<=ny<m):
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(max(map(max, graph)) - 1)