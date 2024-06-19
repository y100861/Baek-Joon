import sys
from collections import deque

input = sys.stdin.readline

def distance(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)

t = int(input())

def bfs(i, j):
    q = deque()
    if distance(i, j, end_x, end_y) <= 1000:
        visited[n] = 1
        return

    for k in range(len(mart)):
        if distance(i, j, mart[k][0], mart[k][1]) <= 1000:
            q.append((mart[k][0], mart[k][1]))
            visited[k] = 1

    while q:
        x, y = q.popleft()

        for k in range(len(mart)):
            if distance(x, y, mart[k][0], mart[k][1]) <= 1000 and visited[k] == 0:
                visited[k] = 1
                q.append((mart[k][0], mart[k][1]))

for _ in range(t):
    n = int(input())
    visited = [0] * (n + 1)

    home_x, home_y = map(int, input().split())
    mart = []
    for i in range(n):
        mart.append(list(map(int, input().split())))

    end_x, end_y = map(int, input().split())
    mart.append((end_x, end_y))

    bfs(home_x, home_y)

    if visited[n] == 1:
        print("happy")
    else:
        print("sad")