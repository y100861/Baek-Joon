import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

def bfs(i, j):
    o, v = 0, 0
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m) and visited[nx][ny] == 0:
                if graph[nx][ny] == "#":
                    continue
                
                if graph[nx][ny] == "o":
                    o += 1
                
                if graph[nx][ny] == "v":
                    v += 1
                
                visited[nx][ny] = 1
                q.append((nx, ny))
    return o, v

s = 0
w = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != "#" and visited[i][j] == 0:
            o, v = bfs(i, j)
            
            if o > v:
                s += o
            if v >= o:
                w += v

print(s, w)