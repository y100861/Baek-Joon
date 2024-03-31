import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for i in range(m):
    graph.append([0] * (n))

square = []

for i in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, b+(d-b)):
        for j in range(a, a+(c-a)):
            graph[i][j] = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    size = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<m and 0<=ny<n):
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                size += 1
                q.append((nx, ny))
    
    square.append(size)

cnt = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt += 1
            bfs(i, j)

print(cnt)

square.sort()
for s in square:
    print(s, end=" ")