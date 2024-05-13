import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

def bfs():
    q = deque([(0, 0)])
    gram = 10001
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if (x, y) == (n-1, m-1):
            return min(gram, visited[x][y] - 1)

        if graph[x][y] == 2:
            gram = visited[x][y] - 1 + ((n-1-x) + (m-1-y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<n and 0<=ny<m):
                continue
            if visited[nx][ny] == 0 and (graph[nx][ny] == 0 or graph[nx][ny] == 2):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return gram

cnt = bfs()

if cnt > t:
    print("Fail")
else:
    print(cnt)