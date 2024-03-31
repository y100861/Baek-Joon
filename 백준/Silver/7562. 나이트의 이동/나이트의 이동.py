import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [2, 2, -2, -2, -1, -1, 1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    graph[i][j] = 0

    while q:
        x, y = q.popleft()

        if x == c and y == d:
            return graph[c][d]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

for _ in range(t):
    graph = []
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    for _ in range(l):
        graph.append([0] * l)
    print(bfs(a, b))