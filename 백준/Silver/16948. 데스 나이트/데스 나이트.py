import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

graph = []
for i in range(n):
    graph.append([0] * n)

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 1

    while q:
        x, y = q.popleft()

        if x == r2 and y == c2:
            break

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs(r1, c1)

if graph[r2][c2] == 0:
    print(-1)
else:
    print(graph[r2][c2] - 1)