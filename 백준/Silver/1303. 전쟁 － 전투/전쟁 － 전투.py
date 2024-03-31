import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, a):
    cnt = 1
    q = deque()
    q.append((i, j))
    graph[i][j] = -1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == a:
                cnt += 1
                graph[nx][ny] = -1
                q.append((nx, ny))

    return cnt * cnt

b2 = 0
w2 = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            w2 += bfs(i, j, "W")
        if graph[i][j] == "B":
            b2 += bfs(i, j, "B")

print(w2, end=" ")
print(b2)