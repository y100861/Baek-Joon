import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
        
def bfs(i, j, k):
    q = deque()
    q.append((i, j, k))

    while q:
        z, x, y = q.popleft()
        if graph[z][x][y] == "E":
            return visited[z][x][y]

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nz<l and 0<=nx<r and 0<=ny<c):
                continue

            if visited[nz][nx][ny] == 0 and graph[nz][nx][ny] != "#":
                visited[nz][nx][ny] = visited[z][x][y] + 1
                q.append((nz, nx, ny))

while True:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    graph = [[] for _ in range(l)]
    for n in range(l):
        for m in range(r+1):
            a = list(input().rstrip())
            if a != []:
                graph[n].append(a)

    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    time = 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S":
                    time = bfs(i, j, k)

    if time != None:
        print("Escaped in {} minute(s).".format(time))
    else:
        print("Trapped!")