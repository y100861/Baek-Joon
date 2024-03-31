import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append([0] * m)

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    size = 0
    q = deque()
    q.append((i, j))
    graph[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue

            if graph[nx][ny] == 1:
                size += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
        
    return size

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result = max(result, bfs(i, j) + 1)

print(result)