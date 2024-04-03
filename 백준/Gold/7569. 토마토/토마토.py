import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = []

for a in range(h):
    graph.append([])
    for _ in range(n):
        graph[a].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

def bfs():
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nz<h and 0<=nx<n and 0<=ny<m):
                continue

            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz, nx, ny))

bfs()

day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            else:
                day = max(day, graph[i][j][k])

print(day - 1)