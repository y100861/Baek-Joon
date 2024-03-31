import sys
from collections import deque

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                q.append((nx, ny))
    
    return graph[n-1][m-1]

print(bfs(0, 0))