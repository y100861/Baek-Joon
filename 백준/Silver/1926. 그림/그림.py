import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
def bfs(i, j):
    global result
    cnt = 1
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
                cnt += graph[nx][ny]
                graph[nx][ny] = 0
                q.append((nx, ny))
    result = max(result, cnt)

c = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            c += 1
            bfs(i, j)

print(c)
print(result)