import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def bfs(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    graph[a][b] = "X"

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue

            if graph[nx][ny] != "X":
                if graph[nx][ny] == "P":
                    cnt += 1
                    graph[nx][ny] = "X"
                    q.append((nx, ny))
                    
                graph[nx][ny] = "X"
                q.append((nx, ny))
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i, j)

if cnt >= 1:
    print(cnt)
else:
    print("TT")