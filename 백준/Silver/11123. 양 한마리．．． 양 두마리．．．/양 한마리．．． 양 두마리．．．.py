import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    graph[i][j] = "."

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == "#":
                graph[nx][ny] = "."
                q.append((nx, ny))

for _ in range(t):
    h, w = map(int, input().split())
    graph = []

    for _ in range(h):
        graph.append(list(input().rstrip()))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "#":
                cnt += 1
                bfs(i, j)

    print(cnt)