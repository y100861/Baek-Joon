import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    graph[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)